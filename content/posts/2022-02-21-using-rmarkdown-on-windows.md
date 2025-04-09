---
title: Windows 下 R mardown 入门实战
date: 2022-02-20 19:30:00 +0800
tags: [rmarkdown]
slug: using-rmarkdown-on-windows
aliases: [/2022-02-20/using-rmarkdown-on-windows.html]
---

## R 基础实战

- 安装比较简单，从[官网](https://cran.r-project.org/)下载后执行，可以只选择 x64；

- 使用`R Gui`执行 R 命令：

  - 运行`R Gui`

  - 尝试执行命令：

    ```R
    print('hello world!')

    sqrt(2)
    [1] 1.414214
    > plot(1:10,sqrt(1:10))
    ```

  - 看下执行效果：

    ![image-20220221205209820](https://pic-1251468582.picsh.myqcloud.com/pic/2022/02/22/5233f3.png)

- 使用命令行执行：

  - 设置环境变量，将`C:\Program Files\R\R-4.1.2\bin\x64`添加到`PATH`中；
  - 命令行指定语句
    - 执行`rscript.exe -e "sqrt(1:10)"`，可以看到命令行能直接输出
    - 执行`rscript.exe -e "plot(1:10,sqrt(1:10))"`，这时候看不到窗口输出，在当面目录会生成`Rplots.pdf`文件；
  - 执行文件
    - 执行`rscript.exe -f "demo.r"`

- 使用命令行执行指定文件：

  - 使用任意编辑器创建文件`demo.r`，里面内容如下

    ```R
    print("hello world!")
    sqrt(1:10)
    ```

  - 执行`rscript.exe "demo.r"`

## R markdown 实战

### 安装 Rmarkdown

启动`R gui`，然后执行语句`install.packages("rmarkdown")`，执行之后会让选择下载节点；

### 编写 Rmarkdown 文件

使用任意编辑器创建文件`demo.rmd`，里面内容如下，其实就是 markdown 文件内嵌了 r 语句，这也是 R markdown 的由来

````markdown
---
title: "Rmarkdown demo"
output: html_document
---

## 绘图示例

### 函数曲线图

```{r}
curve(sin(x), 0, 2*pi)
```

### 条形图

```{r}
barplot(c("男生"=48,"女生"=38), main="男女生人数")
```

### 散点图

```{r}
plot(1:100, sqrt(1:100))
```

## 汇总统计

```{r}
data <- read.csv("taxsamp.csv")
knitr::kable(table(data[['征收方式']]))
knitr::kable((table(data[['征收方式']], data[['申报渠道']])))
summary(data[['营业额']])
```
````

### 编译 Rmarkdown 文件

在命令行下执行语句：`Rscript.exe -e "library('rmarkdown');render('demo.rmd')"`，可以看到有一段编译过程，中间生成了 demo.knit.md，最后生成了 demo.html

![image-20220222210347215](https://pic-1251468582.picsh.myqcloud.com/pic/2022/02/22/7d0352.png)

### 查看 html 文件

查看生成的`demo.html`，效果如下：

![image-20220222210531697](https://pic-1251468582.picsh.myqcloud.com/pic/2022/02/22/503338.png)

## 推荐教程

- [R 语言教程 by 李东风](https://www.math.pku.edu.cn/teachers/lidf/docs/Rbook/html/_Rbook/index.html)
- [庄闪闪的 R 语言手册](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NjUwMjQxMQ==&action=getalbum&album_id=1684900703049138178&scene=173&from_msgid=2247491318&from_itemidx=1&count=3&nolastread=1#wechat_redirect)
- [bookdown: Authoring Books and Technical Documents with R Markdown](https://bookdown.org/yihui/bookdown/about-the-author.html)
