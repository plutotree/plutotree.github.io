---
layout: post
title:  "从windows资源管理器中移除左侧边栏图标"
date:   2019-02-01 15:30:00 +0800
categories: windows
typora-root-url: ..
---

windows10资源管理器，左侧有较多无用的图标，尤其对于洁癖者来说更想把这些图标都清理干净。

![1549007376153](/raw/2019-02-01-windows-10-explorer-remove-left-panel-icon/1549007376153.png)

下面先介绍如何移除上面3个图标：`OneDrive`、`Dropbox`和`Creative Cloud Files`，然后再介绍移除“此电脑”里面的图标。

## 移除OneDrive图标

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 进入下述地址（可以直接拷贝到地址栏中）

   ```bash
   HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}
   ```

3. 将右侧的`System.IsPinnedToNameSpaceTree`值设置为0

   ![1549008970481](/raw/2019-02-01-windows-10-explorer-remove-left-panel-icon/1549008970481.png)

4. 打开新的资源管理器看看，OneDrive图标是不是消失了；

如果使用的是64位版本的windows，在运行32位程序的时候，还是能在`保存`对话框里看到OneDrive。

![1549009483968](/raw/2019-02-01-windows-10-explorer-remove-left-panel-icon/1549009483968.png)

可以进入注册表编辑器里面的下述地址：

```bash
HKEY_CLASSES_ROOT\Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}
```

修改右侧的`System.IsPinnedToNameSpaceTree`值为0。重新打开`保存`对话框，可以发现已经没有OneDrive图标了。

如果需要还原的话，将前面操作中的值设置回1即可。

## 移除Dropbox图标

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 进入下述地址

   ```bash
   HKEY_CURRENT_USER\Software\Classes\WOW6432Node\CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}\ShellFolder
   ```

3. 将右侧的`Attributes`值从`f080004d`改为`f090004d`

4. 进入下述地址

   ```bash
   HKEY_CURRENT_USER\Software\Classes\WOW6432Node\CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}\ShellFolder
   ```

5. 将右侧的`Attributes`值从`f080004d`改为`f090004d`
6. 该操作需要[重启`explorer`进程](https://www.winhelponline.com/blog/exit-explorer-restart-windows-10-8/)或者注销后重新登录才能生效，也可以选择重启系统。

## 移除Creative Cloud Files图标

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 按`Ctrl+F`搜索，输入`Creative Cloud Files`，找到`\HKEY_CLASSES_ROOT\CLSID`下面的一项

   ![1549012475286](/raw/2019-02-01-windows-10-explorer-remove-left-panel-icon/1549012475286.png)

3. 将右侧的`System.IsPinnedToNameSpaceTree`值从`1`改为`0`；

4. 该操作需要[重启`explorer`进程](https://www.winhelponline.com/blog/exit-explorer-restart-windows-10-8/)或者注销后重新登录才能生效，也可以选择重启系统。

经过上述3个操作之后，左侧的边栏变得清晰了很多，如果有其他程序图标，也可以参考类似的方法移除

![1549012686611](/raw/2019-02-01-windows-10-explorer-remove-left-panel-icon/1549012686611.png)

## 移除此电脑里面的应用图标

优先确认应用本身是否提供了移除图标的功能，如果确认没提供的话，再考虑手动操作。可以先试试点击右键删除是否生效，下面以删除`微云同步助手`为例

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 进入下述地址

   ```bash
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace
   ```

3. 依次查看这里的项，可以通过右侧的信息来确定是否是`微云同步助手`；

4. 找到后删除该项；

5. 打开新的资源管理器窗口查看是否生效；

## 移除此电脑里面的3D对象

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 进入下述地址

   ```bash
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}
   ```

3. 右键选择该项删除

4. 进入下述地址（如果是32位的windows系统则不需要该操作）

   ```bash
   HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}
   ```

5. 右键选择该项删除；

6. 上述操作应该可以立即生效；

## 快速访问

如果并不需要快速访问展现最近目录和文件的话，可以从配置里面直接关闭

1. 打开文件夹选项

   ![1549018401493](/raw/2019-02-01-remove-sidebar-icon-from-file-explorer-in-windows/1549018401493.png)

2. 在隐私下去除展现最近文件和文件夹的勾选；

   ![1549018096295](/raw/2019-02-01-remove-sidebar-icon-from-file-explorer-in-windows/1549018096295.png)

3. 如果不喜欢默认展现快速访问的话，还可以将默认打开配置为此电脑

   ![1549018130947](/raw/2019-02-01-remove-sidebar-icon-from-file-explorer-in-windows/1549018130947.png)
