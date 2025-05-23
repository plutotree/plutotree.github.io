---
title: 从告警聊到 IFTTT
date: 2023-02-14 18:30:00 +0800
tags: [ifttt]
slug: from-monitor-to-ifttt-intro
aliases: [/2023-02-14/from-monitor-to-ifttt-intro.html]
---

## 从腾讯云告警聊起

自从将腾讯云的 CVM 流量计费模式从”按宽带计费“调整成”按流量计费“之后，总担心突发的`DDOS`攻击或者随便写个脚本都会导致我的流量费用短时间暴增。目前的带宽上限是 `10Mbps`，如果被人攻击了 7 天，那么总费用就需要`10*86400*7/8=756`元。那如果被攻击了 3 个月没发现呢？我账户里面没有那么多钱啊，应该早被停止服务了，那么我应该也就发现了。

为了避免损失不断扩大，我们需要有完备的监控体系和通知体系了，幸好腾讯云提供的监控体系还是比较完整的。不管是传统的的邮件、短信、电话（收费）外，还是企业微信、钉钉、飞书、slack（这些算是腾讯适配他们的协议了），此外还能支持微信服务号（算是腾讯内部的特殊权利了），以及自定义回调服务。

![push_flow1.drawio](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/cd6b7c.svg)

对比起来群晖的通知体系就比较弱了，支持电子邮件、短信（第三方）、群晖管家的推送和自定义回调服务。而对网站的一些监控是只能依赖 pushover 的。

![push_flow2.drawio](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/694702.svg)

以后可能还有各种告警通知，在想这里能不能统一管理，并且可以比较方便的扩展。

![push_flow3.drawio](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/e9f65f.svg)

如果再往外扩展一步的话，其实不止是告警，也可能是各种其他事件。哈哈，这就有点 IFTTT 的味道了。

![push_flow4.drawio](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/4b3b1d.svg)

## IFTTT 现状

想到这里，我去搜索了一遍国内`IFTTT`的[现状](https://www.jianshu.com/p/a0239b1cd3ff)，结果是惨不忍睹啊。看看这些名字尽管都很山寨，但是怎么就一个也不剩了呢。这些文章大部分还是在 2015 年的，最近几年甚至都没什么人聊起`IFTTT`了。

- [如果是](https://www.ruguoshi.com)
- [如果云](https://www.ruguoyun.com)
- [如果就](https://www.ruguojiu.com)
- [假如就](https://www.jiarujiu.com)
- [一旦就](https://yidanjiu.com)

与此同时，我也去搜了国外的`IFTTT`发展，发现[`Integromat`](https://www.integromat.com/)的也已经玩出了新花样。看看下面的流程图，收到邮件后，表格中插入一行，然后对附件进行处理，将图片发表到 Facebook，将文档打包上传到 dropbox。

![img](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/6fd89c.jpg)

不得不说，这真的很酷，有没有一点像 devops 流行的流水线逻辑。但其实更羡慕的是国外软件开放的思路，几乎大的产品都能提供开放 API，不管是 google 系列的 gmail、google docs，还是 facebook、twitter、instagram、dropbox、evernote、notion 等等。不管是十几年前的产品，还是这几年新出的产品，都会将 API 开放作为重要的功能之一。

反观国内的话，手 Q 和微信带来的 OAuth 流行（每个产品都相当入口哈哈），这几年随着钉钉、企业微信、飞书等协同办公平台的兴起，整个现状比之前是好了太多了。尽管目前相对国外而言还是挺大，不过还是可以期待几年之后，互联网产品能真正从底子里把开放作为基础功能（不做开放功能就别上线哈哈！）。

## 集简云实操 IFTTT

说回国内`IFTTT`的现状，搜索了下一圈发现[集简云](https://apps.jijyun.cn/)算是继承了`IFTTT`的思想，看下他的界面，从”选择触发动作“到”执行这个动作“就是它最基本的设计。

![image-20230214190945114](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/d773b6.png)

并且有点意外的是支持的应用还挺多的，号称有 493 个应用。

![image-20230214192341974](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/e53466.png)

当然受限于应用本身开放的能力，有些功能是实现不了的。举例来说，小红书就只能支持”订单“相关的出发条件，而不能支持”关注的人“发表文章等条件。

![image-20230214193431309](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/12bcbe.png)

但是实测的时候发现很多应用各种报错、各种无法使用，包括头条、抖音、曹操叫车等等之类的，本来还想着实现个好玩的流程实验下的。

回到开始的问题，我们是否可以依赖集简云来实现消息管理中心呢，先拿腾讯云告警通知实验下，整个流程还算是比较顺利。

1. 使用 webhook 作为触发条件：

   ![image-20230214194139810](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/209b7b.png)

2. 点击下一步后，会生成一个 webhook 的 URL 地址，将该 url 地址填写到腾讯云告警的回调地址中

   ![image-20230214194233285](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/dd00fc.png)

   ![image-20230214194340309](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/103b84.png)

3. 点击下一步后可以获取样本数据，这时候可以先在腾讯云上配置一个容易触发的告警事件，比如 CPU>1%之类的，触发之后可以在这里看到样本数据内容，主要是方便后续选择相应字段。这里没有关于回包格式更多清晰的描述，不过至少标准的 json 是支持的。

   ![image-20230214194544104](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/87b347.png)

4. 终于可以到第二步的执行事件了，使用 push 作为关键字试了下，只找到一个`pushplus`，那就用用看吧。

   ![image-20230214194749133](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/f73570.png)

5. 账号这里，参考说明操作就行了，需要关注公众号然后在菜单中去选择相关 token 信息，如果需要使用客服消息的时候则需要有手动操作行为，并且只有 48 小时有效期，否则使用模板消息下发（有总次数限制，之前微信还说要下架后面不了了之了）。不过这也算是微信服务号消息发送的统一解决方案了。

6. 消息标题和内容操作还是比较傻瓜化的，直接选择相应字段作为变量就可以了。

   ![image-20230214195246604](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/033b30.png)

7. 保存之后可以测试下效果，发现在微信公众号里面可以收到消息了。

   ![image-20230214195511674](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/ba1d63.png)

整体用下来，感觉还是不够专业啊，变量设置尽管够”傻瓜化“，但是没看到有更高级的用法。比如需要有高级的变量选择器，类似 XML 的 XPATH 选择器；针对回包内的字段有不同的分支处理；甚至是支持简单的脚本逻辑等；至少是距离我的想像有比较大的差距，另外界面设计上感觉也不太专业。

最后发现每个月的免费调用次数只有 500 次（真的有点少），收费价格貌似还挺高的，当然我不可能成为付费用户了。不过作为国内可能仅有的类`IFTTT`产品，有需要的还是可以多支持支持。

![image-20230214195950161](https://pic-1251468582.file.myqcloud.com/pic/2023/02/14/de61a8.png)

后面我估计还是会使用`IFTTT`来进行相关处理，或者自己单独搞一套似乎也不太难，以后再说吧！
