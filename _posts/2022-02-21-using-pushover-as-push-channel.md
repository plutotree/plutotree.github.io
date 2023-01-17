---
layout: post
title: "从pushbullet切换到pushover作为消息通知工具"
date: 2023-01-17 20:300:00
categories: [pushover]
typora-root-url: ..
comments: true
---

## 背景

之前有在用pushbullet作为消息推送服务，以及偶尔将它当做多平台的分享工具。前几天发现我的bitwarden网站突然不能正常使用了，想着还是需要接入页面的自动监控及消息推送，这时才发现pushbullet竟然不支持iOS（前几个月换回了iPhone作为主力机），这不是推我离开pushbullet么。大致搜索了下，除了pushover似乎也没有太多好的选择了。

## pushbullet和pushover对比

### 支持的平台

|         | Pushbullet | Pushover |
| ------- | ---------- | -------- |
| iOS     | -          | 支持     |
| Android | 支持       | 支持     |
| 浏览器  | 支持       | 支持     |
| Windows | 支持       | -        |

### 费用对比

- Pushover：
  - 提供30天的试用期，后续使用需要付费；
  - 个人用户5美元一个平台（一次性收费），不限制设备数量；
- Pushbullet
  - 每月提供500条免费消息，超出则需要升级Pro版本；
  - 订阅制，一个月4.99美元（年付折合3.33美元/月）；

### 其他说明

- Pushove提供了较为丰富的push相关选项，包括自定义图标、自定义声音、url跳转，以及优先级别的设置等；
- Pushbullet提供了基于channel维度的推送，并且可以开放给其他用户订阅；Pushbullet提供了**发送文件**、设备间共享信息、短信复制等能力；

### 总结说明

- Pushover是一个比较纯粹的消息推送服务，它的能力主要在于此也仅限于此。如果你需要发送消息提醒到手机，那应该算是最佳选择了；
- Pushbullet竟然不支持iOS，这点其实还是有点意外的，原生windows可以不支持，但是怎么能不支持iPhone呢；
- Pushbullet除了发送消息外，各设备之间的消息分享非常有用，有段时间我都把它当做手机（安卓）和电脑（Mac）之间进行文字和文件传递的首选产品。当然如果使用的是iPhone和mac，那必然是AirDrop的填下了。
- Pushbullet的Channel和订阅能力也算是提供了一个社区化的能力，可以运营自己的channel，不断增加粉丝，然后可以发送广告哈。

## 国内的同类软件

参考知乎上的帖子【[国内有没有类似于Pushover,PushBullet等消息推送app](https://www.zhihu.com/question/36023349)】的评论相关信息，调研里面的一些产品。

### [server酱](https://sct.ftqq.com/)

第一版本依赖于微信消息，第二版本可以支持多通道，推荐使用企业微信和[pushdeer](https://github.com/easychen/pushdeer)。pushover除了有完善的消息推送能力外，还能支持自建服务器。目前在运营中，并且发展势头较好，开始做自己的推送生态，下面是官网拷贝的。

- [Server酱Turbo](https://sct.ftqq.com/)：支持企业微信、微信服务号、钉钉、飞书群机器人等多通道的在线服务，无需搭建直接使用，每天有免费额度
- [Wecom酱](https://github.com/easychen/wecomchan)：通过企业微信推送消息到微信的消息推送函数和在线服务方案，开源免费，可自己搭建。支持多语言。
- [PushDeer](https://github.com/easychen/pushdeer)：可自行搭建的、无需安装APP的开源推送方案。同时也提供安装APP的降级方案给低版本/没有快应用的系统。支持作为Server酱的通道进行推送，所有支持Server酱的软件和插件都能直接整合PushDeer。

免费用户一天只能发送5条消息，并且仅显示标题（基本上不太有可用性），收费价格每个月8元或者年付39元（折合3.5元/月）。不过能力和规划看着还是不错的，如果有时间的话我会深度体验并且对比下pushdeer和pushover的。

### [喵提醒](https://miaotixing.com/)

之前推荐的是基于微信公众号消息回复，需要用户48小时内主动发送消息，我认为是没啥实用性的。模板消息可以一定程度上解决这个问题，不过微信模板前端时间也一直在传要下线呢。另外还支持短信、电话提醒（当然是收费的），我看目前还新支持了安卓app和iMessage消息提醒。具体没有详细了解，不过这网站页面做的真的是丑，让人不得不怀疑它能做得多好。

[server饭](https://letserver.run/)

它的介绍是“服务器给微信发通知消息 或用微信控制你的服务器”，从这段话中也可以看出其实定位还是有差异的，它的出发点应该是通过微信控制服务器，所以服务器上是必须安装有agent的，这里也不做详细介绍 了。
