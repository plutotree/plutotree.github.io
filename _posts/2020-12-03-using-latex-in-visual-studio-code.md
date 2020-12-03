---
layout: post
title:  "在Visual Studio Code中使用LaTeX"
date:   2020-12-03 18:30:00 +0800
categories: [vscode, latex, tex]

typora-root-url: ..
typora-copy-images-to: ..\raw\2020-12-03-using-latex-in-visual-studio-code
---

## 关于LaTex

[`LaTeX`](https://zh.wikipedia.org/wiki/LaTeX)是一种基于TeX的排版系统，而TeX是[高德纳](https://zh.wikipedia.org/wiki/%E9%AB%98%E5%BE%B7%E7%BA%B3)在发表《计算机程序艺术》的时候，因为当时的排版软件无法达到他的要求，自己编写的（牛人就是这么牛）。`LaTeX`非常适用于生成高质量的科技文章，在学术界用的较多，期刊杂志都会提供`LaTex`的模板，对于工科研究生来说算是必备的技能了。`LaTeX`作为一种标记语言，遵循的一个基本理念就是呈现和内容分离，和现在的markdown有点类似。

下面看看一个示例效果吧

![image-20201203195703950](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203195703950.png)


对应的代码如下（看着也还好对吧？）

```latex
\documentclass{article}
\usepackage[UTF8]{ctex}
\usepackage{amsfonts}
\usepackage{pgfplots}
\pgfplotsset{compat=1.14}

\begin{document}
    \title{在Visual Studio Code中使用LaTeX}
    \author{PlutoTree}
    \maketitle

    来个公式：

    $$ \int x^{\mu}\mathrm{d}x=\frac{x^{\mu +1}}{\mu +1}+C, \left({\mu \neq -1}\right) $$
    
    来个函数图：

    \begin{center}
        \begin{tikzpicture}
            \begin{axis}[xlabel=$x$,ylabel={$f(x)$},legend pos=outer north east,axis lines=left]
                \addplot[color=red,domain=-3:3,samples=100]{exp(-x^2/2)};
                \addplot[color=blue,domain=-3:3,samples=100]{exp(-x^2/3)};
                \addplot[color=orange,domain=-3:3,samples=100]{exp(-x^2/4)};
                \legend{$\exp(-x^2/2)$,$\exp(-x^2/3)$,$\exp(-x^2/4)$}
            \end{axis}
        \end{tikzpicture}
    \end{center}
\end{document}
```

对`LaTeX`感兴趣的话，可以参考相关资料，这里还是先回归正题，有空的话我也会写写`LaTeX`的使用文章。

## 安装TexLive

目前最新的是`TexLive 2020`，可以在[官网](https://www.tug.org/texlive/)下载在线安装包，不过更建议直接下载完整的ios安装包。可以直接点击[链接](http://mirror.ctan.org/systems/texlive/Images/texlive2020.iso)下载，这个地址会自动选择合适的镜像地址。如果发现下载速度很慢，也可以在下述地址中手动选择，或者使用迅雷之类的工具进行下载：

- 清华大学（北京）：https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/texlive2020.iso
- 北京交通大学（北京）：https://mirror.bjtu.edu.cn/ctan/systems/texlive/Images/texlive2020.iso
- 上海交通大学（上海）：https://mirrors.sjtug.sjtu.edu.cn/ctan/systems/texlive/Images/texlive2020.iso
- 中国科技大学（合肥）：https://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2020.iso
- 重庆大学（重庆）：https://mirrors.cqu.edu.cn/CTAN/systems/texlive/Images/texlive2020.iso
- 腾讯云：https://mirrors.cloud.tencent.com/CTAN/systems/texlive/Images/texlive2020.iso

下载完之后可以直接用资源管理器打开可以直接加载（Windows10支持，使用虚拟光驱），或者也可以使用压缩工具打开后直接解压缩。不管使用哪种方式，iso文件或者解压后的文件需要保留，以方便后续安装宏包。

双击运行`install-tl-windows.bat`

![image-20201203205630699](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203205630699.png)

点击`Advanced`，修改默认的安装路径，然后点击安装

![image-20201203205818216](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203205818216.png)

安装包较大，耐心等待

![image-20201203205928065](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203205928065.png)

安装完成之后可以直接打开`TeXworks editor`进行编辑`tex`文件，以及编译生成`pdf`。如果能接受`TeXworks`的丑陋界面，其实可以不用往后看了哈。除了`Visual Studio Code`之外，也可以选择自己喜欢的任意文本编辑器来使用，包括`vim`、`emacs`、`notepad++`，配置好相关的语法提示，以及快捷命令之后也都可以正常使用。

![image-20201203200900391](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203200900391.png)

## 配置Visual Studio Code

`Visual Studio Code`的安装就不介绍了，直接安装插件`LaTeX Workshop`和`LaTeX Utilities`

![image-20201203165405193](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203165405193.png)

安装完成之后点击`LaTex Workshop`插件的配置选项

![image-20201203201257832](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203201257832.png)

搜索`tools`，然后选择在`settings.json`中编辑（这时候会将默认的配置插入）

![image-20201203201359586](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203201359586.png)

在前面加上下述参数，不要忘记末尾的逗号

```json
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-output-directory=%OUTDIR%",
                "%DOCFILE%"
            ],
            "env": {}
        },
```

![image-20201203201816560](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203201816560.png)

回到插件的配置页面，在上面有`Recipes`的配置说明，同样点击在`settings.json`中编辑（这时候会将默认的配置插入），在前面加上下述参数，同样不要忘记末尾的逗号

```json
        {
            "name": "xelatex",
            "tools": [
                "xelatex"
            ]
        },
```

![image-20201203201909440](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203201909440.png)

## 使用说明

打开一个文件夹，新建一个tex文件，把前面那段代码拷贝进去，点击右上方的箭头进行编译，或者使用快捷键`Ctrl+Alt+B`，成功之后可以点击左边的`View Latex PDF`，默认会启动浏览器进行查看。

![image-20201203202813198](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203202813198.png)

这时候也可以直接查看文件所在目录，会发现除了生成的`pdf`文件之外，还有一些其他文件。

![image-20201203203020259](/raw/2020-12-03-using-latex-in-visual-studio-code/image-20201203203020259.png)

## 参考资料

1. [TeX Live 下载及安装说明](https://liam.page/texlive/)
2. [使用VSCode编写LaTeX](https://zhuanlan.zhihu.com/p/38178015)
3. [2020搭建Latex环境](https://zhuanlan.zhihu.com/p/58811994)