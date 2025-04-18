---
title: Markdown 语法详解
date: 2019-01-29 12:03:00 +0800
tags: [markdown]
categories: [markdown]
slug: markdown-intro
aliases: [/2019-01-29/markdown-intro.html]
---

## Markdown 简介

**Markdown**是一种轻量级标记语言，旨在通过易读易写的纯文本格式来编辑文档，并可转换生成格式化的文档。

Markdown 最早由 John Gruber 于 2004 年创立。2014 年发布的 CommonMark 是第一套严谨的规范。2017 年，GitHub 发布了基于 CommonMark 的 GitHub Flavored Markdown（GFM）的正式规范。

尽管基础的 Markdown 语法简单直观，但不同解析器在实现上多少还是存在差异，特别是对于扩展的 Markdown 语法的支持上。

- [GFM](https://github.github.com/gfm/)：目前最流行的 Mermaidarkdown 扩展规范了；
- [Typora](https://typora.io/)：个人认为最好的 Markdown 编辑器和查看器，支持`windows`和`mac`，在 GFM 基础上，它还支持很多额外的扩展语法；
- [kramdown](https://kramdown.gettalong.org/index.html)：作为`jekyll`的默认 Markdown 解析器，现在也是 github pages 默认的 markdown 解析器；
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint): VSCode 的 Markdown Lint 插件，可以检查语法是否规范；
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced): VSCode 的 Markdown 查看插件，近 700 万的下载次数就能说明其受欢迎程度了；

本文打算以 GFM 和 Typora 为主，来介绍 Markdown 的基础和扩展语法格式规范，以及不同语法在不同解析器下的支持情况，另外还会增加一些[markdownlint](https://github.com/DavidAnson/markdownlint)的规范描述。

## 基础语法

### 标题

使用`#`指定标题，1-6 个`#`，分别对应 1-6 级标题。顾名思义，`#`数目越少，标题级别就越高。按照语法规范，建议`#`和标题名之间保留一个空格，标题行的前后需要保留一行空行。

```markdown
# 一级标题

## 二级标题

### 三级标题

###### 六级标题
```

在生成`html`时，会对应到`<h1>`、`<h2>`、`<h3>`和`<h6>`

```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h6>六级标题</h6>
```

### 正文段落

普通文本直接输入就好，但是文本中的换行是不生效的，即使在编辑器中能看到有换行效果，但是导出生成HTML仍然是不生效的。如果要实现换行的话，需要在行尾加上两个空格。直接用`<br/>`的html标签的话，也是能实现换行，不过这就不算是markdown语法了。

如果中间有一行空行的话，则会产生是一个新的段落。换行对应到 html 的`<br/>`，段落对应到 html`<p> </p>`。

对于下述的Markdown 文本：

```markdown
这是第一段的第一行（结尾加两个空格）  
这是第二行

这是第二段的第一行（结尾没有空格）
这仍然是第二段的第一行
```

使用Typora生成的HTML如下：

```html
<p>
   <span>这是第一段的第一行（结尾加两个空格）</span>
   <br/>
   <span>这是第二行</span>
</p>
<p>
   <span>这是第二段的第一行（结尾没有空格）</span>
   <span>这仍然是第二段的第一行</span>
</p>
```

对于行首和行尾的单个空格常见的渲染处理是会被直接忽略。段落之间多行空行也没有意义，保留一行空行即可。

### 字体样式

| 字体样式                | 语法                  | 例子             | html                         |
| ----------------------- | --------------------- | ---------------- | ---------------------------- |
| 粗体(Bold)              | `** **` 或`__ __`     | **这是粗体**     | `<strong></strong>`          |
| 斜体(Italic)            | `* *` 或`_ _`         | _这是斜体_       | `<em></em>`                  |
| 粗斜体(Bold and Italic) | `*** ***` 或`___ ___` | **_这是粗斜体_** | `<strong><em></em></strong>` |
| 删除线(Strikethrough)   | `~~ ~~`               | ~~这是删除线~~   | `<del></del>`                |

删除线不属于标准的 markdown 规范，但是一般的解析器都会支持。至于使用\*还是使用\_则看个人习惯，使用\*的人更多一些。

### 引用

使用`>`即可进行引用，对应 html 的`<blockquote></blockquote>`，如果引用需要分多段的的话，可以在中间加一个仅包含`>`的一行即可。如果中间是一个空行的情况，大部分解析器会将其认为是 2 个引用块，也有部分会将其认为是 1 个引用块，使用中最好尽量避免中间有空行的情况出现。

李白曾经写过

> 君不见，黄河之水天上来，奔流到海不复回。君不见，高堂明镜悲白发，朝如青丝暮成雪。
>
> 人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。

### 列表

使用`*`、`-`或`+`产生无序列表，使用数字加`.`产生有序列表，有序列表的数字不一定需要有序，但是需要从 1 开始，也可以所有都是 1。

无序列表：

- Java
- C/C++
- Python

有序列表：

1. Java
2. C/C++
3. Python
4. Go
5. PHP

无序列表产生的 html 如下`<ul><li></li><li></li></ul>`，有序列表产生的 html 如下`<ol><li></li><li></li></ol>`

对于多级列表，需要确保子列表与上一级列表的内容对齐，对于有序列表的二级列表缩进 3 个空格（数字+`.`+空格），对于无序列表的二级列表缩进 2 个空格（`-`+空格）。对于 list 内部包含段落、引用、代码块、表格等情况，建议和上述规则保持一致。对于上述情况在二级列表或者段落前后包含一个空行。

不同的 markdown 解析器对于列表内包含段落的情况处理的并不一致，所以存在着各种写法，比如段落前用 4 个空格、在上一行末尾加入 2 个空格（软换行）等等，建议保持标准的写法兼容尽量多的解析器。

```markdown
1. Java

   Java 连续霸榜 TIBOE 编程语言排行榜，已然成为业界最受欢迎的变成语言。

2. C/C++

   - C
   - C++

3. Python
4. PHP

   > 曾经有人说 PHP 是世界上最好的语言

   LAMP 曾经是标配，如今已经不再那么流行……
```

1. Java

   Java 连续霸榜 TIBOE 编程语言排行榜，已然成为业界最受欢迎的变成语言。

2. C/C++

   - C
   - C++

3. Python
4. PHP

   > 曾经有人说 PHP 是世界上最好的语言

   LAMP 曾经是标配，如今已经不再那么流行……

### 链接

链接写法 `[展现名](链接地址 "标题")`，比如[腾讯网](https://www.qq.com)，其中的`"标题"`可以省略，链接地址可以使用绝对路径也可以使用相对路径，或者指向本地/本网站的其他文件。更进一步，也可以指向本文件的其他锚点（书签），比如[跳转引用](#引用)。

展现的名字和链接地址一致的时候会显得有些冗余，比如`[https://www.qq.com](https://www.qq.com)`，有更简洁的写法，直接用`<https://www.qq.com>`生成<https://www.qq.com>。

如果多处需要链接相同的地址，我们也可以采用引用的方式，使用`[展现名][链接名]`，然后在任意地方定义链接名的具体地址 `[链接名]: 链接地址`，比如[腾讯][qq]，这样子还有个好处是方便管理。

[qq]: https://www.qq.com "腾讯网"

### 图片

和链接的语法类似，图片需要在前面加上`!`，常见的写法`![展现名][图片地址]`，如果需要图片本身也是链接的话，在外层加上链接地址：`[![展现名][图片地址]](链接地址)`

[![腾讯网图片](https://mat1.gtimg.com/pingjs/ext2020/qqindex2018/dist/img/qq_logo_2x.png)](https://www.qq.com)

### 表格

表格不是标准的 markdown，但是常见的解析器会支持，写法如下，完整的情况会在第一列前面和最后列后面加上`|`，表头和内容中间需要一行分隔符，这里建议保持和列数一致，某些解析器也会支持最简单的写法`---|---`（不管多少列的情况下），但是很多解析器并不支持，这里可以通过`:`来指定表格的对齐方向，左对齐、右对齐还是居中。

```html
表头1|表头2|表头3 :---|:---:|---: 内容|内容|内容 内容|内容|内容
```

| 国家   |      面积       |   人口 |
| :----- | :-------------: | -----: |
| 中国   | 960 万平方公里  |  14 亿 |
| 美国   | 936 万平方公里  |   3 亿 |
| 俄罗斯 | 1709 万平方公里 | 1.4 亿 |

### 分隔符

使用`---`或者`***`作为分隔符

---

### 转义字符

由于一些符号在 markdown 中有了特殊含义，比如我们就是要输入`*abc*`，并不希望出现斜体的 abc，那么可以使用`\`作为转衣符，输入`\*abc\*`，结果为\*abc\*。

## 扩展语法

### 代码

行内使用\`作为起始和终止符，比如`printf`，代码块使用位于独立行的```作为起始和终止

```cpp
int main(int argc, char *argv[])
    cout << "hello world!" << endl;
    return 0;
}
```

### 任务列表

任务列表（Task List）在 github 中使用非常广泛，语法格式如下，使用`x`标识为已完成，未完成的情况中间需要包含空格。

```markdown
- [x] 银行存款超过 1000 万
- [ ] 当上总经理
- [ ] 赢取白富美
```

- [x] 银行存款超过 1000 万
- [ ] 当上总经理
- [ ] 赢取白富美

### 数学公式

数学公式块，使用位于独立行的`$$`作为起始和终止，比如：

```markdown
$$
f(x)=\sum^{\infty}_{n=0}\frac{f^{(n)}(a)}{n!}(x-a)^n
$$
```

$$
f(x)=\sum^{\infty}_{n=0}\frac{f^{(n)}(a)}{n!}(x-a)^n
$$

行内数学公式，直接使用`$`作为起始和终止：$\delta=b^2-4ac$（有些解析器需要使用`$$`作为起始和终止）。

### html 标签

可以使用 html 标签实现 markdown 不支持的功能，正常情况下尽量避免使用 html 标签。

1. 在表格内部需要换行的时候，可以加上`<br/>`标签；
2. 需要指定样式的时候，可以加上类似`<span style="color:red"> </span>`标签，比如：<span style="color:red">我是红色</span>；
3. 指定下划线，使用`<u> </u>`，比如：<u>我是下划线</u>；

### 非通用语法

### 内容目录

使用`[TOC]`生成自动目录。Typora 支持该语法，GFM 不支持该语法。

### 时序图

使用[js-sequence](https://bramp.github.io/js-sequence-diagrams/)渲染

{{< highlight markdown >}}

```sequence
罗密欧->朱丽叶: 哈喽
朱丽叶-->罗密欧: 我想你了
罗密欧->>朱丽叶: 我也想你了
```

{{< /highlight >}}

![image-20201204112218341](https://pic-1251468582.file.myqcloud.com/pic/2021/11/04/bcb72a.png)

gfm 不支持时序图，Typora 支持。

### 流程图

使用[flowchart.js](http://flowchart.js.org/)渲染

{{< highlight markdown >}}

```flow
st=>start: 开始
cond=>condition: 有房有车
op1=>operation: 赢取白富美
op2=>operation: 走向人生巅峰
e=>end: 结束

st->cond
cond(yes)->op1->op2->e
cond(no)->e
```

{{< /highlight >}}

![image-20201204112431026](https://pic-1251468582.file.myqcloud.com/pic/2021/11/04/850c41.png)

gfm 不支持流程图，Typora 支持。

### mermaid 图

[`mermaid`](https://mermaidjs.github.io/)相比时序图和流程图来说，功能会更强大，支持时序图、流程图、UML 图、状态图、甘特图等，Typora 支持但是 GFM 不支持。目前来看，使用算是比较广泛了。官网提供了较丰富的例子，[Mermaid Live Editor](https://mermaidjs.github.io/mermaid-live-editor/)提供了在线编辑以及导出 SVG。

看下用`mermaid`来画时序图的例子：

{{< highlight markdown >}}

```mermaid
sequenceDiagram
罗密欧->>朱丽叶: 哈喽
朱丽叶-->>罗密欧: 我想你了
罗密欧->>朱丽叶: 我也想你了
```

{{< /highlight >}}

![image-20201204112846477](https://pic-1251468582.file.myqcloud.com/pic/2021/11/04/cc62aa.png)

### 脚标和上下标

可以使用语法 ​`[^脚标A]: 这是脚标A`来创建角标（需要使用代码块模式），在需要引用的地方使用`[^脚标A]`进行引用[^脚标a]。Typora 支持该语法，GFM 不支持该语法。

[^脚标a]: 这是脚标 A

上标和下标没有一致的标准，在 Typora 中使用`^文字^`表示上标，使用`~文字~`表示下标，但我看并没有得到广泛支持。建议在 markdown 中尽量避免使用上下标，如果要保持兼容性的话采用 HTML 的`<sup>文字</sup>`展示上标，使用`<sub>文字</sub>`的方式展示下标。

### YAML 头信息

在文件的头部使用使用独立行的`---`作为开始和终止，其中间部分会作为 metadata，并不会生成可视内容，这本来是[jekyll](https://jekyllrb.com/docs/front-matter/)的特殊格式，现在 Typora 也支持该语法（尽管不一定会生成 html 里面的 metadata）。

### Github emoji

按文本形式输入类似`:smile:`，常见的可以直接输入，完整的可以参考[列表](https://gist.github.com/rxaviers/7360908)。Typora 和 github 都支持，vscode 的相关插件不支持。

- 人：:boy::girl::man::woman::baby::older_woman::older_man::princess::cop::angel::couple::walking::runner::dancers:
- 动物：:cat::dog::pig::frog::cow::horse::snake::bird::mouse::wolf::monkey::camel:
- 表情：:smile::cry::confused::sob::joy::mask::worried::wink::relaxed::grin::kissing::open_mouth::heart_eyes:

## 参考资料

1. [Writing on GitHub/Basic writing and formatting syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
2. [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
3. [Markdown Guide](https://www.markdownguide.org/)
4. [Markdown Tutorial](https://commonmark.org/help/)
