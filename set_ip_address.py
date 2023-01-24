import subprocess

# Set the IP address
ip_address = "192.168.1.10"
subnet_mask = "255.255.255.0"
default_gateway = "192.168.1.1"

# Set the interface name
interface_name = "wlan0"

# Set the IP address
subprocess.run(["ifconfig", interface_name, ip_address, "netmask", subnet_mask])

# Set the default gateway
subprocess.run(["route", "add", "default", "gw", default_gateway, interface_name])
