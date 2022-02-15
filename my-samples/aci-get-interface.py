from requests.models import Response
from acitoolkit import Session, Interface

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")

resp: Response = session.login()
print(type(resp))
if not resp.ok:
    print('%% Could not login to APIC')

interfaces: [Interface] = Interface.get(
    session,
    node='101',
    pod_parent='1',
    port='31',
    module='1')
print(interfaces[0].attributes)


