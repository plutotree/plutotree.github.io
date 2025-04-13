---
title: 博客从 Jekyll 迁移到 Hugo：Valine评论系统相关问题
date: 2025-04-10T01:00:00+08:00
tags: [jekyll, hugo]
featuredImage: https://pic-1251468582.file.myqcloud.com/pic/2025/04/10/VZLUG8.jpg
slug: migrate-from-jekyll-to-hugo
---


最近将博客从 Jekyll 迁移到 Hugo 了，虽然 Valine 评论系统在 Hugo 中可以直接通过配置文件 `hugo.toml` 进行设置，但在实际使用中发现了一些坑，以下是整理的解决方案。

## 1. 配置 `requiredFields` 无效问题

在 Valine 的官方文档中提到，可以通过 `requiredFields` 配置字段来设置评论时的必填项，比如昵称、邮箱等。然而，在 Hugo 中直接配置后发现该功能无效。

### 问题原因

Hugo 主题下文件 `layouts/partials/comment.html` 文件中只针对部分字段进行了处理，而没有对 `requiredFields` 进行正确处理。

### 解决方法

将 `comment.html` 文件复制到项目中相同目录下，然后增加以下代码：

```html
{{- with $valine.requiredFields -}}
    {{- $commentConfig = dict "requiredFields" . | dict "valine" | merge $commentConfig -}}
{{- end -}}
```

## 2. Gravatar 头像显示问题

在配置头像时发现，随机头像无法正常显示，例如以下头像地址。但是将域名替换为 [www.gravatar.com](https://www.gravatar.com/avatar/d41d8cd98f00b204e9800998ecf8427e?d=wavatar&v=1.5.2) 则可以正常显示。  
<https://gravatar.loli.net/avatar/d41d8cd98f00b204e9800998ecf8427e?d=wavatar&v=1.5.2>

### 问题原因

Gravatar的中转服务，gravatar.loli.net 存在处理上的问题，导致随机头像无法显示。

### 解决方法

由于 Gravatar 的官网在国内访问存在较多问题，更换了另一个 Gravatar 的中转服务： cn.gravatar.com。在配置文件中增加avatar_cdn之后，发现这个配置不生效。需要增加类似的处理逻辑，修改 `comment.html` 文件：

```html
{{- with $valine.avatar_cdn -}}
    {{- $commentConfig = dict "avatar_cdn" . | dict "valine" | merge $commentConfig -}}
{{- end -}}
```

修改后，Gravatar 头像和随机头像的显示恢复正常，但邮箱为空时随机头像无法随机。

## 邮箱为空时随机头像问题

### 问题原因

Valine 在邮箱为空时不管昵称是什么，都是直接根据空邮箱去生成 MD5，这导致生成的其实是固定头像。

### 解决方法

将 `valine.min.js` 中的 `t.get("mail")` 修改为 `t.get("mail") || t.get("nick")`，即邮箱为空时使用昵称计算随机头像。修改后需要将文件发布到 CDN 才能使用，具体步骤不在此赘述。

## QQ头像和昵称获取问题

在 Valine 中，昵称字段输入 QQ 时，是可以摘取QQ头像和昵称的，但是测试的时候却发现无法获取。在Chrome的调试窗口，可以看到访问该地址会报错： https://api.qjqq.cn/api/qqinfo?qq=12345 。

### 问题原因

几天前我验证的时候浏览器直接打开这个地址是能存在访问的，只是在Valine中使用存在跨域问题。但是神奇的是，今天这个服务彻底失效了。麻烦的是我连服务的回包结构都不知道。好在有强大的AI，直接把压缩的JS代码丢给AI，它就能很聪明的分析出QQ头像和昵称的处理逻辑。


```javascript
var a = function(e, t) {
    var n = i.default.store.get(o.QQCacheKey);
    n && n.qq == e ? t && t(n) : i.default.ajax({
        url: "https://api.nsmao.net/api/qq/query?key=xx&qq=" + e,
        method: "get"
    }).then(function(e) {
        return e.json()
    }).then(function(n) {
        if (200 == n.code) {
            var r = n.data.nick,
                a = n.data.avatar,
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

### 解决方法

访问API接口，可以发现会跳转到使用奶思猫 API 。在该网站搜索后，发现存在免费的QQ信息服务接口 https://api.nsmao.net/api/qq/query，需要注册后获取密钥即可访问。需要注意的是，这个API的回包结构和Valine中使用的是不一致的。

解决方案1：修改Valine中请求的url以及回包解析。这个方案修改起来很容易，最大的问题是暴露了密钥，尽管密钥是免费的，但也不能随便暴露呀。

- 修改请求URL：`api.njqq.cn/api/qqinfo?qq=xxx` 修改成 `https://api.nsmao.net/api/qq/query?key=xx&qq=`
- 修改昵称和头像的获取：`{var r=n.name,a=n.imgurl`改成`{var r=n.data.nick,a=n.data.avatar`。

解决方案2：后台提供中转服务

通过自己的服务器封装中转接口，避免密钥暴露，接口可以完全丢给AI实现，但需要额外的服务维护成本。

## 评论数据迁移问题

如果 URL 发生变化，评论数据需要迁移。Valine 的数据存储在 LeanCloud 中，可以通过脚本或手动修改数据的 URL。当然评论较少时，其实手动修改也是可以的。

## 总结与展望

在从 Jekyll 迁移到 Hugo 的过程中，Valine 评论系统的配置和使用遇到了一些问题，但通过调整配置文件、修改模板文件和优化代码，基本解决了这些问题。然而，Valine 作为一个没有完全开源的服务，存在一定的局限性。在考虑未来的评论系统选择时，Waline似乎是一个更好的选择。Waline 不仅功能更完善，还提供了更好的国内访问体验和开源支持。唯一的缺点就是需要后台服务（这一点严格来说也不能算缺点）。
