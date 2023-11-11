#小公举缝合怪~
import random
import argparse #goby需要
import re
import xlrd
import os
import base64 #base64需要
import hashlib#md5需要
import os   #swaks需要
import time

#base64编码
def enbase64(i):
    print(str(base64.b64encode(i.encode('utf-8')),encoding= 'utf-8'))
def debase64(i):
    print(str(base64.b64decode(i.encode('utf-8')),encoding= 'utf-8'))
#md5算法
def enmd5(i):
    hash = hashlib.md5()
    hash.update(i.encode(encoding='utf-8'))
    print('32位加密串小写：',hash.hexdigest())
    print('32位加密串大写：',hash.hexdigest().upper())
    print('16位加密串小写：',hash.hexdigest()[8:24])
    print('16位加密串大写：',hash.hexdigest().upper()[8:24])
#16进制数据处理
def hex(i):
    #将原始数据流，插入0x变为16进制
    pattern = re.compile('.{2}')
    #compile生成一个正则表达式对象（pattern），.{2}固定匹配两位字符
    str_16 = ('0X'.join(pattern.findall(i)))
    #findall-在字符串中找到正则表达式所匹配的所有子串
    str_16 = '0X' + str_16
    print(str_16)
#goby数据端口处理
def gobyport():
    #xlrd版本过高会导致读取xlsx文件时报错（xlrd.biffh.XLRDError: Excel xlsx file; not supported），解决：
    #安装低本班xlrd：pip install xlrd==1.2.0
    try:
        path = input('请输入goby文件路径：')
        resultpath = input('请输入结果存储路径（文件夹）：')

        work = xlrd.open_workbook(path)
        sheet = work.sheet_by_name('assetSheet')
        nrows = sheet.nrows

        while True:
            resultcode = ''
            port = input('请输入需要整理的特殊端口：')
            for i in range(nrows):
                ports = sheet.cell_value(i, 1).split(',')
                if port in ports:
                    print(sheet.cell_value(i, 0))
                    resultcode += sheet.cell_value(i, 0) + '\n'

            if resultcode and os.path.exists(resultpath):
                filepath = os.path.join(resultpath, f'{port}.txt')
                with open(filepath, 'w', encoding='utf-8') as file1:
                    file1.write(resultcode)

            next_action = input('是否需要继续整理（y/n）')
            if next_action.lower() != 'y':
                break

    except Exception as e:
        print(f"发生异常：{e}")
#swaks批量发送
def swaks():
    path = input("请输入邮箱列表文件地址：")
    path1 = input("请输入邮件模板地址：")
    email = input("请输入伪造邮件地址：")
    for ok_mail in open(path):
        ok_mail = ok_mail.strip('\n')
        if ok_mail != None:
            with open(path1, 'r') as f:
                lines = f.readlines()
            with open('ok.eml', 'w') as n:
                n.write("To:"+ok_mail + "\n" + "**")
                n.writelines(lines)
                if n != None:
                    os.system("swaks --to "+ok_mail+" --from "+email+" --data ok.eml")
                    time.sleep(10)
                else:
                    pass
        else:
            exit()
#ip随机生成
def random_num1():
	num = random.randint(1, 254)
	return num
def random_num2():
	num = random.randint(0, 255)
	return num
def random_ip():
    ip_count = input("请填写需要生成的ip数量：")
    for j in range(int(ip_count)):
        ip = str(random_num1())+'.'+str(random_num2())+'.'+str(random_num2())+'.'+str(random_num2())
        print(ip)
#ip地址转换为c段地址
def iptoc():
    input_path = input("请输入ip文件地址：")
    output_path = input("结果保存地址（具体到文件名）：")
    try:
        with open(input_path, 'r') as fp, open(output_path, 'w') as fp1:
            for line in fp:
                ip = line.strip()
                octets = ip.split(".")
                c_segment = f"{octets[0]}.{octets[1]}.{octets[2]}.0/24"
                fp1.write(c_segment + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")
#去重
def qc():
    opath = input("请输入需要去重文件的路径(例如 d:\\xx\\w.txt)：")
    if not os.path.exists(opath):
        print("输入的去重文件路径不存在，请检查后重新输入")
        return
    try:
        with open(opath, "r", encoding='utf-8') as f3:
            original_content = [x.strip() for x in f3.readlines()]
            content = set(original_content)
            original_count = len(original_content)
        with open(opath, 'w', encoding='utf-8') as f:
            for line in content:
                f.write(line + '\n')

        print('去重前条数：', original_count)
        print('去重后条数：', len(content))
        print('成功保存文件到', opath)
    except Exception as e:
        print("发生异常：", e)
#文本排序
def sort_text():
    input_file= input("请输入需要排序文本的路径：")
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        sorted_lines = sorted(lines)  # 使用Python的sorted函数进行排序

    with open(input_file, 'w', encoding='utf-8') as file:
        for line in sorted_lines:
            file.write(line)
#secret随机密码生成

#主命令行参数解析
def parse_args():
    parser = argparse.ArgumentParser(description='描述：小公举~缝合怪，按需添加！')
    parser.add_argument('-g','--goby',help='处理goby资产~导出端口对应ip',action='store_true')
    parser.add_argument('-eb','--encodebase64',help='base64编码')
    parser.add_argument('-db','--decodebase64',help='base64解码')
    parser.add_argument('-md5','--md5',help='md5编码')
    parser.add_argument('-ip','--ip',help='随机生成ip',action='store_true')
    parser.add_argument('-ipt','--ipt',help='ipc段转化',action='store_true')
    parser.add_argument('-hex','--hex',help='16进制数据处理')
    parser.add_argument('-q','--quchong',help='文本去重',action='store_true')
    parser.add_argument('-s','--sort',help='文本排序',action='store_true')
    args = parser.parse_args()
    return args
#程序主运行函数
def main(args):
    actions = {
        "goby": gobyport,
        "encodebase64": enbase64,
        "decodebase64": debase64,
        "md5": enmd5,
        "ip": random_ip,
        "hex": hex,
        "quchong": qc,
        "sort": sort_text,
        "ipt": iptoc,
    }
    # 根据命令行参数调用相应的函数
    #items() 用于返回字典中所有的键值对（key-value），将每个键值对中的键赋值给变量 action，将值赋值给变量 function。
    for action, function in actions.items():
        if getattr(args, action):
            #检查当前函数是否有参数（在 Python 中，每个函数都有一个 __code__ 属性，它包含了函数的字节码、常量和其他一些相关信息。其中的 co_argcount 属性表示了函数定义时的参数个数。）
            if getattr(function, '__code__').co_argcount > 0:
                value = getattr(args, action)
                function(value)
            else:
            #如果函数不需要参数，就直接调用 function()
                function()

#运行流程
if __name__ == "__main__":
    main(parse_args())