---
title: MCP 实践例子分享
date: 2025-04-18T12:00:00+08:00
tags: [mcp, ai]
categories: [ai]
featuredImage: https://pic-1251468582.file.myqcloud.com/pic/2025/04/18/29ueFR.jpg
slug: practical-examples-of-mcp-applications
---

## 获取各旅游城市近期天气情况

传统方案可能需要花费 1 个小时以上，还容易出错

1. 百度上搜索全国下有哪些旅游城市；
2. 在天气网站上搜索每个城市的天气信息，然后手动拷贝数据；
3. 将上述数据整理成表格或者 ppt；

当然，如果如果会写代码，第 2 步就可以通过程序来解决。不管是直接解析页面还是通过 API 获取都能确保不出错。不过如果是一次性的工作，可能写代码及调试的时间消耗也不一定能节省多少。

对于有使用 kimi、豆包、元宝等 AI 大模型的人来说，肯定也会直接尝试用 AI 来解决问题。我们尝试把问题直接丢给元宝【整理下全国各大旅游城市近期天气情况，以表格形式返回】，元宝会有模有样给你搜索及整理一番，只是最后的天气你都不知道是哪一天的。[访问](https://yuanbao.tencent.com/bot/app/share/chat/ntQkP3iMLbBN)或者测试下是不是这样。

这时候你可能会想，如果 AI 能写代码访问 API 接口就好了，考虑到任务五花八门，接口千变万化，这里如果能有一套统一标准那就好了。没错，MCP 就是来解决这个事情的。

我们先直接看下效果，对于集成了具备天气查询 MCP 能力的 AI 大模型，我们只要提出问题就可以了。

问题：整理全国主要旅游城市最近的天气情况，以表格形式返回，一个城市一行数据
回答：（表格数据有删减）

| 城市   | 日期       | 白天天气 | 夜间天气 | 白天温度 | 夜间温度 | 白天风向 | 夜间风向 | 白天风力 | 夜间风力 |
| ------ | ---------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 北京市 | 2025-04-18 | 中雨     | 小雨     | 19℃      | 8℃       | 南       | 南       | 1-3 级   | 1-3 级   |
| 北京市 | 2025-04-19 | 多云     | 晴       | 21℃      | 11℃      | 南       | 南       | 1-3 级   | 1-3 级   |
| 上海市 | 2025-04-18 | 阴       | 阴       | 31℃      | 18℃      | 东南     | 东南     | 1-3 级   | 1-3 级   |
| 上海市 | 2025-04-19 | 小雨     | 小雨     | 28℃      | 17℃      | 南       | 南       | 1-3 级   | 1-3 级   |
| 广州市 | 2025-04-18 | 阵雨     | 阵雨     | 28℃      | 22℃      | 南       | 南       | 1-3 级   | 1-3 级   |
| 广州市 | 2025-04-19 | 阵雨     | 多云     | 28℃      | 23℃      | 南       | 南       | 1-3 级   | 1-3 级   |
| 深圳市 | 2025-04-18 | 阴       | 阴       | 30℃      | 24℃      | 东南     | 东南     | 1-3 级   | 1-3 级   |
| 深圳市 | 2025-04-19 | 阴       | 阴       | 30℃      | 24℃      | 西南     | 西南     | 4 级     | 4 级     |
| 成都市 | 2025-04-18 | 多云     | 小雨     | 33℃      | 17℃      | 北       | 北       | 1-3 级   | 1-3 级   |
| 成都市 | 2025-04-19 | 阴       | 阴       | 35℃      | 17℃      | 北       | 北       | 1-3 级   | 1-3 级   |
| 杭州市 | 2025-04-18 | 晴       | 小雨     | 32℃      | 21℃      | 东       | 东       | 1-3 级   | 1-3 级   |
| 杭州市 | 2025-04-19 | 小雨     | 多云     | 29℃      | 21℃      | 西南     | 西南     | 1-3 级   | 1-3 级   |
| 西安区 | 2025-04-18 | 阵雨     | 多云     | 13℃      | 3℃       | 西南     | 西南     | 1-3 级   | 1-3 级   |
| 西安区 | 2025-04-19 | 多云     | 晴       | 17℃      | 3℃       | 西南     | 西南     | 1-3 级   | 1-3 级   |
| 重庆市 | 2025-04-18 | 晴       | 多云     | 34℃      | 21℃      | 东       | 东       | 1-3 级   | 1-3 级   |
| 重庆市 | 2025-04-19 | 多云     | 多云     | 33℃      | 21℃      | 南       | 南       | 1-3 级   | 1-3 级   |
| 武汉市 | 2025-04-18 | 多云     | 小雨     | 34℃      | 19℃      | 北       | 北       | 1-3 级   | 1-3 级   |
| 武汉市 | 2025-04-19 | 阴       | 多云     | 30℃      | 20℃      | 北       | 北       | 1-3 级   | 1-3 级   |
| 南京市 | 2025-04-18 | 晴       | 阴       | 31℃      | 20℃      | 东南     | 东南     | 4 级     | 4 级     |
| 南京市 | 2025-04-19 | 阴       | 多云     | 32℃      | 17℃      | 北       | 北       | 4 级     | 4 级     |

而在这个过程中，大模型是通过调用具备查询天气情况的 MCP 服务来实现，而这个 MCP 服务用的是高德地图 MCP 服务，天气查询其实只是他的众多能力之一。

![天气MCP调用](https://pic-1251468582.file.myqcloud.com/pic/2025/04/18/SSXGRw.png)

在 Cherry-Studio 中我们很方便查看一个 MCP 服务具备的所有能力（工具列表）：

![amap_tools_list](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/1FeKns.png)

## 聚合 API 平台的新用处

看完天气预报的例子，你可能会 MCP 有点像是大模型根据上下文来自动调用 API。而原来的一些 API 聚合平台提供了大量的 API 访问，我们是不是就能让大模型来帮我们自动调用了。

这里以[ALApi](https://www.alapi.cn/)为例来展示下整体流程。

常用的 MCP 服务是用 node.js 和 python 服务为主，而事实上我们只要遵循一定标准就好，这个 ALApi 的[MCP 服务](https://github.com/ALAPI-SDK/mcp-alapi-cn)是用 go 实现的。

1. 注册 [ALApi](https://www.alapi.cn/) 账号，申请 [token](https://www.alapi.cn/dashboard/data/token)，申请需要的[接口](https://www.alapi.cn/explore)。我申请了三个免费的接口：

   ![alapi-api](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/AYOLAT.png)

2. 编译MCP服务，编译成功后会生成`mcp-alapi-cn.exe`

   ```bash
   git clone "https://github.com/ALAPI-SDK/mcp-alapi-cn.git"
   cd mcp-alapi-cn
   git build
   ```

3. 在Cherry-Studio中配置MCP服务，名称任选，命令填写前面编译来的`mlp-alapi-cn.exe`全路径，环境变量配置申请的token即可。

   ![alapi-setting](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/OUwAgO.png)

   如果在Cline、Claude等其他客户端中配置的话，可以粘贴下述json（需要和其他的mcp配置合并下）

   ```json
   {
     "mcpServers":{
       "ALAPI":{
         "name":"ALAPI",
         "type":"stdio",
         "isActive":true,
         "command":"D:\\xxx\\mcp-alapi-cn.exe",
         "args":[
           
         ],
         "env":{
           "ALAPI_TOKEN":"YOUR_API_TOKEN"
         }
       }
     }
   }
   ```

4. 配置完成后，Cherry-Studio中访问的时候勾选相应的MCP服务就可以正常访问了

   ![cherry-studio-select-mcp](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/Hty52M.png)

下面我们来看几个使用例子：

1. 查询油价：执行了一次工具 (api/oil) 查询

   ![search-oil-price](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/ODEKpp.png)

2. 查询汇率：执行了四次工具 (api/exchange) 查询

   ![search-exchange](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/xHyKMW.png)

3. 查询黄金等贵金属价格：

   ![search-gold-price](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/ofiZ00.png)

通过这种方式，ALApi上的所有API接口，都可以转换成MCP服务为大模型所用了。

![alapi-api-list](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/vtWj7W.png)

我们再看下这背后是如何实现的：

通过接口 `/api/user_apis` 获取所有有访问权限的API列表（名字、描述、参数列表等），然后将这些API依次进行注册。注册工具的代码如下：

```golang
func (s *Server) registerOpenAPITools(doc *openapi3.T) error {
    toolCount := 0
    for path, item := range doc.Paths.Map() {
        if item.Post != nil {
            tool := mcp.NewTool(path, mcp.WithDescription(item.Post.Summary))
            schema := item.Post.RequestBody.Value.Content["application/json"].Schema

            requiredParams := make(map[string]bool)
            for _, required := range schema.Value.Required {
                requiredParams[required] = true
            }

            for paramName, ref := range schema.Value.Properties {
                description := ref.Value.Description
                if requiredParams[paramName] {
                    mcp.WithString(paramName, mcp.Description(description), mcp.Required())(&tool)
                } else {
                    mcp.WithString(paramName, mcp.Description(description))(&tool)
                }
            }

            s.mcpServer.AddTool(tool, s.wrapHandler(s.handler.Handle))
            toolCount++
        }
    }

    if toolCount == 0 {
        return fmt.Errorf("no tools were registered from the OpenAPI spec")
    }

    return nil
}
```
