# 鼠须管 Squirrel 选项词横排配置调整


最近鼠须管squirrel升级之后选项变成纵向排列了，本地没有改过配置，那应该就是新版本对`style/horizontal`参数不再兼容了，看了下 `Release notes` 果然如此，这里备注下这两个选项配置不同情况下的效果。一般只需要设置 `candidate_list_layout: linear` 即可。

- candidate_list_layout: linear
- text_orientation: vertical

![261fde](https://pic-1251468582.file.myqcloud.com/pic/2024/06/13/261fde.png)

- candidate_list_layout: linear
- text_orientation: horizontal

![1ce68f](https://pic-1251468582.file.myqcloud.com/pic/2024/06/13/1ce68f.png)

- candidate_list_layout: stacked
- text_orientation: horizontal

![d459fa](https://pic-1251468582.file.myqcloud.com/pic/2024/06/13/d459fa.png)

- candidate_list_layout: stacked
- text_orientation: vertical

![f74978](https://pic-1251468582.file.myqcloud.com/pic/2024/06/13/f74978.png)

