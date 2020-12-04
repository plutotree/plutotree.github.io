---
layout: post
title:  "思源字体介绍"
date:   2020-12-04 18:30:00 +0800
categories: [思源宋体, 思源黑体, 字体]
typora-root-url: ..
typora-copy-images-to: ..\raw\2020-12-04-source-hans-font-intro
---

思源字体是Adobe和Google联合开发的开源字体，以Apache 2.0授权，可以免费商用。每套字体提供了7个尺寸，并且为中日韩，更具体的说大陆、香港、台湾、韩国、日本都进行了针对化的设计。

![image-20201204191346712](/raw/2020-12-04-source-hans-font-intro/image-20201204191346712.png)

[Adobe](https://github.com/adobe-fonts)和[Google](https://www.google.com/get/noto/help/cjk/)采用了不同的命名方式，这里我更喜欢Adobe的命名方式。这里的安装方式比较复杂，有多种字体格式：OTF、OTC、Super OTC和Subset OTF，还要区分多个区域，可以参考github上的[文档](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)。这里我直接用了Super OTC反正是最全的。

| 字体中文名 | adobe字体英文名  | google字体英文名   |
| ---------- | ---------------- | ------------------ |
| 思源宋体   | Source Han Serif | Noto Serif CJK     |
| 思源黑体   | Source Han Sans  | Noto Sans CJK      |
| 思源等宽   | Source Han Mono  | Noto Sans Mono CJK |

在使用字体的时候需要注意的是引用的字体名是**Source Han Sans SC**（**SC**为简体中文缩写，对应大陆常见写法）。 如果使用的是**Source Han Sans**，那会使用日文的字体，包含的文字可能不全，另外部分子写法和我们正常的写法也会不一致。

- **SC**：Simplified Chinese (China)
- **TC**：Traditional Chinese (Taiwan)
- **HC**：Traditional Chinese (Hong Kong)
- **无**：Japan
- **K**=Korean

