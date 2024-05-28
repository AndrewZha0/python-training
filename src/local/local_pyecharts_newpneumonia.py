import requests
import json
from pyecharts.charts import Line

url = 'https://voice.baidu.com/newpneumonia/getv2?from=mola-virus&stage=publish&target=trend&isCaseIn=1&area=%E8%BE%BD%E5%AE%81&callback=jsonp_1652526814976_84234'
response = requests.get(url).text
response = response.replace("jsonp_1652526814976_84234(", "")
response = response[:-2]

data = json.loads(response)
trend_data = data['data'][0]['trend']

line = Line()
line.add_xaxis(trend_data['updateDate'][:16])
line.add_yaxis("确诊", trend_data['list'][0]['data'][:16])
line.add_yaxis("治愈", trend_data['list'][1]['data'][:16])
line.add_yaxis("死亡", trend_data['list'][2]['data'][:16])
line.add_yaxis("新增确诊", trend_data['list'][3]['data'][:16])
line.add_yaxis("新增本土", trend_data['list'][4]['data'][:16])
line.render()
