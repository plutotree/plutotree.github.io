---
layout: post
title: "在PC上使用RIME"
date: 2021-12-15 17:50:00 +0800
tags: [rime]
typora-root-url: ..
comments: true
---

## 为啥需要更换输入法？

我们一直在讨论互联网上的隐私泄漏问题，比如姓名、电话、家庭信息，进一步职业、地理位置等。如果要说拥有最多隐私的产品是什么，很多人会选择微信、微博、抖音等产品。因为它们有我们的关系链、兴趣爱好、LBS 信息、作息习惯等等。这些都没有问题，但是有没有想过这些信息都是依赖输入法输入的，而目前大部分互联网输入法都会将输入词传输到云端。想象下，将你多年的输入词完整分析一遍，能得到多少你个人信息，以及社交信息，甚至分析你的个人性格都不是啥问题。

## 选择一款开源的输入法

[RIME](https://rime.im/)算是最好、最强大的开源输入法，甚至没有之一。它在一个统一的后端服务基础上，利用不同的前端来支持 Windows、MacOS、Android、Linux，实现跨操作系统和跨设备。在 Windows 下叫“小狼毫”，在 Mac 下是“鼠须管”，此外还有 Linux 和 android 版本。这里只介绍 windows 和 mac 上的安装和使用方式，而 iOS 上输入法如果不打开联网权限安全和隐私保护是可靠的。

## 安装及基础使用

### Windows 下小狼毫的安装

1. 在官网下载[小狼毫](https://rime.im/download/)；

2. 安裝完成需要选择输入方案，可以只保留朙月输入法，在皮肤选择中可以选择自己喜欢的样式

   ![image-20230206181740122](https://pic-1251468582.picsh.myqcloud.com/pic/2023/02/06/742201.png)

3. 这时候可以正常输入，但是展示的是繁体字，按 F4 选择简体；

   ![image-20230206182144701](https://pic-1251468582.picsh.myqcloud.com/pic/2023/02/06/7edf8d.png)

4. 默认的是纵向选择候选词，可能不符合一般的使用习惯，可以打开目录`%APPDATA%\Rime`中下的文件`weasel.custom.yaml`（如果不存在的话则新建即可），增加下述内容：

   ```yaml
   patch:
     style:
       horizontal: true
   ```

5. 在菜单中选择“重新部署”后，就可以看到效果了；

### Mac 下鼠须管的安装

1. 安装 RIME，安装过程需要输入密码

   ```bash
   brew install squirrel --cask
   ```

2. 添加输入法，在输入法管理中添加“鼠须管”输入法

   ![image-20211215143151253](https://pic-1251468582.picsh.myqcloud.com/pic/2021/12/15/ca0e5b.png)

3. 这时候就可以正常输入了，不过出来的是繁体字，需要调整为简体字。在输入状态下，按 F4 可以选择切换为简体。

   ![image-20211215143850106](https://pic-1251468582.picsh.myqcloud.com/pic/2021/12/15/1d8811.png)

4. 默认的是纵向选择候选词，可能不符合一般的使用习惯，打开目录`~/Library/Rime`下的文件`squirrel.custom.yaml`（如果不存在则新建），内容如下：

   ```yaml
   patch:
     style:
       horizontal: true
   ```

5. 选择重新部署后，可以实现横向选择了

   ![image-20211216175250203](https://pic-1251468582.picsh.myqcloud.com/pic/2021/12/16/7074b9.png)
