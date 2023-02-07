---
layout: post
title: "jekyll自动生成目录的几种方案"
date: 2019-01-30 13:00:00 +0800
tags: [jekyll]
typora-root-url: ..
comments: true
---

jekyll 的`kramdown`不支持`[TOC]`自动生成目录的方式，目前了解来看有几种方案：

1. 在正文中添加如下标签，这个方案优点在于不需要额外配置，github pages 也默认支持，缺点在于格式看着不太优雅，不符合[markdownlint](https://github.com/DavidAnson/markdownlint)规范，在`visual studio code`的 markdownlint 插件下会导致一堆 lint 告警；

   ```markdown
   - TOC
     {:toc}
   ```

2. 使用[`jekyll-toc`插件](https://github.com/toshimaru/jekyll-toc)，这种方式实现比较优雅，也不会破坏 markdown 源文件，缺点在于 github pages 并不支持自定义插件；

   - 在网站的`gemfile`里面添加一行 `gem 'jekyll-toc'`，然后执行`bundle install`
   - 在网站的`_config.yml`里面添加插件：

     ```markdown
     plugins:

     - jekyll-toc
     ```

   - 在你的 markdown 文件里面的头部分加上`toc: true`；

3. 使用[jekyll html](https://github.com/allejo/jekyll-toc)的解决方案，这是目前在 github pages 下推荐的方案；

   - 下载`toc.html`文件，并放到`_includes`目录；
   - 在`_layouts`下用到的`html`里面，在`content`前面加上一行`% include toc.html html=content %`（前后需要加上`{ }`）
