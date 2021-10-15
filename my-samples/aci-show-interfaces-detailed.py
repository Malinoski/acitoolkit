#!/usr/bin/env python
import json
from typing import List

from acitoolkit import Session, Pod, Interface, Node, Linecard

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Pods
pods: List[Pod] = Pod.get(session)
for pod in pods:
    print("# Pod", "name:{}".format(pod.name), "type:{}".format(pod.type))

    # Nodes
    nodes: List[Node] = Node.get(session, pod)
    for node in nodes:
        print(" ", "# Node",  "name:{}".format(node.name), "role:{}".format(node.role))

        # Linecards
        linecards: List[Linecard] = Linecard.get(session, node)
        for linecard in linecards:
            print("  ", "# Linecard", "name:{}".format(linecard.name))

            # Interfaces
            interfaces: List[Interface] = Interface.get(session, linecard)
            for interface in interfaces:
                print("   ", "# Interface {}".format(json.dumps(interface.attributes, indent=4)))
