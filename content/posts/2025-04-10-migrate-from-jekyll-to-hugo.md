---
title: 博客从 Jekyll 迁移到 Hugo：Valine评论系统相关问题
date: 2025-04-10T01:00:00+08:00
tags: [jekyll, hugo]
featuredImage: https://pic-1251468582.file.myqcloud.com/pic/2025/04/10/VZLUG8.jpg
slug: migrate-from-jekyll-to-hugo
---



## 评论系统

之前Jekyll用的无后端的valine评论系统，在Hugo中也是直接支持的，在`hugo.toml`的`params.page.comment.valine`进行配置即可，具体字段可以参考[valine官方文档](https://valine.js.org/configuration.html)。但是遇到了一个问题，我需要配置昵称是必须字段，但是配置的`requiredFields`却是无效的。研究后从文件`layouts/partials/comment.html`中看到只针对特定字段进行了处理。所以需要将该文件拷贝到项目中相同目录下，增加下述代码：

```html
{{- with $valine.requiredFields -}}
	{{- $commentConfig = dict "requiredFields" . | dict "valine" | merge $commentConfig -}}
{{- end -}}
```

运行之后评论能正常展示，但是随机头像却是一个都无法展示，比如下面这个头像地址，如果将域名换成<www.gravatar.com>是能正常显示的。

<https://gravatar.loli.net/avatar/d41d8cd98f00b204e9800998ecf8427e?d=wavatar&v=1.5.2>

而Gravatar的官网在国内访问可能存在较多问题，而<gravatar.loli.net>似乎处理上存在问题，建议换成<cn.cravatar.com>，需要配置avatar_cdn即可。配置完也发现是无效的，和上面的`requiredFields`一样，需要先增加配置字段的处理。

{{- with $valine.avatar_cdn -}}
	{{- $commentConfig = dict "avatar_cdn" . | dict "valine" | merge $commentConfig -}}
{{- end -}}
```

这样修改之后Gravatar头像和随机头像的展示都正常了。但是如果邮箱为空的话，随机头像展示的都是固定的一个，并没有随机效果。我希望能在邮箱字段为空的时候，用昵称计算md5来获取随机头像。这一点valine本身并没有提供支持，而且现在valine也没提供源码，需要的话就只能直接改发布文件了。将 valine.min.js中的`t.get("mail")` 修改为 `t.get("mail")||t.get("nick")`即可，相当于邮箱为空的时候就用昵称。修改之后需要自己发布到CDN才能用，这个就不在这篇文章中进行说明了。

下一个遇到的评论问题就是在昵称字段输入QQ的时候，无法直接获取QQ昵称和头像，QQ头像和昵称是通过下述域名获取的：

<https://api.qjqq.cn/api/qqinfo?qq=1645253>

这个不是官方接口，而是第三方的接口。这个接口最近似乎无法使用了，返回出错后会跳转到网站
在该网站查询qq相关api接口可以看到这个：
https://api.nsmao.net/doc/21

注册后试了下可以免费接入，但是回包结构和Valine里面的处理会存在差异。现在有了AI就是方便，直接丢给他压缩的代码，他就能帮我找到代码逻辑了。

```javascript
var a = function(e, t) {
    var n = i.default.store.get(o.QQCacheKey);
    n && n.qq == e ? t && t(n) : i.default.ajax({
        url: "https://api.plutotree.cn/qq_api/qqinfo?qq=" + e,
        method: "get"
    }).then(function(e) {
        return e.json()
    }).then(function(n) {
        if (200 == n.code) {
            var r = n.name,
                a = n.imgurl,
                u = {
                    nick: r,
                    qq: e,
                    pic: a
                };
            i.default.store.set(o.QQCacheKey, u),
            t && t(u)
        }
    })
}
```

如果想要在Valine中进行使用，有两种解决方案：

方案1：修改Valine中的请求url以及回包解析
只要将url修改下`https://api.nsmao.net/api/qq/query?key=xx&qq=`，然后将`{var r=n.name,a=n.imgurl`改成`{var r=n.data.nick,a=n.data.avatar`即可了。

但是这里我们的密钥需要暴露在前端，毕竟不太好。

方案2：后台封装中转接口

这个的话有自己的服务器实现起来倒也没啥难度，让AI直接帮忙写代码即可，不过还是涉及到nginx转发，服务维护等等，尽管我完成了这个中转服务，最后还是决定不用了。

下一个问题就是如果url变了的话，评论数据是需要迁移的。数据是存储在LeanCloud的，其实就是直接改下数据的url即可。这个可以通过自己的脚本来修改，甚至评论很少的时候，手动修改也是可行的，我就是这么操作哈。

到这里基本问题解决了，但是valine作为一个并没有真正开源的服务，其实有点想要放弃了，在之前Jekyll引入valine的时候，waline算是刚刚出来，现在似乎比较流行了，后面还是迁移到waline吧。
