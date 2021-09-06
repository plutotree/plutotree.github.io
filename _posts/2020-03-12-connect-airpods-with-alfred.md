---
layout: post
title:  "使用alfred连接AirPods"
date:   2020-03-02 00:10:00 +0800
categories: alfred
typora-root-url: ..
comments: true
---

## 操作步骤

1. 安装蓝牙客户端[BluetoothConnector](https://github.com/lapfelix/BluetoothConnector)：

   ```bash
   brew install bluetoothconnector
   ```

2. 查找airpods的蓝牙地址：按住`option`键，点击顶部蓝牙图标，找到AirPods（前提需要先连接上），右侧会有地址信息（好像不能拷贝，手动记录下吧）

   ![image-20200312014254798](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312014254798.png)

3. 创建alfred工作流：

   - 打开alfred设置页面，选择workflow 选项，点击左侧底部的加号键，选择`Blank Workflow`

     ![image-20200312020649941](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312020649941.png)

   - 选择名称、描述、分类，可以选择导入AirPods的图片（可以下载这个AirPods[大图](https://www.apple.com/v/airpods/j/images/overview/airpods__dh7xkbort402_large_2x.jpg)），选择`Save`保存

     ![image-20200312021125185](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312021125185.png)

   - 在新建的Workflow下方右键选择Inputs - Keywords，输入关键字`airpods`，注意选择`No Argument`，点击`Save`保存

     ![image-20200312021419665](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312021419665.png)

     ![image-20200312021850603](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312021850603.png)

   - 拉动刚创建的触发器的右侧，选择`Actions` - `Run Script`

     ![image-20200312022344161](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312022344161.png)

   - 输入脚本内容 `/usr/local/bin/BluetoothConnector XX-XX-XX-XX-XX --notify`，保存即可。顺便说下，这里用了完整路径，开始是直接指定命令字，但是alfred提示无法找到。应该是PATH环境变量的问题，不过在alfred日志里面并未看到`echo $PATH`的日志输出，有时间的时候再看下问题原因。

     ![image-20200312022854483](/raw/2020-03-12-connect-airpods-with-alfred/image-20200312022854483.png)

4. 触发alred之后，输入airpods即可连接，并会收到系统通知；

5. 如果已连接的状态下，再次输入airpods会触发会触发断开连接，并会收到系统通知；

## 参考资料

- [Easily connect your AirPods to your Mac with Alfred Workflows](https://gary.mcad.am/easily-connect-your-airpods-to-your-mac-with-alfred-workflows-feea1b2fce78)
