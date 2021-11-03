---
layout: post
title: "markdown图床实践：Typora+PicGo-core+腾讯云cos"
date: 2021-11-02 19:58:28
categories: [picgo, markdown, 腾讯云, typora]
typora-root-url: ..
comments: true
---

## 前言

Markdown已然成为事实上的技术文档编写标准，作为markdown编辑器，typora也收到越来越多人的推荐和喜爱。在markdown中我们经常需要插入图片，而markdown只是普通文本文件，因此图片只能作为外部链接而存在。这里的链接可以使用本地的相对路径，也可以使用网络url。当使用网络url的时候，我们需要一个地方去维护和存储图片，这就是我们所谓的“图床”。

而我之前一直没有考虑使用图床，图片都是和markdown文件一起在git里面维护，主要的考虑点有：

1. markdown文件以及图片是作为一个整体，可以理解成是一个项目，那么项目内容本身就是密不可分的；
2. 图片的访问权限可以跟随markdown文件，需要时可以有统一的访问鉴权策略；
3. 方便管理一篇文章的所有图片，对于无用的图片可以直接删除；

在使用过程中遇到了越来越多的不便之处：

1. github网站在国内访问速度较慢，文字影响不大，大量的图片下载耗时很影响体验；
2. 不方便直接分享给他人markdown文件，需要导出pdf或者打包进行分享；
3. 在github仓库中，大量的图片也影响了git仓库的导出速度；
4. 本地存储图片时，图片存储路径在不同场景有差异，不方便统一管理；
5. 不能方便地进行图片的动态缩放；

权衡之后决定还是决定拥抱“图床”。typora自带支持iPic、uPic、PicGo等图片上传工具，我选择国人开发的PicGo。另外因为一直在用腾讯云服务器，自然选择了腾讯云cos作为图床的云存储。

## 腾讯云

### 对象存储

1. 在[对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)创建一个存储桶，选择所属地域，填写桶名称，访问权限选择“公有读私有写”

   ![image-20211103181029412](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/5a3994.png)

2. 点击桶名称进入管理页面，在左侧“域名与传输管理”中打开默认CDN加速域名，这里需要理解下CDN和源站的概念

   ![image-20211103181539258](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/4320b5.png)

3. 回到文件列表页，可以在页面进行上传测试，点击“详情”可以查看文件的具体信息，这里对象有两个访问地址，一个是源站域名，一个是加速域名，我们一般都会选择加速域名。

   ![image-20211103181734118](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/2142aa.png)

### 数据万象

使用图床还有一点很重要的作用是能实现动态的图片处理，简单的比如缩放、裁剪，复杂的比如高斯模糊、水印等等，这里需要用到腾讯的[数据万象](https://console.cloud.tencent.com/ci)。在数据万象的存储通管理中，选择绑定存储桶即可。

![image-20211103182342325](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/fc984c.png)

点击存储通名称进入管理页面，发现这里也有个域名管理，通过这个域名访问才会支持图片的在线处理功能，这个域名本身也是支持cdn加速的，我们会统一采用这个域名来提供用户访问。

![image-20211103182312319](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/752d6c.png)

### 访问授权

在[腾讯云控制台的访问管理](https://console.cloud.tencent.com/cam/user/userType)中新建用户，可以直接使用"快速创建"。这里访问方式修改为“编程访问”，用户权限清空，可接受消息类型清空，用户名称可以用比较清晰明了的，比如`picgo-upload`。创建成功之后能看到子账号的账号ID，还有SecretId和SecretKey，把这些信息记录下来，我们后续需要用到。

![image-20211103183050087](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/426baa.png)

回到[对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，选择“授权管理”，勾选存储桶后修改“用户权限”，增加子账号的权限，权限内容可以勾选数据读取和数据写入。

![image-20211103183428148](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/1c889d.png)

到此，腾讯云上的工作做完了。其实有一点没有谈的是费用问题，这个的话还是有必要了解的，只是这篇文章略过了。

## Picgo

[PicGo](https://github.com/Molunerfinn/PicGo)是一款开源跨平台的图片上传工具，能方便地上传至各种图床和云存储服务器上。可以使用带图片GUI的应用，也可以直接使用其核心部分基于命令行的[PicGo-Core](https://picgo.github.io/PicGo-Core-Doc/)。我推荐直接使用PicGo-Core，再加上[插件能力](https://github.com/PicGo/Awesome-PicGo)足够满足我们的需求了。

```bash
# 如果没有npm的话需要先安装
# brew install npm
# 安装picgo
npm install picgo -g
# 安装picgo插件
picgo install autocopy
picgo install rename-file
```

安装完picgo和插件之后需要进行相关配置，同样有两种方式，一种是[基于命令行的交互输入](https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90)，而另一种是推荐的直接修改配置文件。配置文件在Windows下路径为 `%HOMEPATH%\.picgo\config.json`，Mac下路径为`~/.picgo/config.json`。

```json
{
  "picBed": {
    "current": "tcyun",
    "tcyun": {
      "secretId": "子账号的SecretId",
      "secretKey": "子账号的SecretKey",
      "bucket": "Bucket名称",
      "appId": "",
      "area": "COS区域，类似ap-shanghai",
      "path": "",
      "customUrl": "数据万象url",
      "version": "v5"
    },
    "uploader": "tcyun",
    "transformer": "path"
  },
  "picgoPlugins": {
    "picgo-plugin-rename-file": true,
    "picgo-plugin-autocopy": true
  },
  "picgo-plugin-rename-file": {
    "format": "pic/{y}/{m}/{d}/{rand:6}"
  }
}
```

根据上面的注释进行字段的编辑，重命名插件的具体参数可以参考[这里](https://github.com/liuwave/picgo-plugin-rename-file)。配置完成之后可以通过执行`picgo upload xxx.png`来验证图片上传及插件配置是否生效。这里xxx.png可以支持本地也可以支持网络的url。如果上传成功之后能看到完整的url，同时也会将url写入剪切板，可以直接在浏览器中进行访问验证。

![image-20211103191206334](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/80da56.png)

比如这个地址<https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/80da56.png，>，可以查看其链接规则是符合rename-file插件的配置的。

## Typora

打开偏好设置，按需要勾选之后点击“验证图片上传选项”确认上传是否正常。

![image-20211103191432287](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/30c0b7.png)

这里要注意下mac系统的`PicGo-Core`选项并不可用，需要选择`Custom Commeand`，手动输入命令。另外命令还需要输入完整地址（我尝试了三遍才知道）。我配置的命令内容如下：

```bash
/opt/homebrew/bin/node /opt/homebrew/bin/picgo upload
```

![image-20211103191923824](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/5f16d7.png)

好了，到这里就可以在文章中很方便的插入图片了。使用过程中，可以发现本地图片转化为网络图片是需要一些时间，在上传成功之后才会替换掉本地url。如果在中途不小心修改或者删除了相关内容，会导致后续替换url失败。好在我们是用了autocopy的插件，正确地址已经写入剪切板了，只要ctrl+v就可以了啦。

## 将历史文章中的本地图片批量上传

不想旧文章使用本地图片，而新文章才使用网络图片，这些批量化的工作当然得交给程序。用node或许是比较理想的方式，可以直接以API形式调用picgo。但这是在我用python写到最后才想起的点。不多说，直接给代码，直接保存运行就好了：

```python
import os
import re
import pyperclip

def Upload(img):
    # 使用picgo上传，需要安装插件autocopy
    pyperclip.copy("")
    ret = os.system('picgo upload ./{}'.format(img))
    if ret != 0:
        print('图片[{}]上传失败'.format(img))
        return img
    new_img = pyperclip.paste().rstrip('\n')
    if not new_img:
        print('图片[{}]似乎上传失败'.format(img))
        return img
    print('图片[{}]上传成功 ->[{}]'.format(img, new_img))
    return new_img

def Process(root, file):
    content = ''
    print('process file:{}/{}'.format(root, file))
    inf = open('{}/{}'.format(root, file), 'r')
    for line in inf.readlines():
        result = re.finditer('!\[([^]]*)\]\(([^)]*)\)', line)
        update = False
        new_line = ''
        last_pos = 0
        for r in result:
            img = r.group(2)
            if not (img.startswith('http://') or img.startswith('https://')):
                update = True
                new_line += line[last_pos : r.start(2)]
                last_pos = r.end(2)
                new_line += Upload(img)
        new_line += line[last_pos:]
        if update:
            content += new_line
        else:
            content += line
    inf.close()

    outf = open('{}/{}'.format(root, file), 'w')
    outf.write(content)
    outf.close()

if __name__ == '__main__':
    for root, dirs, files in os.walk('./_posts/'):
        for file in files:
            if file.endswith(".md") or file.endswith(".markdown"):
                Process(root, file)

```

