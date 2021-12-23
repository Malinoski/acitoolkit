#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, PhysDomain, Context, NetworkPool, Node


def main():

    # Connection
    # session = Session("https://10.10.20.14", "admin", "C1sco12345")
    session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")

    session.login()

    # Names
    physical_domain_name = "SnV_phys"  # pool 100-199
    tenant_name = "tenantA"
    ap_name = "apA"
    bd_name = "bdA"
    epg_name = "epgA"

    # Create environment
    tenant = Tenant(tenant_name)
    app = AppProfile(ap_name, tenant)
    vrf = Context('vrfA', tenant)
    bd = BridgeDomain(bd_name, tenant)
    bd.add_context(vrf)

    epg = EPG(epg_name, app)
    epg.add_bd(bd)
    resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)

    # Associate EPG to a Physical Domain
    url = "/api/mo/uni/tn-{}/ap-{}/epg-{}.json".format(tenant_name, ap_name, epg_name)
    json = {
      "fvAEPg": {
        "attributes": {
          "dn": "uni/tn-{}/ap-{}/epg-{}".format(tenant_name, ap_name, epg_name),
          "name": epg_name,
          "rn": "epg-{}".format(epg_name)
        },
        "children": [
          {
            "fvRsDomAtt": {
              "attributes": {
                "tDn": "uni/phys-{}".format(physical_domain_name),
                "status": "created"
              },
              "children": []
            }
          }
        ]
      }
    }
    resp = session.push_to_apic(url, json)

    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)


if __name__ == '__main__':
    main()
