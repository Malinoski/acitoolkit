#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, Context

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")
session.login()

tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    apps = AppProfile.get(session, tenant)
    for app in apps:
        epgs = EPG.get(session, app, tenant)
        for epg in epgs:
            print(epg)


