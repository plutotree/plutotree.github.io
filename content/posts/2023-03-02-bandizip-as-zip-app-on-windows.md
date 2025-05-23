---
title: Windows 下使用 Bandizip 替换 7zip
date: 2023-03-02 12:20:00 +0800
tags: [bandizip]
categories: [Software]
slug: bandizip-as-zip-app-on-windows
aliases: [/2023-03-02/bandizip-as-zip-app-on-windows.html]
---

Windows 下一直在使用 7zip 作为唯一的压缩解压缩工具，不过解压缩的手有个一直困扰的问题：如果直接解压缩到当前目录，可能会出现一堆散乱的文件；如果解压缩到同名的目录，可能会导致多一层无用目录。原因就是因为有些压缩文件里面有根目录，而有些又没有。实际上一般会选择第二种方案，毕竟多一层目录结构总好于散乱的文件还要花时间清理。其实要解决这个问题很简单，提供一个所谓的“智能解压缩”就够了，实现起来可能也没几行代码，不知道 7zip 为啥一直没有支持。

今天看到一篇吐槽 bandzip 国内代理不退款的[帖子](https://www.v2ex.com/t/866229?p=2)，想着换个能支持“智能解压缩“的工具，参考了下[windows 上最好的压缩软件是哪个](https://www.v2ex.com/t/862733)，推荐最多的依次是 7zip (18 票)、WinRar（16 票）、Bandizip（16 票）、360 压缩（8 票）。对 WinRar 历史上一直没有好感，果断还是选择 Bandzip 了。

直接列举下 Bandzip 的优点：

1. 最重要的一点支持智能压缩，并且可以选择右键一级菜单、二级菜单或者双击直接执行；智能压缩后还支持直接打开压缩后的目录，删除压缩文件

   ![bandizip](https://pic-1251468582.file.myqcloud.com/pic/2023/03/02/33d78e.gif)

2. 支持右键直接预览文件，这点也很实用，不过我还是把它折叠到了二级菜单里面。

   ![bandizip2](https://pic-1251468582.file.myqcloud.com/pic/2023/03/02/9420a5.gif)

3. 提供了完善的选项设置，比如压缩文件名可以支持自定义，删除压缩文件可以选择是否放回收站，右键是否展示图标 icon，**支持配置备份和导入**等等；

4. 还有个很重要的点，Bandizip 不属于开源软件，部分功能需要付费才能使用。不过好在不是坑爹的订阅制，一次性付费 30 美元或 199 人民币就可以解锁专业版功能，包括广告去除、包内图片预览、压缩包修复等，还有密码器管理、恶意文件扫描等。后面两项功能其实算是和压缩工具不那么搭边，也可以认为作者比较善良，附赠了一些能力吧哈哈，只是我目前还没需求购买专业版，用一段时间再看看吧。

   ![image-20230302121805838](https://pic-1251468582.file.myqcloud.com/pic/2023/03/02/1502e3.png)

顺便研究了付费的这几个功能点

1. 密码管理器：密码记录在注册表，如果设置了主密码那么存放的就是加密后的串，如果忘记了主密码重置的时候只能清空所有密码信息。这项功能其实和所谓的密码管理器差距还挺大的，注册表毕竟也不是那么可靠，官网也说明了不要完全依赖密码管理器。

1. 压缩包内恶意软件扫描：开始我以为它自己做了一套安全扫描工具，还在想代价会不会太大了。看了文档才知道，windows 提供了反恶意软件扫描接口 (AMSI) 的通用接口标准，可以将杀毒软件的能力继承在其他产品中。不仅仅是自带的`Windows Defender`支持`AMSI`，还有`Kapersky`、`MCAfee`等等，不过看到描述的腾讯电脑管家不支持`AMSI`，还是有点感叹，国内的产品太没有开放意识了。

  ![image-20230302152033900](https://pic-1251468582.file.myqcloud.com/pic/2023/03/02/a61462.png)

1. 密码修复：其实就是提供了一个暴力破解的方式，官网也很友好的给出了预估时间

  ![image-20230302152243495](https://pic-1251468582.file.myqcloud.com/pic/2023/03/02/608d84.png)

1. 压缩包内图片预览：这个对于有需求的人来说还是挺实用性的，我个人好像没啥需求；

1. 压缩包修复：没有太明确的说明，我猜测有可能只是基于文件标准格式的简单处理，毕竟也不会保证修复的成功率；
