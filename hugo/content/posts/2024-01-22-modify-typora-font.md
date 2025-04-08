---
title: "修改Typora的字体"
date: 2024-01-22 18:00:00 +0800
tags: [typora]
comments: true
---

从typora早起的beta版就开始在用，现在应该越来越多人认可其作为最佳Markdown编辑器。不过默认情况下，在windows展示的字体使用的是宋体，看起来其实不太美观，我们可以换成其它更好看得字体。微软雅黑我最不满意的是中文标点符号太丑，甚至不太容易分辨，我还是比较喜欢思源黑体。

![image-20240122190421116](https://pic-1251468582.picsh.myqcloud.com/pic/2024/01/22/c47fcf.png)

在Typora的设置页中打开主题文件夹，然后新建一个 `xx.user.css` 文件（`xx`为你的主题名称），比如使用的主题为github，则新建一个 `github.user.css` 文件，里面的内容填写如下：

```css
body {
    font-family: "Source Han Sans SC", "Microsoft Yahei";
}

header, .context-menu, .megamenu-content, footer{
    font-family: "Source Han Sans SC", "Microsoft Yahei";
}

.md-fences, tt, code {
    font-family: Consolas;
}

```

这里其实就是修改了字体为思源黑体、微软雅黑，以及代码字体为 `Consolas`。关于思源字体的介绍，可以参考之前发表的[文章](/2020-12-04/source-hans-font-intro.html)。重新打开Typora，或者切换其它主题再切换回来就可以生效了。最近新装了Windows11， 把常用软件都切换成了深色界面了，Typora也换成了官方的Night主题。

顺便补充一点，字体的英文名可以通过 `Exif` 查看工具（比如 `exif-tool` 命令行工具或者在线工具也行）获取真实的 `font-family`，在windows的字体设置中展示的是中文font-family，实测并不可用。
