from netmiko import ConnectHandler

cisco_l2_sw1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.8.207',
    'username': 'user1',
    'password': 'pass'
}

cisco_l2_sw2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.8.133',
    'username': 'user1',
    'password': 'pass'
}

cisco_l2_sw3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.8.177',
    'username': 'user1',
    'password': 'pass'
}

list_of_devices = [cisco_l2_sw1, cisco_l2_sw2, cisco_l2_sw3]

for device in list_of_devices: 
    net_connect = ConnectHandler(**device)
    for i in range (1,100):
        config_command = ['vlan ' + str(i), 'name netmiko_VLAN ' + str(i)]
        output = net_connect.send_config_set(config_command)
        print (output)