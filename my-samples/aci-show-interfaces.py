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
for pod in pods:
    print('# POD:')
    print('name: {}'.format(pod.name))

    # Nodes
    nodes: List[Node] = Node.get(session, pod)
    for node in nodes:

        # Filter
        if node.role == "leaf":
            print('\t# LEAF')
            print('\tname: {}'.format(node.name))

            # Linecards
            linecards: List[Linecard] = Linecard.get(session, node)
            for linecard in linecards:

                # Interfaces
                interfaces: List[Interface] = Interface.get(session, linecard)
                for interface in interfaces:
                    print('\t\t# INTERFACE')
                    print('\t\tname: {}'.format(interface.name))
                    print('\t\tid: {}'.format(interface.id))
                    print('\t\tdn: {}'.format(interface.dn))
                    print('\t\tpod: {}'.format(interface.pod))
                    print('\t\tport: {}'.format(interface.port))
                    print('\t\tmodule: {}'.format(interface.module))
                    print('\t\tnode: {}'.format(interface.node))
                    print('\t\ttype: {}'.format(interface.type))
                    print('\t\tdescr: {}'.format(interface.descr))
                    print('\t\tif_name: {}'.format(interface.if_name))
                    print('\t\tadminstatus: {}'.format(interface.adminstatus))
                    print('\t\tinterface_type: {}'.format(interface.interface_type))
                    print('\t\tjson {}'.format(interface.get_json()))
                    print('\t\tattributes: {}'.format(interface.attributes))
