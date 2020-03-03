---
layout: post
title:  "使用bitwarden搭建自己的密码管理服务器"
date:   2020-03-02 00:10:00 +0800
categories: 
---

## 背景

大概是15年开始使用[1password](https://1password.com/)作为自己的密码管理软件，看中的是多平台同步的功能、方便快捷的密码填充和不错的交互操作，最重要的一点是自己可控的密码库（而不是使用官方的云同步）。当然最大的问题是同步方式只支持dropbox，每次同步都得搭梯子才能进行。

`1password`在2016-2017年开始推出订阅版之后，逐步就开始抛弃独立版本了。一开始还保留了一次性购买授权的方案，但是很快就被彻底放弃了。我对密码管理没特别的诉求，已有的版本功能正常就继续用着。直到有一天发现chrome的`1password`插件无法使用了。作为拖延症晚期患者当然没在第一时间就去寻找替换方案（其实是找了而没有实施），只能在需要的时候手动打开软件去搜索密码了。

## 搭建web服务器

- 拥有一台自己的服务器，拥有一个自己的域名，这个流程就不再赘述了；

- 申请https证书，不得不说[acme.sh](https://github.com/acmesh-official/acme.sh)一键申请&部署证书，真的是太方便了

  - 安装acme.sh

  	```bash
  	curl  https://get.acme.sh | sh
  	```

  - 生成证书

    这里选择使用standalone的方式，需要确保这个域名是未在使用的，如果默认的80端口已经被使用，还可以指定其他端口
    
    ```bash
acme.sh  --issue -d xx.yourdomain.com --standalone
    ```
    
  - 拷贝证书：nginx的配置文件和证书文件放在`/etc/nginx.conf/conf.d/`目录下
  
    ```bash
    acme.sh --installcert -d xx.yourdomain.com \
    --fullchain-file /etc/nginx/conf.d/xx.yourdomail.com.crt \
    --key-file /etc/nginx/conf.d/xx.yourdomail.com.key \
    --reloadcmd "systemctl restart nginx"
    ```
  
- nginx的完整配置文件`/etc/nginx/conf.d/xx.yourdomail.com.conf`如下:

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

  这里将请求转发至了本地的12345端口（就是我们后面要部署的bitwarden服务的地址）

##  部署bitwarden服务

由于官方的服务需要用到sqlserver，资源占用较大，推荐使用[bitwarden_rs](https://github.com/dani-garcia/bitwarden_rs)，用ruby实现的bitwarden服务端兼容版本，这就是开源的好处。

不得不说docker安装真的是太方便，两句命令搞定：第二句里面我把对外的端口调整成了12345，而不是默认的80，就是前面所配置的nginx转发目标地址。

```bash
docker pull bitwardenrs/server:latest
docker run -d --name bitwarden -v /bw-data/:/data/ -p 12345:80 bitwardenrs/server:latest
```

## 迁移1password的数据

官方的[教程](https://help.bitwarden.com/article/import-from-1password/)说的比较清楚了，登录的数据包括历史密码信息都能比较完整导入到bitwarden，但是类别信息并不能完整保留，因为2者的类别定义也不一致。安全备注信息也比价好的导入到了bitwarden，但是有些分类信息也作为备注导入到了bitwarden。

## 使用感受

待补充