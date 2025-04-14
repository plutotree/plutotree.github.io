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
{{- with $valine.requiredFields -}} {{- $commentConfig = dict "requiredFields" .
| dict "valine" | merge $commentConfig -}} {{- end -}}
```

## 2. Gravatar 头像显示问题

在配置头像时发现，随机头像无法正常显示，例如以下头像地址。但是将域名替换为 [www.gravatar.com](https://www.gravatar.com/avatar/d41d8cd98f00b204e9800998ecf8427e?d=wavatar&v=1.5.2) 则可以正常显示。  
<https://gravatar.loli.net/avatar/d41d8cd98f00b204e9800998ecf8427e?d=wavatar&v=1.5.2>

### 问题原因

Gravatar 的中转服务，gravatar.loli.net 存在处理上的问题，导致随机头像无法显示。

### 解决方法

由于 Gravatar 的官网在国内访问存在较多问题，更换了另一个 Gravatar 的中转服务： cn.gravatar.com。在配置文件中增加 avatar_cdn 之后，发现这个配置不生效。需要增加类似的处理逻辑，修改 `comment.html` 文件：

```html
{{- with $valine.avatar_cdn -}} {{- $commentConfig = dict "avatar_cdn" . | dict
"valine" | merge $commentConfig -}} {{- end -}}
```

修改后，Gravatar 头像和随机头像的显示恢复正常，但邮箱为空时随机头像无法随机。

## 邮箱为空时头像并不会随机

### 问题原因

获取随机头像的 MD5 是根据邮箱地址进行生成，而邮箱地址为空时其生成的 MD5 是固定的，这也导致获取的也都是固定头像。

### 解决方法

将 `valine.min.js` 中的 `t.get("mail")` 修改为 `t.get("mail") || t.get("nick")`，即邮箱为空时使用昵称计算随机头像。修改后需要将文件发布到 CDN 才能使用，具体步骤不在此赘述。

## QQ 头像和昵称获取问题

在 Valine 中，昵称字段输入 QQ 时，预期是可以获取 QQ 头像和昵称的，但是实际测试的时候却无法正确获取。在 Chrome 的调试窗口，可以看到访问第三方的 API 地址的时候会报错：

<https://api.qjqq.cn/api/qqinfo?qq=12345>

### 问题原因

就在写该文章的几天前直接在浏览器中访问这个地址还是正常的，不过会因为跨域问题而导致在 Valine 中无法正常使用。今天访问这个地址，发现这个服务已经无法访问了，页面会跳转到一个 API 服务平台[奶思猫](https://api.nsmao.net/)。

### 解决方法

在网站上搜索后，发现有免费的[QQ 信息服务接口](https://api.nsmao.net/api/qq/query)。这个 API 的回包结构和 Valine 中使用的 api.qjqq.cn 是不一致的。由于原来的接口已经下线，正确的回包结构目前也不清楚。好在现在有强大的 AI，直接把压缩的 JS 代码丢给 AI，它就能分析出原来处理 QQ 头像和昵称的逻辑。

```javascript
var a = function (e, t) {
  var n = i.default.store.get(o.QQCacheKey);
  n && n.qq == e
    ? t && t(n)
    : i.default
        .ajax({
          url: "https://api.nsmao.net/api/qq/query?key=xx&qq=" + e,
          method: "get",
        })
        .then(function (e) {
          return e.json();
        })
        .then(function (n) {
          if (200 == n.code) {
            var r = n.data.nick,
              a = n.data.avatar,
              u = {
                nick: r,
                qq: e,
                pic: a,
              };
            i.default.store.set(o.QQCacheKey, u), t && t(u);
          }
        });
};
```

我们有两种方案分别是在客户端直接修改和在服务端进行中转：

方案 1：修改 Valine 中请求的 url 以及回包解析逻辑。方案修改起来很容易，最大的问题是会暴露了密钥。

- 修改请求 URL：`api.njqq.cn/api/qqinfo?qq=xxx` 修改成 `https://api.nsmao.net/api/qq/query?key=xx&qq=`
- 修改昵称和头像的获取：`{var r=n.name,a=n.imgurl` 修改成 `{var r=n.data.nick,a=n.data.avatar`。

方案 2：后台提供中转服务

通过自己的服务器封装中转接口，避免密钥暴露，接口可以丢给 AI 实现，但需要额外的服务维护成本。

下面是用 golang 实现的获取QQ资料的 HTTP 服务，功能就是将奶思猫提供的 QQ 资料的API接口转换成适配Valine的格式。需要设置下密钥和访问端口。

```golang
package main

import (
        "encoding/json"
        "fmt"
        "io/ioutil"
        "log"
        "net/http"
        "os"
)

// APIResponse represents the response from the QQ API
type APIResponse struct {
        Code     int    `json:"code"`
        Msg      string `json:"msg"`
        Data     QQData `json:"data"`
        ExecTime float64 `json:"exec_time"`
        IP       string  `json:"ip"`
}

// QQData represents the data field in the API response
type QQData struct {
        Nick      string `json:"nick"`
        Qid       string `json:"qid"`
        RegTime   string `json:"regTime"`
        Level     int    `json:"level"`
        Avatar    string `json:"avatar"`
        Email     string `json:"email"`
        IsVip     bool   `json:"is_vip"`
        IsYearsVip bool  `json:"is_years_vip"`
        VipLevel  int    `json:"vip_level"`
}

// ClientResponse represents the response we'll send to the client
type ClientResponse struct {
        Code   int    `json:"code"`
        Name   string `json:"name"`
        ImgURL string `json:"imgurl"`
        Email  string `json:"email"`
}

func main() {
        // Get the API key from environment variable or use default
        apiKey := os.Getenv("QQ_API_KEY")
        if apiKey == "" {
                apiKey = "MY_KEY" // Default key for development
        }

        http.HandleFunc("/qq_api/qqinfo", func(w http.ResponseWriter, r *http.Request) {
                // Get QQ number from query parameter
                qqNumber := r.URL.Query().Get("qq")
                if qqNumber == "" {
                        http.Error(w, "Missing qq parameter", http.StatusBadRequest)
                        return
                }

                // Construct the API URL
                apiURL := fmt.Sprintf("https://api.nsmao.net/api/qq/query?key=%s&qq=%s", apiKey, qqNumber)

                // Make the request to the QQ API
                resp, err := http.Get(apiURL)
                if err != nil {
                        log.Printf("Error making request to QQ API: %v", err)
                        http.Error(w, "Failed to fetch QQ information", http.StatusInternalServerError)
                        return
                }
                defer resp.Body.Close()

                // Read the response body
                body, err := ioutil.ReadAll(resp.Body)
                if err != nil {
                        log.Printf("Error reading response body: %v", err)
                        http.Error(w, "Failed to read QQ information", http.StatusInternalServerError)
                        return
                }

                // Parse the API response
                var apiResp APIResponse
                if err := json.Unmarshal(body, &apiResp); err != nil {
                        log.Printf("Error parsing API response: %v", err)
                        http.Error(w, "Failed to parse QQ information", http.StatusInternalServerError)
                        return
                }

                // Prepare the client response
                clientResp := ClientResponse{
                        Code:   200,
                        Name:   "",
                        ImgURL: "",
                        Email:  "",
                }

                // Only populate the fields if the API request was successful
                if apiResp.Code == 200 {
                        clientResp.Name = apiResp.Data.Nick
                        clientResp.ImgURL = apiResp.Data.Avatar
                        clientResp.Email = apiResp.Data.Email
                } else {
                        // If the API request failed, pass along the error code
                        clientResp.Code = apiResp.Code
                        log.Printf("API returned error: %s", apiResp.Msg)
                }

                // Set content type header
                w.Header().Set("Content-Type", "application/json")

                // Encode and send the response
                if err := json.NewEncoder(w).Encode(clientResp); err != nil {
                        log.Printf("Error encoding client response: %v", err)
                        http.Error(w, "Failed to encode response", http.StatusInternalServerError)
                        return
                }
        })

        // Start the HTTP server
        port := os.Getenv("PORT")
        if port == "" {
                port = "52101" // Default port
        }

        log.Printf("Starting server on port %s", port)
        if err := http.ListenAndServe(":"+port, nil); err != nil {
                log.Fatalf("Failed to start server: %v", err)
        }
}
```

另外还需要在 nginx 配置中进行 proxy_pass 的转发配置，这里不再赘述i。

## 评论数据迁移

如果 URL 没有改变，评论数据是无需处理的。如果 URL 发生了变化，并且你想保留之前的评论数据，那就需要手动进行迁移。 Valine 的所有数据是存储在 LeanCloud 中，可以很方便地通过脚本进行修改。

不过因为我的评论量少得可怜，我就直接手动修改了。

## 总结

Valine 评论系统现在已经基于处理停止维护的状态了，而且新的版本源友也没有完全开源的服务，存在较大的局限性。未来如果有时间的话，升级 Waline 似乎是一个比较好的选择。Waline 不仅功能更完善，还提供了更好的国内访问体验和开源支持。另外最大的差异其实是 Waline 是需要后台服务，这一点可以说是优点，也可以说是限制。
