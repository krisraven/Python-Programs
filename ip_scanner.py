#!usr/bin/env python3
# scans wlan and returns all connected ip's
#improvement ideas: create way of breaking down ips's to return device makes as well

import re
import subprocess as sub
import scapy.all as scapy
# import optparse

def get_current_ip_range():
    ip_get = sub.check_output(["ip", "route"])
    ip_search = re.search(r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})/24", ip_get)
    return ip_search.group(0)

# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-t", "--target",
#                       dest="target",
#                       type="string",
#                       help="Target IP address")
#     (options, arguments) = parser.parse_args()
#     if options.target is None:
#         print("Please enter -t option with valid argument")
#         exit()
#     else:
#         return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast_signal = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast_signal/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(result_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

# option = get_arguments()
gathered_ip_range = get_current_ip_range()
ip_and_mac = scan(gathered_ip_range)
print_result(ip_and_mac)
