import requests
from bs4 import BeautifulSoup as bs
import re
html1=requests.get("http://www.geeksforgeeks.org/python/")
html1=html1.content
sp=bs(html1,"html.parser")
ph=re.compile(r'(<li><a href=.*</a></li>)(\\n)')
mt=ph.findall(str(html1))
sp1=bs(str(mt),"html.parser")
links=sp1.find_all('a',href=True)
for i in links:
	name=i.string
	print(name)
	link=requests.get(i['href'])
	with open(name+".html", "wb") as code:
		code.write(link.content)
	print("done")
print("final")

''''
This is Alternative Way by Regex

urls = list(re.findall(r'href=[\'"]?([^\'" >]+)', str(mt)))
t=1
for i in urls[]:
	link=requests.get(i)
	with open(str(t)+".html", "wb") as code:
		code.write(link.content)
	print('done')
	t+=1
print("final")


'''