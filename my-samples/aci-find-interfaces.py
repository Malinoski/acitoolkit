from pprint import pprint
from typing import List
from requests.models import Response
from acitoolkit import Session, Pod, Interface, Node, Linecard, VmmDomain

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")

resp: Response = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Pods
pods: List[Pod] = Pod.get(session)
print(pods)
for pod in pods:
    print('\n# POD - {}'.format(pod.name))
    # Nodes
    nodes: List[Node] = Node.get(session, pod)
    for node in nodes:

        # Filter
        if node.role == "leaf":
            print('\n# LEAF - name:{}'.format(node.name))

            # Linecards
            linecards: List[Linecard] = Linecard.get(session, node)
            for linecard in linecards:

                # Interfaces
                interfaces: List[Interface] = Interface.get(session, linecard)
                for interface in interfaces:
                    print('\n# INTERFACE')
                    print('name: {}'.format(interface.name))
                    print('id: {}'.format(interface.id))
                    print('dn: {}'.format(interface.dn))
                    print('pod: {}'.format(interface.pod))
                    print('port: {}'.format(interface.port))
                    print('module: {}'.format(interface.module))
                    print('node: {}'.format(interface.node))
                    print('type: {}'.format(interface.type))
                    print('descr: {}'.format(interface.descr))
                    print('if_name: {}'.format(interface.if_name))
                    print('adminstatus: {}'.format(interface.adminstatus))
                    print('interface_type: {}'.format(interface.interface_type))
                    print('json {}'.format(interface.get_json()))
                    print('attributes: {}'.format(interface.attributes))
