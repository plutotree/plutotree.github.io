---
layout: post
title:  "在jekyll中使用腾讯统计或百度统计"
date:   2019-02-01 15:30:00 +0800
categories: windows
typora-root-url: ..
---

1. 在[腾讯分析](https://ta.qq.com/)申请创建一个项目，得到一段类似代码：

   ```javascript
   <script type="text/javascript" src="http://tajs.qq.com/stats?sId=66171907" charset="UTF-8"></script>
   ```

2. 在`_includes/footer.html`（如果该文件不存在的话，可以从模板里面拷贝出来）最后增加一行，将上面的代码拷贝进去，这时候正常运行就可以得到统计结果了；

[百度统计](https://tongji.baidu.com)的方式也类似，另外如果想要在header引入的话也可以考虑放在`_includes/head.html`。

这时候还存在一点困扰，本地调试的时候也会作为统计上报，为了避免这种情况，我们可以在该段代码前后加上判断条件，这样子在本地调试的时候查看源代码可以发现不会引入该script。

```javascript
{%- if jekyll.environment == 'production' -%}
  <script type="text/javascript" src="http://tajs.qq.com/stats?sId=66171907" charset="UTF-8"></script>
{%- endif -%}
```

如果你调试的时候想临时验证下的话，可以指定环境变量，类似这样子执行：

```bash
JEKYLL_ENV=production bundle exec jekyll serve
```

再进一步，也可以在配置文件里面增加配置项用来配置是否启用腾讯统计或者百度统计。在`_config.yml`增加一行`tencent_analytics: 1`，然后在`_includes/footer.html`里面加个条件：

```javascript
{%- if jekyll.environment == 'production' and site.tencent_analytics == 1 -%}
  <script type="text/javascript" src="http://tajs.qq.com/stats?sId=66171907" charset="UTF-8"></script>
{%- endif -%}
```
