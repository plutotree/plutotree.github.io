---
title: 使用autohotkey实现evernote的多级标题
date: 2021-11-03 11:32:25 +0800
tags: [autohotkey, evernote]
slug: use-autohotkey-to-implement-evernote-multi-level-title
aliases: [/2021-11-03/use-autohotkey-to-implement-evernote-multi-level-title.html]
---

一直没想明白 evernote 国际版为啥一直不支持多级标题，这几乎是一个基础特性的缺失。网上的资料大多是用`autohotkey`来实现的，基本处理函数如下：

![image-20211103193322072](https://pic-1251468582.file.myqcloud.com/pic/2021/11/03/baca97.png)

这里没有好的设置行间距的方式，样式比较丑，今天发现有直接对剪切板操作的[脚本](https://www.autohotkey.com/boards/viewtopic.php?t=80706)，转而一想我们可以通过直接插入`<h1></h1>`等 html 标签的方式来实现标题的设置，因为 evernote 本身是支持这些标签的。

这里直接给 AutoHotkey 的代码：

![image-20211103193531372](https://pic-1251468582.file.myqcloud.com/pic/2021/11/03/2ac5a0.png)

有一点的问题在于`ClipWait`看着并不生效，没有后续的`Sleep`是会有概率粘贴失败的。所以这个方案也并不完美，只是勉强可用，需要的可以[点击下载](https://pic-1251468582.file.myqcloud.com/pic/2021/11/03/20dd72.ahk)。

实现效果就是这样子（这里的序号手动加的）：

![image-20211103195545338](https://pic-1251468582.file.myqcloud.com/pic/2021/11/03/f48336.png)
