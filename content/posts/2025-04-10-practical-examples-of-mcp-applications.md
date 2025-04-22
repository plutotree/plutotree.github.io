---
title: MCP 实践例子分享
date: 2025-04-18T12:00:00+08:00
tags: [mcp, ai]
categories: [ai]
featuredImage: https://pic-1251468582.file.myqcloud.com/pic/2025/04/18/29ueFR.jpg
slug: practical-examples-of-mcp-applications
---

## 获取各旅游城市近期天气情况

### 传统方案的低效

传统方案不仅耗时费力（通常需要1小时以上），还存在较高的人为操作错误风险：

1. ​城市列表收集​：通过百度搜索手动整理全国旅游城市名录
2. ​数据采集阶段​：逐个访问天气网站，复制粘贴各城市气象数据
3. 成果输出阶段​：将零散数据手工整理为结构化表格或PPT

虽然开发人员可通过编写爬虫或调用API优化第2步，但面对一次性需求时，代码开发调试的时间成本往往难以覆盖收益。

### AI 工具的初步尝试

使用kimi、豆包、元宝等AI大模型时，直接提问【整理全国各大旅游城市近期天气情况，以表格形式返回】看似可行。但[实际测试](https://yuanbao.tencent.com/bot/app/share/chat/ntQkP3iMLbBN)，模型可能返回格式正确但数据时效存疑的结果——例如天气日期信息缺失或不明确。

### MCP 标准化解决方案

MCP（模型控制协议）通过统一接口标准，完美解决了API多样性和任务复杂性的矛盾。集成天气查询MCP能力的AI大模型，只需自然语言指令即可完成精准调用：

提问​：
整理全国主要旅游城市最近的天气情况，以表格形式返回，一个城市一行数据

​响应结果​（数据已精简）：

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

查看执行的过程，我们能看到大模型自动发起了多次工具调用，用于查询天气信息。

![天气MCP调用](https://pic-1251468582.file.myqcloud.com/pic/2025/04/18/SSXGRw.png)

通过Cherry-Studio可直观查看高德地图MCP服务的完整能力，天气查询仅是众多标准化接口之一，更主要的是提供路径规划和导航的能力。

![amap_tools_list](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/1FeKns.png)

## API 聚合平台的 MCP 转型实践

看完前面的的例子，有了 MCP 就能自动调用各类 API，而其能力自然也取决于 API 本身。这时候原来的一些 API 聚合平台是不是就能大显身手了。 下面以[ALApi](https://www.alapi.cn/)为例来展示下整体流程。

常用的 MCP 服务是用 node.js 和 python 服务为主，而事实上我们只要遵循一定标准就好，这个 ALApi 的[MCP 服务](https://github.com/ALAPI-SDK/mcp-alapi-cn)是用 go 实现的。

1. 账号及权限申请

   注册 [ALApi](https://www.alapi.cn/) 账号，申请 [token](https://www.alapi.cn/dashboard/data/token)，申请需要的[接口](https://www.alapi.cn/explore)。

   ![alapi-api](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/AYOLAT.png)

2. 服务部署

   编译MCP服务，编译成功后会生成`mcp-alapi-cn.exe`

   ```bash
   git clone "https://github.com/ALAPI-SDK/mcp-alapi-cn.git"
   cd mcp-alapi-cn
   git build
   ```

3. 系统集成

   在Cherry-Studio中配置MCP服务，名称任选，命令填写前面编译来的`mlp-alapi-cn.exe`全路径，环境变量配置申请的token即可。

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

4. 启用MCP

   配置完成后，Cherry-Studio 中访问的大模型的时候勾选相应的MCP服务就可以了

   ![cherry-studio-select-mcp](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/Hty52M.png)

### 应用场景展示

1. 查询油价：执行了一次工具 (api/oil) 查询

   ![search-oil-price](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/ODEKpp.png)

2. 查询汇率：执行了四次工具 (api/exchange) 查询

   ![search-exchange](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/xHyKMW.png)

3. 查询黄金等贵金属价格：

   ![search-gold-price](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/ofiZ00.png)

通过这种方式，ALApi上的所有API接口，都可以转换成MCP服务为大模型所用了。

![alapi-api-list](https://pic-1251468582.file.myqcloud.com/pic/2025/04/22/vtWj7W.png)

### 背后逻辑

整个流程是如何实现的呢？我们看下代码，可以发现先通过接口 `/api/user_apis` 获取所有有访问权限的API列表（名字、描述、参数列表等），然后将这些API依次进行注册。核心注册工具的代码如下：

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

## 总结

MCP最大的作用是实现了​标准化的接口层​，建立了统一的交互标准，并得到市场的认可。
