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

    tn.write(b"conf t\n")

    for i in range(2, 11): 
        tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
        tn.write(b"name VLAN_" + str(i).encode('ascii') + b"\n") 
    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))