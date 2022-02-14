from acitoolkit import Session, Tenant, AppProfile, EPG, Interface, L2Interface, BridgeDomain, Node, Context

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")

resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Data
tenant_name = 'tenant_public'
ap_name = 'ap1_public'
epg_name = 'my_epg1'
physical_domain_name = "SnV_phys"  # pool 100-199

# Create the Tenant, App Profile, and EPG
tenant = Tenant(tenant_name)
app = AppProfile(ap_name, tenant)
bd = BridgeDomain('bd_public', tenant)
vrf = Context('vrf_public', tenant)
bd.add_context(vrf)
epg = EPG(epg_name, app)
epg.add_bd(bd)

# Create EPG in APIC
resp = tenant.push_to_apic(session)
if not resp.ok:
    print('Error: Could not create EPG: {}'.format(resp))
    exit()

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
            # "status": "created"
          },
          "children": []
        }
      }
    ]
  }
}
resp = session.push_to_apic(url, json)
if not resp.ok:
    print('Error: Could not set Physical Domain to EPG')
    exit()

# Set and attach interface to EPG
intf = Interface(interface_type='eth', pod='1', node='101', module='1', port='31')
free_vlan = "103"
vlan_intf = L2Interface(
    name='some_name',
    encap_type='vlan',  # mode access 802.1P
    encap_id=free_vlan,
    encap_mode='native'
)
vlan_intf.attach(intf)
epg.attach(vlan_intf)
epg.set_deployment_immediacy("immediate")
resp = tenant.push_to_apic(session)
if not resp.ok:
    print('Error: Could not attach interface: {}'.format(resp))
    exit()

# resp = intf.push_to_apic(session)
# if not resp.ok:
#     print('Error: Could not push interface configuration to APIC')
#     print("{}".format(dir(resp)))
#     print("{}".format(resp.reason))
#     print("{}".format(resp.text))
# else:
#     print("{}".format(resp.text))

