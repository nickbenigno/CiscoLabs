from netmiko import ConnectHandler

cisco_l2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.8.132',
    'username': 'user1',
    'password': 'pass',
    'port' : 22,          # optional, defaults to 22
    'secret': 'pass',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_l2)
config_command = ['debug all', 'y']
output = net_connect.send_config_set(config_command)
print (output)


config_command = ['int loop 0', 'ip address 69.69.69.69 255.255.255.255']
output = net_connect.send_config_set(config_command)
print (output)

for i in range (1,100):
    config_command = ['vlan ' + str(i), 'name netmiko_VLAN ' + str(i)]
    output = net_connect.send_config_set(config_command)
    print (output)