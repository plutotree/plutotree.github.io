# 搭建自己的bitwarden密码管理服务器


## 背景

大概是 15 年开始使用[1password](https://1password.com/)作为自己的密码管理软件，看中的是多平台同步的功能、方便快捷的密码填充和不错的交互操作，最重要的一点是自己可控的密码库（而不是使用官方的云同步）。最大的一个问题是同步方式只支持 dropbox，每次同步都得搭梯子才能进行。

但是`1password`在 2016-2017 年开始推出订阅版之后，一开始仍然保留了一次性购买永久授权的方案，并且保持着双版本同步更新。接着独立版更新力度就逐步减弱，重点都放在了订阅版本，毕竟对公司来说订阅版本更加赚钱。windows 的最后一个[独立版本](https://app-updates.agilebits.com/product_history/OPW4)的发布时间在 2017 年 9 月份，mac 的最后一个[独立版本](https://app-updates.agilebits.com/product_history/OPM4)的发布时间在 2018 年 5 月份。尽管不再更新了，不过对密码管理没特别的诉求，已有的版本功能足够满足需求了，就继续正常使用着。直到有一天突然发现 chrome 的`1password`插件无法使用了，而这个是重度的使用场景。这个时候只能打开软件手动搜索了，作为拖延症晚期患者没在第一时间去寻找替代方案（其实是找了而没有实施），直到最近换了一个新的手机之后才决定要切换新的密码管理软件。

并没有花太多时间去寻找新选择，很快确定了 bitwarden，开源、多平台、功能齐全，甚至可以自己部署独立服务器，还有什么理由不用它呢。尽管用官方存储不会有什么大问题，一开始也尝试了下，不过选择自己部署会更可控些。

## 搭建 web 服务器

- 拥有一台自己的服务器，拥有一个自己的域名，建议使用一个二级域名作为 bitwarden 服务，下文以`bw.yourdomail.com`为例。国内域名要走备案流程复杂，国外的话就很方便了。这个流程就不细述了。

- 申请 https 证书，不得不说[acme.sh](https://github.com/acmesh-official/acme.sh)一键申请&部署证书，真的是太方便了

  - 安装 acme.sh

    ```bash
    curl  https://get.acme.sh | sh
    ```

  - 生成证书

    这里选择使用 standalone 的方式，需要确保这个域名是未在使用的，如果默认的 80 端口已经被使用，还可以指定其他端口

  ```bash
  acme.sh  --issue -d xx.yourdomain.com --standalone
  ```

  - 拷贝证书：nginx 的配置文件和证书文件放在`/etc/nginx.conf/conf.d/`目录下

    ```bash
    acme.sh --installcert -d xx.yourdomain.com \
    --fullchain-file /etc/nginx/conf.d/xx.yourdomail.com.crt \
    --key-file /etc/nginx/conf.d/xx.yourdomail.com.key \
    --reloadcmd "systemctl restart nginx"
    ```

- 用 nginx 实现域名的转发，对于`https://xx.yourdomail.com`的请求转发至本地的 12345 端口，即后续部署的 bitwarden 服务的端口，nginx 的完整配置文件`/etc/nginx/conf.d/xx.yourdomail.com.conf`如下:

  ```bash
  server {
      listen 443 ssl;
      server_name xx.yourdomail.com;
      ssl_certificate conf.d/xx.yourdomail.com.crt;
      ssl_certificate_key conf.d/xx.yourdomail.com.key;
      ssl_session_timeout 5m;
      ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
      ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
      ssl_prefer_server_ciphers on;

      location / {
          proxy_pass http://127.0.0.1:12345;
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection "upgrade";
      }
  }
  ```

  这里将请求转发至了本地的 12345 端口（就是我们后面要部署的 bitwarden 服务的地址）

## 部署 bitwarden 服务

由于官方的服务需要用到 sqlserver，资源占用较大，推荐使用[bitwarden_rs](https://github.com/dani-garcia/bitwarden_rs)，用 ruby 实现的 bitwarden 服务端兼容版本，这就是开源的好处。

不得不说 docker 安装真的是太方便，两句命令搞定：第二句里面我把对外的端口调整成了 12345，而不是默认的 80，就是前面所配置的 nginx 转发目标地址。

```bash
docker pull bitwardenrs/server:latest
docker run -d --name bitwarden -v /bw-data/:/data/ -p 12345:80 bitwardenrs/server:latest
```

## 迁移 1password 的数据

官方的[教程](https://help.bitwarden.com/article/import-from-1password/)说的比较清楚，导入操作很快，有几点提一下：

- 登录信息比较成功迁移，包括登录密码的历史信息、收藏信息都能比较完整导入到 bitwarden；

- 安全备注以及密码、会员信息、护照、软件许可、银行账户等类别能成功导入到 bitwarden，不过都是作为安全笔记的类型而存在，除了部分字段外，原始信息基本上都作为了自定义字段进行保存；

  这里的自定义字段会存在问题，比如护照的有效期在 1password 里面保存的是时间戳而不是可见的日期格式（这点很合理，因为展现格式是可以更换的），这样导入到 bitwarden 之后就变成了一串数字；比如性别保存的是 male/female，导入后也是这些字符串。bitwarden 自定义类型是只有 text 和 bool 的，没有其他类型！

## 使用感受

1. 1password 有非常完善的类型，包含信用卡、护照、银行账户、邮箱、软件 license、服务器、数据库等等，并且每个类型的字段都非常完整。对比而言，bitwarden 只有卡片和身份两个类型，卡片只有信用卡的最基础的几个字段，身份是相对完整的个人信息。所以除了登录密码，bitwarden 维护其他数据还是不太方便。
2. 1password 是或做比较实时地自动同步，而 bitwarden 的自动同步间隔是非常长的，几个小时才同步一次，而且没有发现有自动同步的时间设置选项，官方回复[在此](https://www.reddit.com/r/Bitwarden/comments/75i6xm/is_there_a_way_to_change_the_sync_frequency/)，的确没有相关同步时间选项，只能手动同步；
3. 其他待补充

## 二步验证（TOTP）

TOTP (Time-based One-Time Password) 直接翻译就是有有效期的一次性密码，只是他的场景用在了登录时的二次验证，所以就姑且叫他二次验证吧。对 TOTP 想要了解更多的，[这篇文章](https://www.iplaysoft.com/two-factor-authentication.html)做了不错的介绍，当然也可以直接看[wiki](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm)。

官方版本需要付费的 TOTP 功能在自己搭建 bitwarden_rs 服务直接支持了，不过涉及到扫描二维码，相关操作需要用手机上的 bitwarden app 进行。操作很简单，编辑相应的登录项，选择 totp 字段，扫描屏幕二维码，搞定！在实际使用时不会自动切换到 totp 验证码，需要手动拷贝（也可能是我的操作姿势不对？后面再确认）

另外提一句，bitwarden 主账户也是可以打开 totp 的，问题来了，可以使用 bitwarden 来作为自己的 totp 服务么？想象下，你登录 bitwarden 需要验证码，而这个验证码需要进入 bitwarden 才能拿到，是不是死循环了，无法进入了，所以不要这样做，还是选择 authy 或者 google authenticator 吧。

