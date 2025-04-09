---
title: 小狼毫100%模仿微软输入法的皮肤
date: 2023-02-07 17:30:00 +0800
tags: [rime, 小狼毫]
slug: simulate-microsoft-input-method-skin-in-rime
aliases: [/2023-02-07/simulate-microsoft-input-method-skin-in-rime.html]
---

对于输入法来说，皮肤可以说是非常重要，我们设置一款感觉舒适的，对于打字体验来说能提升不少。毕竟大家不是设计师，我们可以自己盗取成熟的输入法的皮肤效果就好了。这里我们参考的是微软拼音输入法，毕竟作为 windows 系统自带的，微软的设计师水准还是值得信赖的。

## 效果对比

先看下效果，这个是 Windows 系统自带的微软拼音输入法

![image-20230207152007275](https://pic-1251468582.picsh.myqcloud.com/pic/2023/02/07/210a5e.png)

这个是小狼毫模拟的效果，应该做到了 99%的相似度吧。

![image-20230207160021058](https://pic-1251468582.picsh.myqcloud.com/pic/2023/02/07/5d9de1.png)

## 皮肤颜色设置

[官网](https://github.com/rime/home/wiki/CustomizationGuide#%E4%B8%80%E4%BE%8B%E5%AE%9A%E8%A3%BD%E5%B0%8F%E7%8B%BC%E6%AF%AB%E9%85%8D%E8%89%B2%E6%96%B9%E6%A1%88)给了比较清晰的颜色样式配置说明，另外也提供了一个方便的[在线工具](https://bennyyip.github.io/Rime-See-Me/)用来生成配置。我们用取色工具获取微软拼音输入法的相关颜色填充即可（可以用系统自带的画图工具）。

![img](https://pic-1251468582.picsh.myqcloud.com/pic/2023/02/07/f711c9)

![image-20230207160813197](https://pic-1251468582.picsh.myqcloud.com/pic/2023/02/07/aa4b39.png)

在配置文件`weasel.custom.yaml`里面将相关内容填写进入即可。

## 样式设置

这块可能稍微复杂一些，这里不做具体介绍了。结合皮肤设置的内容，在`weasel.custom.yaml`的内容现在是这样：

```yaml
patch:
  preset_color_schemes:
    microsoft_sim:
      name: 仿微软输入法
      author: plutotree
      back_color: 0xF4F4F4
      border_color: 0xDCDCDC
      text_color: 0x000000
      hilited_text_color: 0xF4F4F4
      hilited_back_color: 0xFFD8A6
      hilited_candidate_text_color: 0x000000
      hilited_candidate_back_color: 0xFFD8A6
      candidate_text_color: 0x000000
      comment_text_color: 0x888888

  style:
    color_scheme: microsoft_sim
    label_format: "%s"
    font_face: "微软雅黑"
    font_point: 14
    horizontal: true
    inline_preedit: true
    layout:
      min_width: 160
      min_height: 0
      border_width: 1
      border_height: 1
      margin_x: 12
      margin_y: 12
      spacing: 10
      candidate_spacing: 24
      hilite_spacing: 8
      hilite_padding: 12
      round_corner: 0
```

此外，候选词的个数设置是在文件`default.custom.yaml`，如果有需要修改成和微软拼音输入法一样的 7 个，可以这样填写。

```yaml
patch:
  menu:
    page_size: 7
```

需要注意的一点是`patch`字段内容要和原来的合并，不能新增一个`patch`字段。
