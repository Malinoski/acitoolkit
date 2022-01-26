from typing import List
from requests.models import Response
from acitoolkit import Session, Pod, Interface, Node, Linecard

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")
resp: Response = session.login()
print(type(resp))
if not resp.ok:
    print('%% Could not login to APIC')

# Pods
pods: List[Pod] = Pod.get(session)
for pod in pods:
    print('\nPOD - {}'.format(pod.name))
    # Nodes
    nodes: List[Node] = Node.get(session, pod)
    for node in nodes:
        print('\nNODE - name:{}'.format(node.name))
        # Filter
        if node.role == "leaf":

            # Linecards
            linecards: List[Linecard] = Linecard.get(session, node)
            for linecard in linecards:

                # Interfaces
                interfaces: List[Interface] = Interface.get(session, linecard)
                for interface in interfaces:
                    print('\nINTERFACE:{}'.format(interface.name))
                    if 'discovery' in interface.attributes['usage']:

                        print("AVAILABLE: {}".format(interface.attributes))
