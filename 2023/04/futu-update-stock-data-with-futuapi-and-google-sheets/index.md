# 使用富途 API 实现 Google 表格的股票数据在线更新


对于查看和分析股票的基础数据，在线表格其实是很不错的分析工具，筛选、排序、数据透视图等操作简直太方便了。

Google文档提供了很强的函数[`GOOGLEFINANCE`](https://support.google.com/docs/answer/3093281?hl=zh-Hans)，能获取比较丰富的股票数据，通过`GOOGLEFINANCE("SHE:001309","price")`就能获取最新价格，但是不支持上证只支持深证股票，无奈只能放弃。腾讯文档提供了比较基础的`STOCK`，能获取比较基础的股票数据。那么我们如何才能实现复杂的股票数据处理呢？Google文档提供了API进行相关的数据操作，而富途API也提供了完整的股票数据获取，结合两者，我们就可以实现完整的流程了。

```mermaid
graph LR

A[通过Google API获取表格内的股票列表]
B[通过futu API获取相关股票的行情信息]
C[通过Google API更新表格内的行情数据]

A-->B-->C
```

来直接看下效果：

- 这是现在Google表格的数据内容，只有股票代号，没有其余信息

  ![image-20230414200118396](https://pic-1251468582.file.myqcloud.com/pic/2023/04/14/777ecb.png)

- 这是执行脚本后的效果，自动填充了所有内容（这里表格的列是可以动态调整的）

  ![image-20230414200156119](https://pic-1251468582.file.myqcloud.com/pic/2023/04/14/d4e1ef.png)

下面简单描述下技术细节：

## 通过Google API读取及更新表格内容

Google官方提供了非常详细的[示例](https://developers.google.com/sheets/api/guides/values?hl=zh-cn#read_multiple_ranges)，直接参考应该就可以操作了。注意一点，好像是只支持OAuth方式进行操作，这点还是稍有些不方便。仅做了层简单的封装，暴露外部的接口如下：

```python
try:
    sheets = GoogleSheets(token_file)
except InvalidCrendentialException as err:
    DoAuth(token_file)
    sheets = GoogleSheets(token_file)

# 读取单个范围数据
print(sheets.GetValue(spreadsheet_id, 'A2:C3'))

# 同时读取多个范围数据
print(sheets.BatchGetValue(spreadsheet_id, ['A2:B4', 'C2:D4']))

# 更新多个范围数据
range_list = ['B3:C4', 'E3:F4']
values_list = [[['x1', 'x2'], ['x3', 'x4']], [['x5', 'x6'], ['x7', 'x8']]]
sheets.BatchUpdateValue(spreadsheet_id, range_list, values_list)

# 更新单个范围数据
sheets.UpdateValue(spreadsheet_id, 'A15:B16', [['xx', 'yy'], ['zz', 'hh']])
```

## 通过富途API读取股票基础行情

这里也制作了一层简单的封装，具体可以参考富途官方的说明。我们需要在机器上先安装FutuOpenD，可以在服务器上安装，并监听`0.0.0.0`，这样可以在各个客户端直接调用了。

```python
class FutuHelper:

    def __init__(self, host, port):
        self.quote_ctx = OpenQuoteContext(host, port)

    def __del__(self):
        self.quote_ctx.close()

    def GetMarketState(self, code_list):
        """获取指定标的的市场状态
        获取stock_name(股票名称)、market_state(交易情况)
        参考：https://openapi.futunn.com/futu-api-doc/quote/get-market-state.html
        """
        return self.quote_ctx.get_market_state(code_list)

    def GetMarketSnapshot(self, code_list):
        """获取快照
        获取各类价格信息，包含最新价、开盘、最高、最低、最新、均价、历史高价、历史低价等，以及
        财务信息，包含市盈率、总市值、流通市值、资产净值、净利润、每股盈利、股本数量等
        参考：https://openapi.futunn.com/futu-api-doc/quote/get-market-snapshot.html
        """
        return self.quote_ctx.get_market_snapshot(code_list)
```

## 处理股票行情数据

为了方便表的列名使用中文描述，做一层简单的转换，同时增加一些自定义的字段。比如富途本身不支持涨跌幅，我们可以拿最新价和昨日收盘价计算即可。还有一些用来方便查看的数据，比如高点对比、低点对比等。

![image-20230414200923885](https://pic-1251468582.file.myqcloud.com/pic/2023/04/14/91fee0.png)

处理流程相对比较简单，主要的数据通过[`get_market_snapshot`](https://openapi.futunn.com/futu-api-doc/quote/get-market-snapshot.html)获取即可。这里扩展的话，我们可以增加一些历史K线数据字段，比如3日最高价、3日均线等等。

## 扩展下

有这个流程了之后，还可以做更多事情：

- 同步自选股：从google文档读取自选股列表，通过富途API同步自选股。这样的话可以用Google文档作为源数据进行维护，可惜同花顺没有API进行自选股同步；

- 批量更新到价提醒：从google文档读取特定股票列表，通过富途API批量增加到价提醒；

