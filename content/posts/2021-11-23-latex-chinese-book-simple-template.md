---
title: latex中文书籍模板
date: 2021-11-22 12:30:00 +0800
tags: [latex]
slug: latex-chinese-book-simple-template
aliases: [/2021-11-22/latex-chinese-book-simple-template.html]
---

使用`ctexbook`的一个最简单的模板

- 标题页无页码；
- 目录页无页码；
- 正文页页码重新计数；
- 设置好字体后可以直接在[overleaf](https://www.overleaf.com/)上面运行；

代码如下：

```latex
\documentclass{ctexbook}

% 设置页边距
\usepackage[margin=3.18cm,a4paper]{geometry}

% 在OverLeaf上可以使用指定字体
% \setmainfont{Caladea}

\pagestyle{headings}

\title{三国演义}
\author{罗贯中}
\date{}

\begin{document}

% 标题页不需要页码
\maketitle
\thispagestyle{empty}

% 目录页不需要页码
\tableofcontents
\thispagestyle{empty}

% 页码重新计数
\setcounter{page}{0}

\chapter{宴桃园豪杰三结义\ 斩黄巾英雄首立功}

\noindent 滚滚长江东逝水，浪花淘尽英雄。\\
是非成败转头空。\\
青山依旧在，几度夕阳红。\\
白发渔樵江渚上，惯看秋月春风。\\
一壶浊酒喜相逢。\\
古今多少事，都付笑谈中。\\
------调寄《临江仙》

话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。汉朝自高祖斩白蛇而起义，一统天下，后来光武中兴，传至献帝，遂分为三国。推其致乱之由，殆始于桓、灵二帝。桓帝禁锢善类，崇信宦官。及桓帝崩，灵帝即位，大将军窦武、太傅陈蕃共相辅佐。时有宦官曹节等弄权，窦武、陈蕃谋诛之，机事不密，反为所害，中涓自此愈横。

\chapter{张翼德怒鞭督邮\ 何国舅谋诛宦竖}

且说董卓字仲颖，陇西临洮人也，官拜河东太守，自来骄傲。当日怠慢了玄德，张飞性发，便欲杀之。

\end{document}

```
