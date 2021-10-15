#!/usr/bin/env python
import json

from acitoolkit import Session, Pod, Interface, Node, Linecard

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

pod: Pod = Pod("1")
node: Node = Node("101")  # Can be leaf, spine or controller
module: Linecard = Linecard("1")

# Verbose params
pod_string_id: str = pod.pod
node_name = node.name
module_string_id = module.pod
port_string_number = "1"  # must be string

# Note: pod.pod is the number of pod (ex.: 1)
interfaces = Interface.get(session, pod_string_id, node_name, module_string_id, port_string_number)

data = []
for interface in interfaces:

    data.append((interface.attributes['if_name'],
                 interface.attributes['porttype'],
                 interface.attributes['adminstatus'],
                 interface.attributes['operSt'],
                 interface.attributes['operSpeed'],
                 interface.attributes['mtu'],
                 interface.attributes['usage'],))

# Display the data downloaded
template = "{0:17} {1:6} {2:^6} {3:^6} {4:7} {5:6} {6:9} "
print(template.format("INTERFACE", "TYPE", "ADMIN", "OPER", "SPEED", "MTU", "USAGE"))
print(template.format("---------", "----", "------", "------", "-----", "___", "---------"))
for rec in data:
    print(template.format(*rec))




