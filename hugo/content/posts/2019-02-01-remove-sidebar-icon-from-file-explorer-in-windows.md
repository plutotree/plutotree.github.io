---
title: "从windows资源管理器中移除左侧边栏图标"
date: 2019-02-01 15:30:00 +0800
tags: [windows]
comments: true
---

windows10 资源管理器，左侧有较多无用的图标，尤其对于洁癖者来说更想把这些图标都清理干净。

![1549007376153](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/0b0d31.png)

下面先介绍如何移除上面 3 个图标：`OneDrive`、`Dropbox`和`Creative Cloud Files`，然后再介绍移除“此电脑”里面的图标。

## 移除 OneDrive 图标

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 进入下述地址（可以直接拷贝到地址栏中）

   ```bash
   HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}
   ```

3. 将右侧的`System.IsPinnedToNameSpaceTree`值设置为 0

   ![1549008970481](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/a30ad4.png)

4. 打开新的资源管理器看看，OneDrive 图标是不是消失了；

如果使用的是 64 位版本的 windows，在运行 32 位程序的时候，还是能在`保存`对话框里看到 OneDrive。

![1549009483968](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/83d49e.png)

可以进入注册表编辑器里面的下述地址：

```bash
HKEY_CLASSES_ROOT\Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}
```

修改右侧的`System.IsPinnedToNameSpaceTree`值为 0。重新打开`保存`对话框，可以发现已经没有 OneDrive 图标了。

如果需要还原的话，将前面操作中的值设置回 1 即可。

## 移除 Dropbox 图标

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

## 移除 Creative Cloud Files 图标

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 按`Ctrl+F`搜索，输入`Creative Cloud Files`，找到`\HKEY_CLASSES_ROOT\CLSID`下面的一项

   ![1549012475286](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/f0e4e3.png)

3. 将右侧的`System.IsPinnedToNameSpaceTree`值从`1`改为`0`；

4. 该操作需要[重启`explorer`进程](https://www.winhelponline.com/blog/exit-explorer-restart-windows-10-8/)或者注销后重新登录才能生效，也可以选择重启系统。

经过上述 3 个操作之后，左侧的边栏变得清晰了很多，如果有其他程序图标，也可以参考类似的方法移除

![1549012686611](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/9f3e82.png)

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

## 移除此电脑里面的 3D 对象

1. 按`Win+R`，输入`regedit`，打开注册表编辑器；

2. 进入下述地址

   ```bash
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}
   ```

3. 右键选择该项删除

4. 进入下述地址（如果是 32 位的 windows 系统则不需要该操作）

   ```bash
   HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}
   ```

5. 右键选择该项删除；

6. 上述操作应该可以立即生效；

## 快速访问

如果并不需要快速访问展现最近目录和文件的话，可以从配置里面直接关闭

1. 打开文件夹选项

   ![1549018401493](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/0a99da.png)

2. 在隐私下去除展现最近文件和文件夹的勾选；

   ![1549018096295](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/b3ea05.png)

3. 如果不喜欢默认展现快速访问的话，还可以将默认打开配置为此电脑

   ![1549018130947](https://pic-1251468582.picsh.myqcloud.com/pic/2021/11/04/210175.png)
