import re
import os
import argparse
import requests

#获取目录中js路径：遍历文件夹获取全局js文件的绝对路径（返回值为列表）
def get_js_files(dir_path):
    js_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith((".js", ".json", ".txt",".wxss")):
                js_path = os.path.join(root, file)
                js_files.append(js_path)
    return js_files
#js文件处理函数：获取js文件中的url（返回值为列表）
def jswork(path):
    #pattern = r"""(?:"|')(((?:[a-zA-Z]{1,10}://|//)[^"'/]{1,}\.[a-zA-Z]{2,}[^"']{0,})|((?:/|\.\./|\./)[^"'><,;| *()(%%$^/\\\[\]][^"'><,;|()]{1,})|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{1,}\.(?:[a-zA-Z]{1,4}|action)(?:[\?|/][^"|']{0,}|))|([a-zA-Z0-9_\-]{1,}\.(?:php|asp|aspx|jsp|json|action|html|js|txt|xml)(?:\?[^"|']{0,}|)))(?:"|')"""
    pattern = r"""
      (?:"|')                               # Start newline delimiter
      (
        ((?:[a-zA-Z]{1,10}://|//)           # Match a scheme [a-Z]*1-10 or //
        [^"'/]{1,}\.                        # Match a domainname (any character + dot)
        [a-zA-Z]{2,}[^"']{0,})              # The domainextension and/or path
        |
        ((?:/|\.\./|\./)                    # Start with /,../,./
        [^"'><,;| *()(%%$^/\\\[\]]          # Next character can't be...
        [^"'><,;|()]{1,})                   # Rest of the characters can't be
        |
        ([a-zA-Z0-9_\-/]{1,}/               # Relative endpoint with /
        [a-zA-Z0-9_\-/]{1,}                 # Resource name
        \.(?:[a-zA-Z]{1,4}|action)          # Rest + extension (length 1-4 or action)
        (?:[\?|/][^"|']{0,}|))              # ? mark with parameters
        |
        ([a-zA-Z0-9_\-]{1,}                 # filename
        \.(?:php|asp|aspx|jsp|json|
             action|html|js|txt|xml)             # . + extension
        (?:\?[^"|']{0,}|))                  # ? mark with parameters
      )
      (?:"|')                               # End newline delimiter
    """
    with open(path,'r',encoding='utf-8') as f:
        content = f.read()
    url = []
	#正则匹配
    pattern1 = re.compile(pattern, re.VERBOSE)
    links = re.findall(pattern1,content)
    if links != []:
        for i in links:
			#结果为元组序列
            for j in i:
                if j == '':
                    pass
                else:
                    url.append(j)
    #去重：这个正则表达式有点问题，会重复匹配两个值，需要去重处理
    url = set(url)
    return url
#大范围js文件中提取url_path并输出-处理逻辑
def bw(dir_path):
    for i in get_js_files(dir_path):
        for j in jswork(i):
            print(j.strip())
#单个js文件中提取url_path并输出-处理逻辑
def sw(path):
    for i in jswork(path):
        print(i.strip())


#url爬虫实现
def send_get(url,cookie=None):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
    }
    for i in url:
        response = requests.get(url=i,headers=headers,cookies=cookie)
        if response.status_code in [200,302,401,301,403]:
            results.append(str(response.status_code)+'-'+str(len(response.content))+': '+i.strip())
    return results
#url拼接url_path处理
def url(url,url_path):
    new_url_list = []
    for path in url_path:
        if path.startswith('http'):
            new_url_list.append(path)
        else:
            if not path.startswith('/'):
                path = '/' + path
            new_url_list.append(url + path)
    return new_url_list
#未授权接口测试逻辑
def pw(args):
    url_path = []
    url_l = []
    results = []
    #url_path获取
    if getattr(args,'range'):
        for i in get_js_files(getattr(args,'range')):
            for j in jswork(i):
                url_path.append(j.strip())
    else:
        for i in jswork(getattr(args,'alone')):
            url_path.append(i.strip())
    #通过url_path，处理成url
    url_l = url(args.url,url_path)
    #url爬取
    if getattr(args,'cookie'):
        results = send_get(url_l,args.cookie)
    else:
        results = send_get(url_l)
    for i in results:
        print(i)


#命令行参数获取
def parse_args():
    parse = argparse.ArgumentParser(usage='js_tackle工具',description='描述：处理js文件的脚本：主要用于从js文件中提取url_path，进行未授权接口检测（日常批量自动化处理~）；')
    parse.add_argument('-r','--range',help='js文件所处目录路径：大范围js文件中提取url_path处理')
    parse.add_argument('-a','--alone',help='js文件路径：单个js文件中提取url_path处理')
    parse.add_argument('-p','--ptest',action='store_true',help='（可选）只有填了这个参数才会测试接口，不然仅仅爬取url_path并输出！')
    parse.add_argument('-u','--url',help='（可选）(选择了-p参数必选)需要根据提取的path测试未授权接口的url')
    parse.add_argument('-c','--cookie',help='（可选）（可选）cookie设置')
    args = parse.parse_args()
    return args
#程序主运行函数
    #通过字典的形式来优化参数判断
def main(args):
    actions = {
        "range": bw,
        "alone": sw,
    }
    #循环判断命令行参数选择
    for action in actions:
        if getattr(args,action):
            if getattr(args,'ptest') and getattr(args,'url'):
                pw(args)
            else: 
                actions[action](getattr(args,action))

if __name__ == "__main__":
    main(parse_args())