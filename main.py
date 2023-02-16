import requests
import re

# url = "http://localhost:7890/pages/31185780/02/31185780/02/resources/osn/alm/topic/alm_r_lof.html"
# resp = requests.get(url)
# page_content1 = resp.text
# 告警解释
# obj1 = re.compile(r'告警解释</h2>\n<div class="alarmdescbody"><p>(?P<explation>.*?)</p>')
# data1 = obj1.search(page_content1)
# print(data1)

f = open("1.txt",mode="r",encoding="utf-8")
page_content1 = f.read()

# 告警属性
obj2 = re.compile(r'<td valign="top" headers="mcps1.2.2.1.1"><p>(?P<jibie>.*?)</p>[\s\S]*?2.1.2"><p>(?P<leixing>.*?)</p>')
data2 = obj2.search(page_content1)
print(data2.group('jibie'))
print(data2.group(2))


算法