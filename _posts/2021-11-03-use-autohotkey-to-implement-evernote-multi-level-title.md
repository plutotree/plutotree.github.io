---
layout: post
title: "使用autohotkey实现evernote的多级标题"
date: 2021-11-03 11:32:25
categories: [autohotkey, evernote, multi-level title]
typora-root-url: ..
comments: true
---

一直没想明白evernote国际版为啥一直不支持多级标题，这几乎是一个基础特性的缺失。网上的资料大多是用`autohotkey`来实现的，其原理大致上是先使用`Home`和`END`选中文本，然后执行加粗、字体放大等操作，基本处理函数如下：

```
IncreaseFontSize(n) {
	Send {END}
	Send +{HOME}
	Send ^b
	Loop, %n% {
		Send ^+.
	}
	Send {END}
	Return
}
```

有个问题是没找到好用的设置行间距的方式，样式还是比较丑，所以一直也没用上这种方式。今天重拾`autohotkey`的时候，发现有直接对剪切板操作的[脚本](https://www.autohotkey.com/boards/viewtopic.php?t=80706)



