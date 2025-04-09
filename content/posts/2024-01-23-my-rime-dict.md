---
title: 我的RIME词库说明
date: 2024-01-23 18:00:00 +0800
tags: [rime]
slug: my-rime-dict
aliases: [/2024-01-23/my-rime-dict.html]
---

最开始用的基础词库来源于[ssnhd/rime](https://github.com/ssnhd/rime)，这是它的词表介绍

![img](https://pic-1251468582.file.myqcloud.com/pic/2024/01/23/63c9cf)

主要用了这几份词库：

- `luna_pinyin.dict.yaml`：默认字库，有部分的词语，总计7万；
- `luna_pinyin.sogou.dict.yaml`：来源于搜狗词库，总计105万；
- `easy_en.dict.yaml`：英文词库，总计11万；

此外还用了几份自己维护的词库：

- 股票名称列表，使用[Tushare](https://tushare.pro/) API拉取A股的股票名称列表生成词库，总计5千；
- 我的搜狗自定义词库，从搜狗导出后经过手动删除，总计3千；
- 我手动维护的词库，总计1百；

但是这份词库存在几个问题：

1. 缺乏词库持续的更新维护；
2. 这份百万级的搜狗词库质量不高，并不是搜狗自带的词库；
3. 本身基于繁体，尽管这符合RIME的做法；

最近发现两份还不错的简体词库，分别是[四叶草拼音](https://github.com/fkxxyz/rime-cloverpinyin)和[雾凇拼音](https://github.com/iDvel/rime-ice)。其中雾凇拼音有6K的star数量，并且更新还是比较及时的，提供的功能也比较完善，下面是一个功能介绍：

![demo](https://pic-1251468582.file.myqcloud.com/pic/2024/01/23/92f3d3.webp)

作者也明确说明了他会长期维护几份词库：

- `8105` 字表。
- `base` 基础词库。
- `ext` 扩展词库，小词库。
- `tencent` 扩展词库，大词库。
- Emoji

雾凇拼音用了大量的`lua`脚本来实现功能，这里先不整体引用，打算只引用词库。但是在部署的时候却发现小狼毫会一直处于加载中，尝试后发现是在加载Tencent大词库的时候才出问题。搜索[Github](https://github.com/rime/weasel/issues/953)发现可以关掉配置`use_preset_vocabulary`就可以解决问题。

目前使用的外部词库保留了来源于雾凇拼音的四份中文词库

- `cn_dicts/8105`     # 字表
- `cn_dicts/base`     # 基础词库
- `cn_dicts/ext`      # 扩展词库
- `cn_dicts/tencent`  # 腾讯词向量
