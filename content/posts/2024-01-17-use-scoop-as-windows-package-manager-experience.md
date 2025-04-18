---
title: Windows 包管理器 Scoop的使用经验
date: 2024-01-17 18:00:00 +0800
tags: [scoop]
categories: [Software]
slug: use-scoop-as-windows-package-manager-experience
aliases: [/2024-01-17/use-scoop-as-windows-package-manager-experience.html]
---

如果有在 Mac 下用过`HomeBrew`的都知道，软件安装起来是多么方便。Windows 一直缺少这么方便的包管理工具。`Chocolatey`只能算是便捷的安装工具，和包管理工具差距还挺大的。`WinGet`可以算是一个包管理工具，只是目前支持的应用还比较少。以前有听说过[`Scoop`](https://scoop.sh)，印象中说法是支持的软件数量较少。不过最近试了下，发现其支持的软件数量已经相当广泛。各类常见开发工具自然不必说了，主流的软件其中包括部分国内软件都能在官方的 bucket 中找到。官方不支持的软件，我们也能通过第三方的 bucket 进行安装。目前我有 59 个软件是通过 scoop 进行安装了。

![image-20240117194514171](https://pic-1251468582.file.myqcloud.com/pic/2024/01/17/767a1a.png)

## Scoop 操作示例

1. 安装 scoop

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
   ```

2. 安装`main`的软件

   ```powershell
   scoop install go
   scoop install nodejs
   ```

3. 安装`extra`的软件 （也是官方维护，要求比`main`宽松）

   ```powershell
   scoop bucket add extras
   scoop install extras/apifox
   ```

4. 安装第三方软件（这是我自己的 bucket 哈）

   ```powershell
   scoop bucket add plutotree https://github.com/plutotree/scoop-bucket
   scoop install plutotree/qqmusic
   ```

5. 安装字体

   ```powershell
   scoop bucket add nerd-font
   scoop install hack-nf
   ```

6. 更新所有软件

   ```powershell
   scoop update
   scoop update *
   ```

安装流程和 Mac 下的 Homebrew 相似，scoop 用 json 来维护软件信息，做法也是和老版本的 homebrew 一样。不过 scoop 有点优势在于，绝大部分软件都能支持自动更新，官方也提供了 Github Action 组件，定时检测发现有新版本的时候会自动更新描述文件。

## Scoop 使用说明

1. 使用自定义目录进行安装

   ```powershell
   [environment]::setEnvironmentVariable('SCOOP', 'E:\Scoop', 'User')
   $env:SCOOP='E:\Scoop' # 如果不用这句话的话可以重开窗口也行
   iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
   ```

2. 增加常用的 bucket，可以参考官方介绍的[bucket 列表](https://github.com/ScoopInstaller/Scoop?tab=readme-ov-file#known-application-buckets)（质量比较高），我目前只加了 extra 和 nerd-fonts

   ```powershell
   scoop bucket add extra
   scoop bucket add nerd-fonts
   ```

3. 安装官方推荐的加速下载工具 aria2

   ```powershell
   scoop install aria2
   ```

4. 从控制面版卸载不需要的程序，然后通过 scoop 进行安装和管理。

- 查找：`scoop search xx`
- 安装： `scoop install xx`
- 卸载：`scoop uninstall xx`
- 升级: `scoop update; scoop update xx`
- 查看缓存（下载的安装包）：`scoop cache`
- 删除缓存：`scoop cache rm xx` （\*表示所有软件）
- 查看已安装软件：`scoop list`
- 删除软件的旧版本：`scoop cleanup xx` （\*表示所有软件）
- 删除软件的旧版本同时清理缓存：`scoop cleanup -k xx`（\*表示所有软件）

### 哪些软件不适合

绿色软件是更适合的，而和系统关联性太强的软件是不适合的，尤其是需要管理员权限进行安装的。尽管 scoop 也支持使用管理权限进行安装，但是同样更新和卸载也许要管理权限，我觉得就没必要了而且维护起来会比较麻烦。

目前就我电脑上的软件而言，没有使用 scoop 管理的主要是：

1. 系统驱动和厂商管理工具，比如 Nvidia、HP 等管理工具；
2. 微软的开发工具和环境依赖，比如`Microsoft Visual C++ xx Redistributables`、`Microsoft Windows Desktop Runtime`等；
3. 微软自带的部分商店应用，比如主题、微软 TODO 工具、画图工具、3D 查看器等；
4. 和系统关联系比较大，或者不方便迁移出来的，比如 Adobe 系列、Office 软件、iTunes、输入法等；
5. 平台类软件，需要使用其更新管理，比如 steam、Epic 等，后续需要研究下；
6. 专业软件，或者内部使用的软件；
7. 部分还没来得及迁移的软件，比如 TortoseSVN、QQ、微云等；

### 查找软件

可以使用命令`scoop search`进行搜索，不过建议是在[官网](https://scoop.sh)进行搜索，需要注意的是选项`Official bucket only`选项是否开启，一般情况下是建议安装官方包，以及可信赖的第三方。而我个人而言，第三方目前会控制在自己的 bucket 范围。

![image-20240117195631058](https://pic-1251468582.file.myqcloud.com/pic/2024/01/17/fb9b29.png)

在官方查找不到的时候，可以扩展到第三方，找到之后可以修改后何如自己的 bucket 中。第三方的 bucket 其实质量并一定能保证，最后看下描述文件内容，以及是否从官网下载。还有部分维护破解软件的第三方 bucket，建议就不要使用了。还有就是关注下 bucket 的 star 数量，毕竟 star 多点还是稍微靠谱点。这个[网站](https://rasa.github.io/scoop-directory/by-stars)提供按 star 数量排名的 bucket 列表，也可以参考下，蛮多是中国人维护的 bucket。

![image-20240117200008573](https://pic-1251468582.file.myqcloud.com/pic/2024/01/17/6b538b.png)

## 维护自己的 bucket

1. 创建一个自己的 bucket
   - 在 GitHub 上直接通过[Bucket 模板](https://github.com/ScoopInstaller/BucketTemplate)新建一个仓库；
   - 按照提示说明，修改仓库的设置，开启读写权限；
   - 修改几个文件的占位符，指定下仓库名信息；
2. 维护自己软件的描述信息，
   - 自己写应用描述信息，或者直接复用第三方，或者在其基础上修改；
3. 增加自己的 bucket：`scoop bucket add BUCKET_NAME YOUR_BUCKET_GIT_ADDRESS`
4. 安装自己的软件：`scoop install BUCKET_NAME/APP_NAME`

## 应用描述信息

这块算是 scoop 中最复杂的内容了，官方文档提供了基础的介绍，更有用的话应该需要多参考已有的描述。我们来看几个例子

### Cos-Browser

```json
{
  "version": "2.11.13",
  "description": "A visualization interface tool provided by Tencent Cloud COS, view, transfer, and manage COS resources easily",
  "homepage": "https://github.com/tencentyun/cosbrowser",
  "license": "Freeware",
  "url": "https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-2.11.13.exe#/dl.7z",
  "hash": "sha512:0063411445cc4a2af098b71780525ec2e190f396934d1b910fbd62aea897ce99a0b2099a848d15df871e7f774aa7334be6acd2c4c4de2e9d0ae8cce05830940f",
  "architecture": {
    "64bit": {
      "pre_install": "Expand-7zipArchive \"$dir\\`$PLUGINSDIR\\app-64.7z\" \"$dir\""
    },
    "32bit": {
      "pre_install": "Expand-7zipArchive \"$dir\\`$PLUGINSDIR\\app-32.7z\" \"$dir\""
    }
  },
  "post_install": "Remove-Item \"$dir\\`$*\" -Force -Recurse",
  "shortcuts": [
    ["cosbrowser.exe", "COSBrowser", "--user-data-dir=\"$dir\\UserData\""]
  ],
  "persist": "UserData",
  "checkver": {
    "url": "https://cos5.cloud.tencent.com/cosbrowser/latest.yml",
    "regex": "version: ([\\d.]+)"
  },
  "autoupdate": {
    "url": "https://cos5.cloud.tencent.com/cosbrowser/cosbrowser-setup-$version.exe#/dl.7z",
    "hash": {
      "url": "$baseurl/latest.yml",
      "regex": "sha512: $base64"
    }
  }
}
```

看下整体流程：

1. 下载指定 URL，下载后进行 Hash 校验；
2. URL 后面有`#/dl.7z`，在校验成功后会直接使用 7zip 进行解压缩；
3. 调用`pre_install`脚本内容，这里使用了`Expand-7zipArchive`解压缩；
4. 调用`install`脚本内容，这个应用是空的；
5. 创建快捷方式，这里关注下有指定参数`--user-data-dir`，这样就不会使用系统的`AppData`目录了。猜测这个参数是 electron 开发的软件都会有的，其它框架开发的就不支持了。
6. 调用`post_install`脚本内容，这里主要就是删除一些无用的文件；
7. `persist`指定了需要持久化的目录，scoop 会帮忙创建一个链接，并且卸载的时候不会删除；
8. checkver 是用来检测是否有新版本，autoupdate 是用来在有新版本的时候进行下载并且更新描述文件。这两块的细节内容会比较复杂点，可以参考[官方文档](https://github.com/ScoopInstaller/Scoop/wiki/App-Manifest-Autoupdate)。

### Evernote

```json
{
  "version": "10.71.2",
  "description": "[Evernote] Use it for note taking, project planning and organize everything",
  "homepage": "https://evernote.com",
  "license": "Freeware",
  "url": "https://win.desktop.evernote.com/builds/Evernote-latest.exe#/dl.zip",
  "hash": "7e3b3565651b6ddeaa9dfb86502951917d996b09ebd32f2ce11509325d3bcce1",
  "architecture": {
    "64bit": {
      "pre_install": "Expand-7zipArchive \"$dir\\`$PLUGINSDIR\\app-64.7z\" \"$dir\""
    },
    "32bit": {
      "pre_install": "Expand-7zipArchive \"$dir\\`$PLUGINSDIR\\app-32.7z\" \"$dir\""
    }
  },
  "post_install": "Remove-Item \"$dir\\`$*\" -Force -Recurse",
  "shortcuts": [["Evernote.exe", "Evernote"]],
  "checkver": {
    "url": "https://evernote.com/release-notes",
    "regex": "Version.*?([\\d.]+)"
  },
  "autoupdate": {
    "url": "https://win.desktop.evernote.com/builds/Evernote-latest.exe#/dl.zip"
  }
}
```

基本上和 Cos-Browser 的信息是类似的，但是 autoupdate 这里没有指定 Hash 获取方式，其实是官方没有提供，这种情况下的话就只能等文件下载完成之后再进行 hash 计算了，理论上来说是存在文件下载异常描述信息有问题的，这种的话就只能等发现之后手动修复了。

### QQ 音乐

```json
{
  "##": "QQ音乐",
  "version": "20.05.0",
  "description": "[QQ音乐] 千万正版音乐海量无损曲库新歌热歌天天畅听的高品质音乐平台",
  "homepage": "https://y.qq.com",
  "license": "Freeware",
  "url": "https://dldir1.qq.com/music/clntupate/QQMusic_YQQWinPCDL.exe#/dl.7z",
  "hash": "4c35742f11a011e8aff31987966e29b014fcdabfd6f50240125c8252f86188b2",
  "post_install": "Copy-Item \"$dir\\QQMusic.tpc\" \"$dir\\instok\"",
  "checkver": {
    "url": "https://y.qq.com/download/download.html",
    "regex": "Windows PC.*\\:([\\d.]+)"
  },
  "shortcuts": [
    ["QQMusic.exe", "QQ音乐"],
    ["QQMusic.exe", "QQ Music"]
  ],
  "autoupdate": {
    "url": "https://dldir1.qq.com/music/clntupate/QQMusic_YQQWinPCDL.exe#/dl.7z"
  }
}
```

这里我们创建了两个快捷方式，分别是 QQ 音乐和`QQ Music`，这样不管输入的是哪个都能启动了。同样 QQ 音乐也没提供 hash 获取方式，只能下载后本地计算。

### 补充说明

腾讯会议比较奇怪，不能直接在`current`目录启动，而必须在版本目录启动，所以就不能用自带的快捷方式，而需要手动创建了。

```json
{
  "pre_install": [
    "Rename-Item \"$dir\\`$_*_\" \"$dir\\$version\"",
    "Remove-Item \"$dir\\`$*\",\"$dir\\wemeetapp_new.exe\" -Recurse -Force",
    "startmenu_shortcut -target $(Get-Item \"$dir\\wemeetapp.exe\") -shortcutName \"Tencent Meeting\"",
    "startmenu_shortcut -target $(Get-Item \"$dir\\wemeetapp.exe\") -shortcutName \"腾讯会议\""
  ],
  "pre_uninstall": [
    "if (Get-Process -Name \"wemeetapp\" -Erroraction SilentlyContinue) {Stop-Process -Name \"wemeetapp\"}",
    "if (Test-Path \"$(shortcut_folder)\\Tencent Meeting.lnk\"){Remove-Item \"$(shortcut_folder)\\Tencent Meeting.lnk\" -Force}",
    "if (Test-Path \"$(shortcut_folder)\\腾讯会议.lnk\"){Remove-Item \"$(shortcut_folder)\\腾讯会议.lnk\" -Force}"
  ]
}
```

有些软件是不能直接解压缩的，而是通过 Inno 方式进行安装，这种的话 scoop 也有自带提供支持，可以参考其它软件，等我遇到的时候再补充。

## 问题记录

### GitHub 访问 401 问题

遇上 GitHub API 访问受限导致的 401 问题，可以设置环境变量`SCOOP_GH_TOKEN`，使用自己的 Access Token 即可。创建 Access Token 的时候不需要指定任何特别的权限，使用默认权限即可。

### 应用打开网址无法拉起 Chrome 浏览器

尝试过多种方法但是仍然有不低的概率遇上，最后只能放弃使用 scoop 来维护 Chrome，换成 chrome 默认安装之后问题就不再出现了。

### everything 开机启动无效

这里主要在使用 uTools 调用 everything 搜索的时候，每次开机启动需要重新进行索引，按照 uTools 的说法，如果使用的是安装版并且开机启动的前提下，是不会触发使用内置的绿色版 everything 而导致重新索引的问题的。最后也放弃使用 scoop 维护 everything，而使用官方的安装版本进行安装。不过这个问题也可能通过修改 everything 的配置项能解决。

### hash 校验不一致导致无法安装

有一种可能是更换了安装包但是没有更换版本号，也有可能是计算 hash 的时候遇到了一些bug。在执行 `scoop install` 的时候只要增加 `-s` 参数即可跳过 hash 校验。
