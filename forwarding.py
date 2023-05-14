#tcp server
import socket
host = '127.0.0.1'          #Local Server IP
host2 = '127.0.0.1'   #Real Server IP
port = 8083 #Local Server Port
port2 = 7890 #Real Server Port
def ProcData(data):
    return data
    #add more code....
def run():
    print ("Map Server start from " + host + ":" + str(port) +" to " + host2 + ":" + str(port2) +"\r\n")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    print ("127.0.0.1 Server start at "+ str(port) +"\r\n")
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    client.connect((host2,port2))
    print (host +" Client connect to " + host2 + ":"+str(port2)+"\n")
    server.listen(5)
    ss, addr = server.accept()
    print ('got connected from',addr)

    msg = ss.recv(20480)
    print (msg)
    client.send(msg)
    buf=client.recv(20480)
    ss.send(buf)
    print(buf)
    server.close
    client.close
run()

