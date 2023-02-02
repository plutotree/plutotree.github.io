---
layout: post
title: "在mac上使用RIME"
date: 2021-12-15 17:50:00
categories: [autohotkey, evernote, multi-level title]
typora-root-url: ..
comments: true
---

## 为啥需要更换输入法？

我们一直在讨论互联网上的隐私泄漏问题，比如姓名、电话、家庭信息，进一步职业、地理位置等。如果要说拥有最多隐私的产品是什么，很多人会选择微信、微博、抖音等产品。因为它们有我们的关系链、兴趣爱好、LBS 信息、作息习惯等等，这些都对，但是有没有想过

## 安装鼠须管

1. 安装 RIME，安装过程需要输入密码

   ```bash
   brew install squirrel --cask
   ```

2. 添加输入法，在输入法管理中添加“鼠须管”输入法

   ![image-20211215143151253](https://pic-1251468582.picsh.myqcloud.com/pic/2021/12/15/ca0e5b.png)

3. 这时候就可以正常输入了，不过出来的是繁体字，需要调整为简体字。在输入状态下，按 F4 可以选择切换为简体。

   ![image-20211215143850106](https://pic-1251468582.picsh.myqcloud.com/pic/2021/12/15/1d8811.png)

4. 在`~/Library/Rime`下创建文件`squirrel.custom.yaml`，内容如下：

   ```yaml
   patch:
     app_options: {}
     style:
       # 设置皮肤颜色
       color_scheme: clean_white
       horizontal: true
       inline_preedit: true
       corner_radius: 5
   ```

5. 现在可以实现横向选择了

   ![image-20211216175250203](https://pic-1251468582.picsh.myqcloud.com/pic/2021/12/16/7074b9.png)
