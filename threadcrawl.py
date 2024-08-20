import requests
import threading
import tqdm
import time

# 计数变量
request_count = 0
# 异常退出线程计数变量
exception_count = 0
# 拦截变量
badrq = 0
badcode = []
passrq = 0
# 锁对象
lock1 = threading.Lock()

# 爬虫方法
def ceshi(i):
    global request_count
    global badrq
    global badcode
    global passrq
    global lock1
    global exception_count
    headers = {
        'Host': 'www.xxx.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Cookie': '',
    }
    try:
        response = requests.get(url='http://www.mytju.com/classcode/tools/urldecode_gb2312.asp', headers=headers)
        with lock1:
            request_count += 1
            if str(response.status_code) == '200':
                passrq += 1
            else:
                badrq += 1
                badcode.append(str(response.status_code))
    except Exception as e:
        with lock1:
            request_count += 1
            exception_count += 1  # 记录异常退出线程数量
        tqdm.tqdm.write(f"请求发生异常：{e}")

# 主程序
def main():
    global request_count
    global badrq
    global badcode
    global passrq
    global exception_count
    
    t = []
    for j in tqdm.trange(3):
        start_time = time.time()
        
        for i in range(1,500):
            t.append(threading.Thread(target=ceshi, name=i, args=(i,)))
        
        for thread in t:
            thread.start()
        
        for thread in t:
            thread.join()
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        qps = request_count / elapsed_time if elapsed_time > 0 else 0
        tqdm.tqdm.write("QPS=" + str(qps))
        
        request_count = 0
        t = []
    tqdm.tqdm.write('已拦截请求数量：' + str(badrq))
    for i in set(badcode):
        tqdm.tqdm.write('已拦截请求状态码为：' + i)
    tqdm.tqdm.write('正常请求数量：' + str(passrq))
    tqdm.tqdm.write('异常退出线程数量：' + str(exception_count))  # 打印异常退出线程数量

# 执行逻辑
if __name__ == "__main__":
    main()