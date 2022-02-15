#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, PhysDomain, Context, NetworkPool, Node

# Connection
# session = Session("https://10.10.20.14", "admin", "C1sco12345")
session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
session.login()

url = "/api/node/mo/uni/tn-tenant_public/ap-ap1_public/epg-my_epg2/rspathAtt-[topology/pod-1/paths-101/pathep-[eth1/40]].json"
data = {
    "fvRsPathAtt": {
        "attributes": {
            "dn": "uni/tn-tenant_public/ap-ap1_public/epg-my_epg2/rspathAtt-[topology/pod-1/paths-101/pathep-[eth1/40]]",
            "status": "deleted"
        },
        "children": []
    }
}
resp = session.push_to_apic(url=url, data=data)
if not resp.ok:
    print("Fail")
else:
    print("Success")

print("dir: {}".format(dir(resp)))
print("type: {}".format(type(resp.text)))
print("content: {}".format(resp.text))