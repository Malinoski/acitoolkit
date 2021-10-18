import json
import sys
import acitoolkit.acitoolkit as ACI

# session = ACI.Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
session = ACI.Session("https://10.10.20.14", "admin", "C1sco12345")
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')
    sys.exit(0)

# Download all of the interfaces
data = []
interfaces = ACI.Interface.get(session)
for interface in interfaces:
    print("{}".format(json.dumps(interface.attributes, indent=4)))
    data.append((interface.attributes['if_name'],
                 interface.attributes['porttype'],
                 interface.attributes['adminstatus'],
                 interface.attributes['operSt'],
                 interface.attributes['operSpeed'],
                 interface.attributes['mtu'],
                 interface.attributes['usage']))

# Display the some data as table
template = "{0:17} {1:6} {2:^6} {3:^6} {4:7} {5:6} {6:9} "
print(template.format("INTERFACE", "TYPE", "ADMIN", "OPER", "SPEED", "MTU", "USAGE"))
print(template.format("---------", "----", "------", "------", "-----", "___", "---------"))
for rec in data:
    print(template.format(*rec))


