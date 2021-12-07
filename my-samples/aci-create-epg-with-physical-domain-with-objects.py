#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, PhysDomain


def main():

    session = Session("https://10.10.20.14", "admin", "C1sco12345")
    session.login()

    tenant = Tenant('tenantA')
    app = AppProfile('apA', tenant)
    bd = BridgeDomain('bdA', tenant)
    epg = EPG("epgG", app)
    epg.add_bd(bd)

    resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)

    # TODO:
    # physical_domain_name = "phys"
    # pd = PhysDomain(physical_domain_name)
    # pd.add_child(epg)
    # resp = session.push_to_apic(pd.get_url(), pd.get_json())
    # if not resp.ok:
    #     print('%% Error: Could not push configuration to APIC')
    #     print(resp.text)
    

if __name__ == '__main__':
    main()
