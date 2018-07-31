# Python 3.6.5
# By: Francisco Rojo, 30/7/2018
# Cisco BB Level 1 _assignment
# 
# How to run on Python3
# > python3 <file>.py

import json
import os

_path = os.path.abspath(os.path.dirname(__file__))
print (_path)

with open(os.path.join(_path, "bblevel1_interfaces.json"), mode = "r") as file:
    json_in = json.loads(file.read())

for interface in json_in["ietf-interfaces:interfaces"]["interface"]:
        name=interface["name"]
        ip=interface["ietf-ip:ipv4"]["address"][0]["ip"]
        netmask=interface["ietf-ip:ipv4"]["address"][0]["netmask"]
        print (name,":",ip,netmask)

#    print("{name}: {ip} {netmask}".format(
#        name=interface["name"],
#        ip=interface["ietf-ip:ipv4"]["address"][0]["ip"],
#        netmask=interface["ietf-ip:ipv4"]["address"][0]["netmask"],
#    ))