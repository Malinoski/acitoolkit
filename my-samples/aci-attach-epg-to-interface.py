from acitoolkit import Session, Tenant, AppProfile, EPG, Interface, L2Interface

session = Session("https://10.10.20.14", "admin", "C1sco12345")
# session = ACI.Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")

resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Create the Tenant, App Profile, and EPG
tenant = Tenant('tenantA')
app = AppProfile('apA', tenant)
epg = EPG('epg1', app)

# Create the physical interface object
# Obs.:
INTERFACE = {'type': 'eth',
             'pod': '1',
             'node': '101',
             'module': '1',
             'port': '39'}
intf = Interface(INTERFACE['type'],
                 INTERFACE['pod'],
                 INTERFACE['node'],
                 INTERFACE['module'],
                 INTERFACE['port'])

# Create a VLAN interface and attach to the physical interface
VLAN = {'name': 'my_vlan123',
        'encap_type': 'vlan',
        'encap_id': '5'}  # ??????????????????????????????
vlan_intf = L2Interface(VLAN['name'],
                        VLAN['encap_type'],
                        VLAN['encap_id'])
vlan_intf.attach(intf)

# Attach the EPG to the VLAN interface
epg.attach(vlan_intf)

# Push the tenant config to the APIC
resp = tenant.push_to_apic(session)
if not resp.ok:
    print('%% Error: Could not push tenant configuration to APIC')

# Push the interface attachment to the APIC
resp = intf.push_to_apic(session)
if not resp.ok:
    print('%% Error: Could not push interface configuration to APIC')
