---
title: "记录一个curl访问的https证书问题"
date: 2023-02-01 12:30:00 +0800
tags: [ssl]
---

## 问题描述

前段时间证书更新后，发现在 linux 服务器上使用 curl 命令访问会提示`curl: (60) Peer's Certificate issuer is not recognized.`

```bash
[root@centos]# curl "https://www.plutotree.cn"
curl: (60) Peer's Certificate issuer is not recognized.
More details here: http://curl.haxx.se/docs/sslcerts.html

curl performs SSL certificate verification by default, using a "bundle"
 of Certificate Authority (CA) public keys (CA certs). If the default
 bundle file isn't adequate, you can specify an alternate file
 using the --cacert option.
If this HTTPS server uses a certificate signed by a CA represented in
 the bundle, the certificate verification probably failed due to a
 problem with the certificate (it might be expired, or the name might
 not match the domain name in the URL).
If you'd like to turn off curl's verification of the certificate, use
 the -k (or --insecure) option.
```

增加`--verbose`参数可以得到更详细的信息

```bash
* Initializing NSS with certpath: sql:/etc/pki/nssdb
*   CAfile: /etc/pki/tls/certs/ca-bundle.crt
  CApath: none
* Server certificate:
*       subject: CN=plutotree.cn
*       start date: Feb 01 09:09:40 2023 GMT
*       expire date: May 02 09:09:39 2023 GMT
*       common name: plutotree.cn
*       issuer: CN=R3,O=Let's Encrypt,C=US
* NSS error -8179 (SEC_ERROR_UNKNOWN_ISSUER)
* Peer's Certificate issuer is not recognized.
* Closing connection 0
```

使用浏览器访问的时候是正常的，不管是 chrome 还是 Safari。

## 问题定位及解决

### 尝试更新根证书无效

首先怀疑的是根证书问题，搜索之后最常见的解决方案是更新根证书，在`centos`下执行下述命令：

```bash
yum install ca-certificates
update-ca-trust force-enable
update-ca-trust extract
```

### 尝试手动更新证书

另外的思路就是手动将网站证书添加，但这个终归不是一个好办法，简单尝试了（发现仍然无效）下就放弃了（估计是哪一步操作不对）。

### 从 zerossl 更换回 Let's Encrypt

这次使用`acme.sh`更新证书的时候，是有提示默认服务切换至 zerossl，怀疑是不是 zerossl 颁发的证书导致无法正确识别，所以切换回去使用 Let's Encrypt 了，结果当然是仍然无效。

### 发现一段重要说明

在 acme.sh 发现一段重要说明：

> Nginx 的配置`ssl_certificate`使用`/etc/nginx/ssl/fullchain.cer`，而非`/etc/nginx/ssl/<domain>.cer` ，否则`SSL Labs`的测试会报`Chain issues Incomplete`错误。

立刻尝试手动拷贝文件并且修改了下 nginx 配置，问题直接就解决了。

之前的证书安装命令压根就没有指定`--fullchain-file`，而只是指定了`--key-file`和`--cert-file`，而在 nginx 下`--cert-file`是不需要的，`--fullchain-file`确实必须的。之前看文档的时候就错看了这一点结果悲剧了。

```bash
acme.sh --install-cert -d plutotree.cn --cert-file /etc/nginx/conf.d/plutotree.cn.cer  --key-file /etc/nginx/conf.d/plutotree.cn.key --fullchain-file /etc/nginx/conf.d/fullchain.cer --reloadcmd "systemctl force-reload nginx"
```

## 总结教训

搜索引擎不是万能的！还是要先多看看文档！
