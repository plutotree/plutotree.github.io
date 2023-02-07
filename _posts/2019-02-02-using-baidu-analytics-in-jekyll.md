---
layout: post
title: "在jekyll中使用百度统计"
date: 2019-02-01 15:30:00 +0800
tags: [jekyll]
typora-root-url: ..
comments: true
---

> 腾讯统计已下线，可以查看最后一部分引入百度统计

## 操作步骤

加入腾讯统计的方法非常简单，只需要 2 步就可以了：

1. 在[腾讯分析](https://ta.qq.com/)申请创建一个项目，得到一段类似代码：

   ```javascript
   <script
     type="text/javascript"
     src="http://tajs.qq.com/stats?sId=66171907"
     charset="UTF-8"
   ></script>
   ```

2. 在`_includes/footer.html`（如果该文件不存在的话，可以从模板里面拷贝出来）最后增加一行，将上面的代码拷贝进去，这时候正常运行就可以得到统计结果了；

[百度统计](https://tongji.baidu.com)的方式也类似，如果想要在 header 引入的话可以考虑放在`_includes/head.html`。

这时候本地调试也会上报统计，这种情况如果不想上报的话，需要加上判断条件。这里用了`jekyll.enviroment`变量，该变量在 github pages 发布的时候会设置成`production`，而本地没有设置该变量就不会引入该 script。注意下代码的`%`需要加上对应的`{`和`}`（没有直接加是因为会被 jekyll 自动处理）

```javascript
%- if jekyll.environment == 'production' -%
  <script type="text/javascript" src="http://tajs.qq.com/stats?sId=66171907" charset="UTF-8"></script>
%- endif -%
```

如果你调试的时候想临时验证下的话，可以指定环境变量，类似这样子执行：

```bash
JEKYLL_ENV=production bundle exec jekyll serve
```

再进一步，也可以在配置文件里面增加配置项用来配置是否启用腾讯统计或者百度统计。在`_config.yml`增加一行`tencent_analytics: 1`，然后在`_includes/footer.html`里面的条件换成

```javascript
%- if jekyll.environment == 'production' and site.tencent_analytics == 1 -%
```

## 更新

腾讯分析将于 2020 年 12 月 31 日下线，这里引导的腾讯移动分析也将在 2021 年 3 月份下线，所以只能放弃腾讯分析了。

![image-20201203214147198](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/49ed9a.png)

只能切到[百度统计](https://tongji.baidu.com/sc-web)了，百度统计的 js 看着有点复杂，先直接拷贝吧。

```javascript
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?xxxxxx";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>

```
