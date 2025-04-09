---
title: 使用Stable Diffusion生成美女图
date: 2023-03-14 20:00:00 +0800
tags: [AI]
categories: [AI]
slug: using-stable-diffusion-web-to-generate-ai-girl
aliases: [/2023-03-14/using-stable-diffusion-web-to-generate-ai-girl.html]
---

最近 Stable Diffusion 都大火，小红书上也是各种 AI 美女图，我也来凑一把热闹。

## 安装Stable Diffusion web UI

需要先安装好`python 3.10`和`git`（对于程序员的机器来说应该都是必备的了），直接两步执行就好了：

1. 导出git仓库：`git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`
2. 运行脚本：`webui-user.bat`，这一步下载`pytorch`可能耗时较长，耐心等待即可；
3. 执行完成之后，会提示访问<http://127.0.0.1:7860/>即可体验了；
4. 可以输入一些简单的标签体验下效果，多个标签用`,`分割，只支持英文；对于不熟悉的标签可以参考[网站](https://tags.novelai.dev/)；

这时候会发现效果没想象的那么好，尤其是生成的“美女”图，可能千奇百怪。

## 使用ChilloutMix模型

1. 在[civitai](https://civitai.com/models/6424)上下载ChilloutMix模型，模型较大，耐心等待；

2. 下载完成后放入目录`stable-diffusion-webui\models\Stable-diffusion`；

3. 重新刷新页面就可以看到左上角可以选择模型了；

   ![image-20230314200940381](https://pic-1251468582.picsh.myqcloud.com/pic/2023/03/14/88c2ac.png)

## 使用Lora插件

1. 在[civirtai](https://civitai.com/models/4503/amber-genshin-impact-lora)上下载lora插件；

2. 下载完成后放入目录`stable-diffusion-webui\extensions\sd-webui-additional-networks\models\lora`；

3. 切换到`Extensions`，选择`Load From`，搜索`Kohya-ss Additional Networks`，点击`Install`

4. 切换`Settings`，选择`Reload UI`

## 开始玩耍

1. 在[ChilloutMix](https://civitai.com/models/6424/chilloutmix)中选择你喜欢的图片，比如[这张](https://civitai.com/gallery/249318?reviewId=41236)，拷贝右侧的标签信息；

2. 看看生成的效果

   ![image-20230314202031188](https://pic-1251468582.picsh.myqcloud.com/pic/2023/03/14/53a658.png)

仔细看能发现一个比较大的问题，就是手指还是会有各种奇怪的现象
