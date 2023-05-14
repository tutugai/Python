import os
import time

for ok_mail in open("22.txt"):
    ok_mail = ok_mail.strip('\n')
    if ok_mail != None:
        with open('name.eml', 'r') as f:
            lines = f.readlines()
    
        with open('ok.eml', 'w') as n:
            n.write("To:"+ok_mail + "\n" + "**")
            n.writelines(lines)
            if n != None:
                os.system("swaks --to "+ok_mail+" --from admin@xxx.com.cn"+" --data ok.eml")
                time.sleep(10)
            else:
                 pass
    else:
        exit()