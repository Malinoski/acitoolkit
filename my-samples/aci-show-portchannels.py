import json
from typing import List
from acitoolkit import Session, Pod, Interface, Node, Linecard, ConcreteVpc, ConcreteVpcIf, PortChannel

# session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
session = Session("https://10.10.20.14", "admin", "C1sco12345")
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

pcs: List[PortChannel] = PortChannel.get(session)
for pc in pcs:
    print("name:{} dn:{} node:{} port:{}".format(pc.name, pc.dn, pc.node, pc.port))
    print(json.dumps(pc.get_json(), indent=4, sort_keys=True))
