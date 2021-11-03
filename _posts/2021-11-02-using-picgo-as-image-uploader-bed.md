---
layout: post
title: "markdown图床实践：Typora+PicGo-core+腾讯云cos"
date: 2021-11-02 19:58:28
categories: [picgo, markdown, 腾讯云, typora]
typora-root-url: ..
comments: true
---

[TOC]

在markdown文件中一直没有采用图床，而是直接放在一起维护，之前主要有几个考虑点：

1. markdown、图片以及其他资源是一个整体，可以理解成一个项目；
2. 图片的访问权限跟随markdown文件，所在场景有统一的访问鉴权策略也可以统一生效，而图床一般都是公开访问；
3. 方便在文章维度直接删除无用的图片，而图床比较难清理文章涉及到所有历史图片；

但是在使用过程中也越来越遇到了不变之处：

1. github网站在国内访问速度较慢，文字内容还可以接受，但是大量的图片下载需要大量等待时间；
2. 在分享给他人包含图片的markdown文件时需要导出pdf，而不能直接丢个文本文件；
3. 图片占用git存储空间，图片大量增加也影响了git仓库的导出速度，而使用lfs会将问题变得复杂；
4. 在不同的文件中，图片文件存储路径有差异，需要切换的时候会很麻烦；
5. 图片的大小尺寸不方便管理，不能动态进行缩放；

权衡再三之后决定还是使用图床的方式来维护图片，图床选择了“腾讯云cos”，上传工具采用了“picgo-core”命令行工具。

## 腾讯云相关

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

在[腾讯云控制台的访问管理](https://console.cloud.tencent.com/cam/user/userType)中新建用户，可以直接使用"快速创建"。这里访问方式修改为“编程访问”，用户权限清空，可接受消息类型清空，用户名称可以用比较清晰明了的，比如`picgo-upload`。创建成功之后记录下新子账号的账号ID。

![image-20211103183050087](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/426baa.png)

回到[对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，选择“授权管理”，勾选存储桶后修改“用户权限”，增加子账号的权限，权限内容可以勾选数据读取和数据写入

![image-20211103183428148](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/1c889d.png)

到此，腾讯云上的工作做完了。其实有一点没有谈的是费用问题，这个的话还是有必要了解的，只是这篇文章略过了。

## Picgo

[PicGo](https://github.com/Molunerfinn/PicGo)是一个快速图片上传工具，其核心部分是[PicGo-Core](https://picgo.github.io/PicGo-Core-Doc/)。我们只需要使用PicGo-Core，再加上[插件能力](https://github.com/PicGo/Awesome-PicGo)就能满足需求了。

```bash
# 如果没有npm的话需要先安装
# brew install npm
# 安装picgo
npm install picgo -g
# 安装picgo插件
picgo install autocopy
picgo install rename-file
```

接着就是对picgo进行配置了，包括图床配置和插件配置，可以参考[这里](https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90)执行`picgo set uploader`交互式的方式配置腾讯云cos相关信息，不过我更喜欢直接编辑配置文件。

Windows下路径为： `%HOMEPATH%\.picgo\config.json`，Mac路径为`~/.picgo/config.json`。

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

需要编辑的字段内容都已经注明了，重命名插件的具体参数可以参考[这里](https://github.com/liuwave/picgo-plugin-rename-file)。配置完成之后可以通过执行`picgo upload xxx.png`来验证图片上传及插件配置是否生效。这里xxx.png可以支持本地也可以支持网络的url，是不是很方便？

![image-20211103191206334](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/80da56.png)

https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/80da56.png，这个图片地址符合我们插件的配置。

## Typora

打开偏好设置，勾选之后可以点击“验证图片上传选项”确认上传是否正常。

![image-20211103191432287](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/30c0b7.png)

这里要注意下mac系统的这个PicGo-Core选项并不可用，需要选择Custom Commeand，并手动输入命令，另外命令还需要输入完整才行。我配置的命令内容如下：

```bash
/opt/homebrew/bin/node /opt/homebrew/bin/picgo upload
```

![image-20211103191923824](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/03/5f16d7.png)

好了，配置完成之后可以在文章中很方便的插入图片了。另外提一点，本地图片转化为网络图片是需要一些时间的，如果在中途不小心编辑到这段内容的话，会导致后续替换失败。不过好在我们是用了autocopy的插件，我们只要手动ctrl+v就可以了。



