---
layout: post
title:  "在jekyll中使用valine评论系统"
date:   2021-09-06 17:30:00 +0800
categories: [jekyll, 评论系统, valine]
typora-root-url: ..
comments: true
---

博客怎么能少了评论系统，但是一直没有找到满意的，各种国内被禁的，缺乏更新维护的，做得太复杂的等等之类的。今天看到一个感觉还不错的评论系统[Valine](https://valine.js.org/)，一款快速、简洁且高效的无后端评论系统，存储基于leancloud。作者的[博客](https://github.com/staticblog/staticblog.github.io)提供了一个jekyll的示例，直接引入。

先参考[这里](https://valine.js.org/quickstart.html#%E8%8E%B7%E5%8F%96APP-ID-%E5%92%8C-APP-Key)的说明，注册Leancloud并创建新的应用，顺便提一下，现在监管严格，需要进行实名注册，最后还要支付宝扫描验证。

接着直接修改jekyll的内容即可（下面的内容照抄作者博客，也可以按自己习惯定义变量）

1. 修改`default.html`，在footer.html前面增加下面这段内容

   ```html
   {% if site.data.social.valine_comment.enable and page.comments == true %}
   <div id="comments"></div>
   {% endif %}
   {% include scripts.html %}
   ```

2. 修改`_includes/head.html`，在合适的地方增加下面这段内容

   ```html
   <!-- Valine Comment -->
   {% if site.data.social.valine_comment.enable and page.comments == true %}
   <script src="//cdn1.lncld.net/static/js/3.0.4/av-min.js"></script>
   <script src="//unpkg.com/valine/dist/Valine.min.js"></script>
   {% endif %}
   ```

3. 在`_includes`下面增加新文件`valine_comments.html`

   ```html
   <script>
       new Valine({
           av: AV,
           el: '#comments',
           app_id: '{{ site.data.social.valine_comment.leancloud_appid }}',
           app_key: '{{ site.data.social.valine_comment.leancloud_appkey }}',
           placeholder: '{{ site.data.social.valine_comment.placeholder }}'
       });
   </script>
   ```

4. 在`_includes`下面增加新文件`scripts.html`

   ```html
   {% if page.comments %}{% include valine_comments.html %}{% endif %}
   ```

5. 在`_data`下面增加新文件`social.yml`

   ```yaml
   valine_comment:
     enable: true
     leancloud_appid: 你的Leancloud Appid
     leancloud_appkey: 你的Leancloud appkey
     placeholder: just go go
   ```

6. 在你的文章头增加`comments: true`

另外还看到一个基于valine的评论系统，叫做[waline](https://github.com/walinejs/waline)，功能很齐全，有空可以再研究下。
