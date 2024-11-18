#!/usr/bin/env/python

import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    print(f"[+] Changing mac address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--interface",
        dest="interface",
        help="Specify interface you want to change MAC address to.",
    )
    parser.add_option(
        "-m",
        "--mac",
        dest="new_mac",
        help="Enter the new mac address you want to assign to the interface.",
    )

    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface. Go to help for more details.")
    elif not options.new_mac:
        parser.error("[-] Please specify new MAC address. Go to help for more details.")
    return options

def get_new_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if new_mac:
        return new_mac.group(0)
    else:
        print("[-] Couldn't find the MAC address.")


options = get_arguments()
change_mac(options.interface, options.new_mac)
current_mac = get_new_mac(options.interface)
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to {current_mac}")
else:
    print("[-] MAC address did not get changed.")
print(str(current_mac))