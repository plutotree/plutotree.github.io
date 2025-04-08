---
layout: post
title: "从 Cronicle 到 n8n 实践自动化工作流"
date: 2024-06-16 01:00:00 +0800
tags: [cronicle,n8n]
typora-root-url: ..
comments: true
---

> 文章经过 AI 润色

最近又开始折腾起我的服务器了，重点关注数据更新流程中的一些不满意之处：

1. Git仓库同步更新：广州和香港的服务器通过crontab任务每分钟执行git pull操作；
2. 博客同步更新：服务器上的crontab任务执行git fetch，对比差异后触发构建流程；
3. Cronicle部署：广州服务器未部署cronicle，导致定时脚本依赖crontab，无法在页面查看执行状态

### 部署cronicle

为了简化广州服务器上的定时任务管理，我部署了 [Cronicle](https://cronicle.net/)。尽管步骤较多，但得益于之前的经验，十几分钟内便完成了：

1. 申请并配置域名，设置 CNAME 转发；
2. 配置 Nginx，申请 HTTPS 证书；
3. 安装Cronicle（未使用Docker，直接通过curl命令）；
4. 修改配置文件，参照香港服务器；
5. 启动Cronicle；
6. 在页面配置任务，如进程监控脚本等；

部署过程中发现，Cronicle支持API远程访问，这正是我一直期望的功能。考虑到直接在机器上部署agent来转发命令存在安全隐患，且定制化配置页面需要额外维护，cronicle的API很好的满足了我。

### 部署n8n

有了Cronicle的API，我们具备了通过GitHub push webhook触发同步更新的基础。接下来，需要找到一个合适的服务接收webhook请求，并优雅地调用我们的API接口。这时，我想起了持续集成（CI）的概念。曾尝试使用集简云等服务，但它们通常按执行次数收费且价格不菲。经过一番搜索，我发现[n8n](https://n8n.io/)受到了许多人的推荐。其插件生态完善，能方便地集成主流服务。

部署n8n相对简单：

1. 申请域名，配置CNAME转发；
2. 配置Nginx，申请HTTPS证书；
3. 使用Docker部署n8n；

### 借助n8n实现git仓库的同步更新

配置流水线花费了一些时间，没找到直接参考的例子，只能一步步琢探索。

第一步：引入`GitHub Trigger`节点，配置了token之后，只看到一个`Test step`的按钮。点击之后，n8n能自动配置GitHub的Webhook的配置项。n8n区分了测试和正式的webhook地址，注意的是对于正式地址仍然需要手动在GitHub页面配置的。

第二步：引入`HTTP request`节点，调用cronicle的API。

简单测试了下发现流程就可以跑通了，但是这里的流水线没有对API执行的结果做回包解析。所以第三不便是需要引入`Code`节点，判断下下错误码，对于非0的情况直接抛异常了。

```javascript
code=$input.item.json.code

if (code !== 0) {
  throw new Error(`HTTP request failed with code {data[0].code}`)
}

return $input.item;
```

整体流水线的配置，只包含三类节点

![image-20240616012923132](https://pic-1251468582.picsh.myqcloud.com/pic/2024/06/16/deb5cb.png)

### 实现博客的同步更新

有了git仓库同步的经验，要解决博客的同步更新其实就比较简单了。不过这里顺便提下n8n的消息通知并不优雅，没有地方统一配置成功和失败的消息发送。目前来看需要针对每一条流水线进行配置。

![image-20240616013153943](https://pic-1251468582.picsh.myqcloud.com/pic/2024/06/16/27e707.png)

后续会将更多任务挪到n8n上面来，这只是一个起步。
