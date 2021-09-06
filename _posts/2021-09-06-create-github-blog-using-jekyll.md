---
layout: post
title:  "在github pages上使用jekyll"
date:   2021-09-06 15:30:00 +0800
categories: [jekyll]
typora-root-url: ..
comments: true
---

网上有大量文章说明如何在github pages上面使用jekyll，这里仅说明下大致流程

- 导出git
- 本地编辑markdown
- 本地启动jekyll，验证文章效果
- git提交
- 网页生效

1. 选择合适的jekyll模版，也可以直接使用我的网站（记得删除_posts和raw目录）

   ```bash
   git clone "https://github.com/plutotree/plutotree.github.io.git"
   cd plutotree.github.io.git
   ```

2. 安装必要的依赖，以及启动jekyll 

    ```bash
    # 安装ruby，不使用自带的版本
    brew install ruby@2.7
    export PATH="/opt/homebrew/opt/ruby@2.7/bin:$PATH" >> ~/.zshrc
    source ~/.zshrc

    # 适用bundler做gem包管理
    gem install bundler
    bundle install

    # 启动jekyll
    bundle exec jekyll serve
    ```

- 为什么使用ruby 2.7

  参考[GitHub Pages依赖的版本信息](https://pages.github.com/versions/)，ruby支持的版本为2.7.3
