import urllib3
import urllib.request
import os
from bs4 import BeautifulSoup
import re
method = 'GET'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
url = 'http://www.netbian.com'
#创建poolmanager对象的实例
http = urllib3.PoolManager()
#创建请求对象
response = http.request(method,url,headers)
#解析请求的返回数据
soup = BeautifulSoup(response.data,features='lxml',exclude_encodings='utf-8')
#查找<div class='list'>标签
div = soup.find('div',attrs={'class':'list'})
#查找<div class='list'>标签下的<li>标签
list_li = div.find_all('li')
name_list = []      #定义保存壁纸名称的列表
href_list = []      #定义保存壁纸地址的列表
for item in list_li:
    name = item.a.img['alt']
    href = item.a.img['src']
    name_list.append(name)
    href_list.append(href)
'''##############################################
测试是否返回正确的名称和地址，不是该程序的代码
print(name_list)
print(len(name_list))
print('#'*80)
print(href_list)
print(len(href_list))
##############################################'''
#测试要创建的目录是否存在
_path = os.getcwd()
new_path = os.path.join(_path,'壁纸')
if not os.path.isdir(new_path):
    os.mkdir(new_path)
new_path += '\\'    #在创建的目录加'/'才能在该目录下创建文件
for number in range(len(href_list)):
    savename = new_path + name_list[number]
    #正则表达式判断地址中是否存在'/'，因为Windows系统在创建文件名时认为'/'为非法字符
    pattern = '/'
    match = re.search(pattern,savename)
    if  match != None:      #如果匹配成功，则说明字符串中含有'/'；re的reserch方法如果没有匹配成功，则返回none值。
        savename= '200'
    urllib.request.urlretrieve(href_list[number],savename + '.jpg')
    