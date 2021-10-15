#!/usr/bin/env python
import json
from typing import List

from acitoolkit import Session, Pod, Interface, Node, Linecard

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Interfaces
interfaces_result: List[Interface] = []

# Pods
pods: List[Pod] = Pod.get(session)
for pod in pods:

    # Nodes
    nodes: List[Node] = Node.get(session, pod)
    for node in nodes:

        # Filter
        if node.role == "leaf":

            # Linecards
            linecards: List[Linecard] = Linecard.get(session, node)
            for linecard in linecards:

                # Interfaces
                interfaces: List[Interface] = Interface.get(session, linecard)
                for interface in interfaces:
                    print("Adding interface ### ", "{} ### ".format(interface), "attributes:{} #### ".format(interface.attributes))
                    interfaces_result.append(interface)

for interface_result in interfaces_result:
    print("RESUT:", interface_result)

