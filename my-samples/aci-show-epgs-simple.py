#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, EPG

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")

session.login()

tenants: [Tenant] = Tenant.get(session)
for tenant in tenants:
    print("# Tenant:")
    print("name: {}".format(tenant.name))

    apps: [AppProfile] = AppProfile.get(session, tenant)
    for app in apps:
        print("\t# Application Profile:")
        print("\tname: {}".format(app.name))

        epgs: [EPG] = EPG.get(session, app, tenant)
        for epg in epgs:
            print("\t\t# EPG:")
            print("\t\tname: {}".format(epg.name))


