# 在github pages上使用jekyll


网上有大量文章说明如何在 github pages 上面使用 jekyll，这里仅说明下大致流程

- 导出 git
- 本地编辑 markdown
- 本地启动 jekyll，验证文章效果
- git 提交
- 网页生效

1. 选择合适的 jekyll 模版，也可以直接使用我的网站（记得删除\_posts 和 raw 目录）

   ```bash
   git clone "https://github.com/plutotree/plutotree.github.io.git"
   cd plutotree.github.io.git
   ```

2. 安装必要的依赖，以及启动 jekyll

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

- 为什么使用 ruby 2.7

  参考[GitHub Pages 依赖的版本信息](https://pages.github.com/versions/)，ruby 支持的版本为 2.7.3

