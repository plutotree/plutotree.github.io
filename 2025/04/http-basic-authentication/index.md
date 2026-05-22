# HTTP Basic Authentication (HTTP 基本认证)


<!--more-->

## 什么是 HTTP 基本认证

对于部署的一些纯前端系统，本身并没有内置用户校验。但是我们又不希望其他用户能无限制使用，所以希望能有简单的用户校验流程。这就需要用到 HTTP Basic Authentication (HTTP 基本认证) 。

HTTP 基本认证是一种非常简单的认证机制，广泛用于保护 Web 应用的资源。它通过 HTTP Header 传递用户名和密码，并通过 Base64 编码对其进行简单的编码（注意：不是加密）。实际应用中需要配合 HTTPS 使用，以防止明文凭据在网络中被拦截。

## HTTP 基本认证的交互流程

{{< mermaid >}}
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务端
    Client->>Server: 请求资源 (无认证信息)
    Server-->>Client: 返回 401 Unauthorized + WWW-Authenticate 头
    Client->>Client: 提示用户输入用户名和密码
    Client->>Server: 发送请求 (包含 Authorization 头)
    Server->>Server: 验证用户名和密码
    alt 验证成功
        Server-->>Client: 返回资源 (200 OK)
    else 验证失败
        Server-->>Client: 返回 401 Unauthorized
    end
{{< /mermaid >}}

1. 客户端请求资源：客户端向服务器发起请求，但未包含认证信息。
2. 服务器返回 401 响应：服务器返回 401 Unauthorized 状态码，同时通过 WWW-Authenticate 头提示客户端需要提供凭证。
3. 客户端提示输入凭证：客户端向用户请求输入用户名和密码。
4. 客户端发送认证信息：客户端将用户名和密码通过 Base64 编码后，添加到 HTTP Header 的 Authorization
5. 服务器验证凭证：服务器解码并验证用户名和密码的正确性。
6. 服务器返回响应：
   - 如果验证成功，返回 200 OK 和资源。
   - 如果验证失败，返回 401 Unauthorized 并要求重新认证。

下面我们用 curl 命令的交互来看下整个流程能更加清晰，可以使用参数`-u` 来指定用户名和密码，而实际处理中会对用户名和密码计算 MD5，并填充到 Authorization 的 Header 中。

```bash
curl --verbose "https://some.examples.com"

> GET / HTTP/1.1
> Accept: */*
>
< HTTP/1.1 401 Unauthorized
< WWW-Authenticate: Basic realm="Need Authorization"

curl -u user:pwd --verbose "https://some.examples.com"
> GET / HTTP/1.1
> Authorization: Basic Base64ByUserAndPwd
> Accept: */*
>
< HTTP/1.1 200 OK
```

我们再来看下浏览器中访问效果，对于返回需要校验的网站，浏览器会弹出一个弹框，要求输入用户名和密码：

![auth-window](https://pic-1251468582.file.myqcloud.com/pic/2025/04/21/BdTsLs.png)

## 如何在 Nginx 中配置 HTTP 基本认证

### 创建用户凭据文件

1. 安装 `htpasswd` 工具：

   ```bash
   apt-get install apache2-utils
   ```

2. 创建新用户，执行命令后输入密码

   ```bash
   cd /etc/nginx/conf.d/

   htpasswd -c ./auth.htpasswd username
   ```

3. 设置文件权限，设置文件所有者和nginx的执行用户一致

   ```bash
   chmod 600 auth.htpasswd
   chown xx:xx auth.htpasswd
   ```

4. 可以本地校验下

   ```bash
   htpasswd -v ./auth.htpasswd username
   ```

### 配置nginx

配置较为简单，只要增加`auth_basic`和`auth_basic_user_file`就好了

```conf
location / {
    auth_basic "Need Authorization";  # 认证提示内容，显示取决于客户端实现
    auth_basic_user_file /etc/nginx/conf.d/auth.htpasswd

    # 其他的配置
}
```

配置完成后，重新加载下nginx的配置

```bash
systemctl reload nginx
```

### 测试访问

可以在浏览器中输入网址，访问验证下是否有弹出一个认证窗口，提示用户输入用户名和密码。验证成功后，服务器将正常返回资源，否则会要求重新输入用户名和密码。如果浏览器关闭重新打开后，会要求重新输入。

## 如何无感登录

增加了这一步骤的确是更安全了，但是每次打开页面需要输入一遍用户名和密码，这又带来了很大的不便。我们可以通过浏览器自带的密码保存，在下次要求认证的时候，直接按登录按钮就好了。

有没有可能更进一步，连登录按钮也不用按，在可信任的电脑上默认帮我登录呢。[BitWarden](https://bitwarden.com/help/basic-auth-autofill/) 还真提供了这样的功能，能隐藏式自动填充用户名和密码的功能，这样对使用者就完全无感了。理论上还有种方式可以通过浏览器的插件来直接设置Header。

## 总结

HTTP 基本认证算是一种最简单有效的认证方式，如果需要更复杂的认证机制，可以考虑其他方式，如 OAuth、JWT 或基于 Session 的认证。

