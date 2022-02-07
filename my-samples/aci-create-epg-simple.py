#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, Context

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")

session.login()

tenant = Tenant('TN-DEV')
app = AppProfile('AP1-DEV', tenant)
vrf = Context('VRF-DEV', tenant)
bd = BridgeDomain('BD-DEV', tenant)
bd.add_context(vrf)

epg = EPG('epg001', app)
epg.add_bd(bd)
resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
if not resp.ok:
    print('%% Error: Could not push configuration to APIC')
    print(resp.text)
