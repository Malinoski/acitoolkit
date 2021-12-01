#!/usr/bin/env python
from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, PhysDomain


def main():

    session = Session("https://10.10.20.14", "admin", "C1sco12345")
    session.login()

    physical_domain_name = "phys"
    ap_name = "apA"
    tenant_name = "tenantA"
    epg_name = "epgA"

    # Create Tenant, AP and EPG
    tenant = Tenant(tenant_name)
    app = AppProfile(ap_name, tenant)
    epg = EPG(epg_name, app)
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
