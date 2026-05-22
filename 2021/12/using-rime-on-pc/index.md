# 使用RIME输入法


## 为啥需要更换输入法？

互联网上的隐私泄漏问题一直是讨论的热点，比如姓名、电话、职业、学校等，更进一步还有家庭住址、家庭成员等。那么有没有想过，这么多互联网产品中，拥有你最多隐私的数据产品是什么？很多人会选择微信、微博、抖音等产品，因为它们有我们的关系链、兴趣爱好、LBS 信息、作息习惯等等。这些都没有问题，但是有没有想过我们常用的输入法所拥有的信息甚至比这些产品还要多。而目前大部分输入法都会将输入词传输到云端进行联想提示。想象下，如果将你这么多年的输入词完整分析一遍，能得到多少你个人信息，以及社交信息，甚至分析你的个人性格都不是啥问题。

## 选择一款开源的输入法

[RIME](https://rime.im/)算是最好、最强大的开源输入法，甚至没有之一。它在一个统一的后端服务基础上，利用不同的前端来支持 Windows、MacOS、Android、Linux，实现跨操作系统和跨设备。在 Windows 下叫“小狼毫” (Weasel)，在 Mac 下是“鼠须管” (Squirrel)，在 Linux 下叫“中州韵” (ibus)。此外还有 Android 版本。这里只介绍 windows 和 mac 上的安装和使用方式，而 iOS 上输入法如果不打开联网权限安全和隐私保护是可靠的。

## 安装及基础使用

### Windows 下小狼毫的安装

1. 在官网下载[小狼毫](https://rime.im/download/)；

2. 安裝完成需要选择输入方案，可以只保留朙月输入法，在皮肤选择中可以选择自己喜欢的样式

   ![image-20230206181740122](https://pic-1251468582.file.myqcloud.com/pic/2023/02/06/742201.png)

3. 这时候可以正常输入，但是展示的是繁体字，按 F4 选择简体；

   ![image-20230206182144701](https://pic-1251468582.file.myqcloud.com/pic/2023/02/06/7edf8d.png)

4. 默认的是纵向选择候选词，可能不符合一般的使用习惯，可以打开目录`%APPDATA%\Rime`中下的文件`weasel.custom.yaml`（如果不存在的话则新建即可），增加下述内容：

   ```yaml
   patch:
     style:
       horizontal: true
   ```

5. 在菜单中选择“重新部署”后，就可以看到效果了；

### Mac 下鼠须管的安装

1. 安装 RIME，安装过程需要输入密码

   ```bash
   brew install squirrel --cask
   ```

2. 添加输入法，在输入法管理中添加“鼠须管”输入法

   ![image-20211215143151253](https://pic-1251468582.file.myqcloud.com/pic/2021/12/15/ca0e5b.png)

3. 这时候就可以正常输入了，不过出来的是繁体字，需要调整为简体字。在输入状态下，按 F4 可以选择切换为简体。

   ![image-20211215143850106](https://pic-1251468582.file.myqcloud.com/pic/2021/12/15/1d8811.png)

4. 默认的是纵向选择候选词，可能不符合一般的使用习惯，打开目录`~/Library/Rime`下的文件`squirrel.custom.yaml`（如果不存在则新建），内容如下：

   ```yaml
   patch:
     style:
       horizontal: true
   ```

5. 选择重新部署后，可以实现横向选择了

   ![image-20211216175250203](https://pic-1251468582.file.myqcloud.com/pic/2021/12/16/7074b9.png)

## Rime的相关参考资料

1. [四叶草拼音输入方案，做最好用的基于rime开源的简体拼音输入方案！](https://github.com/fkxxyz/rime-cloverpinyin)
2. [Rime 配置：雾凇拼音 | 长期维护的简体词库](https://github.com/iDvel/rime-ice)
3. [Rime Squirrel 鼠须管配置文件（朙月拼音、小鹤双拼、自然码双拼）](https://github.com/ssnhd/rime)
4. [Rime（中州韵）全拼与双拼的自用配置方案](https://github.com/LufsX/rime)

