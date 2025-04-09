from netmiko import ConnectHandler

menu = -1

device = {
    "device_type": "cisco_ios_serial",
    "serial_settings": {"port": "COM1"},
}

with ConnectHandler(**device) as net_connect:
    def test_connection():
        output = net_connect.send_command("show ip int brief")
        return output

    def write_ip_int():
        interface = input("Enter interface: ")
        ip_addr = input("Enter ip address: ")
        ip_subnet_mask = input("Enter subnet mask: ")
        output = net_connect.send_command("conf t ")
        output += net_connect.send_command("int " + interface)
        output += net_connect.send_command("ip address " + ip_addr + ip_subnet_mask)
        output += net_connect.send_command("exit")
        return output

while menu != 0:
    print("Options\n\t1. Test connection\n\t2. Write ip address to specified interface")
    menu = int(input("Enter option: "))

    if menu == 1:
        output = test_connection()
        print(f"\n{output}\n")
    elif menu == 2:
        output = write_ip_int()
        print(f"\n{output}\n")
    elif menu != 0:
        print("Invalid option, please try again")

print("\nExiting...")