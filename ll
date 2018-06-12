import requests
response = requests.get('http://news.baidu.com/')
import re
a = response.text
result = re.findall('<a\shref="(http.*?)"',a)
print (result)