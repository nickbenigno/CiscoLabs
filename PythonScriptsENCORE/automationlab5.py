"""Python Get Scripts"""

import getpass
import telnetlib


user = input("Enter your telnet user: ")
password = getpass.getpass()

f = open('myswitches')

for ip in f: 
    ip = ip.strip()
    host = ip
    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch" + host, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.close
    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))