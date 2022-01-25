from acitoolkit import Session, Tenant, AppProfile, EPG, Interface, L2Interface, BridgeDomain, Node

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
# session = Session("https://10.10.20.14", "admin", "C1sco12345")

resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Create the Tenant, App Profile, and EPG
tenant = Tenant('tenant_public')
app = AppProfile('ap1_public', tenant)
# bd = BridgeDomain('db_public', tenant)
epg = EPG('my_epg1', app)
# epg.add_bd(bd)

# Get interface (p.s.: node can bve a leaf, and module is a linecard)
intf = Interface(interface_type='eth', pod='1', node='101', module='1', port='2')

# Set a free VLAN, including mode access 802.1P (encap_mode='native') and encapsulation mode 5 (encap_id='5')
free_vlan = "101"  # TODO: Get a free VLAN in APIC (or in NetworkAPI/environments).
intf_name_no_space = intf.name.replace(" ", "")  # exp.: eth1/101/1/1
vlan_intf = L2Interface(
    name='vlan{}_on_interface_{}'.format(free_vlan, intf_name_no_space),
    encap_type='vlan',
    encap_id=free_vlan,
    encap_mode='native'
)
vlan_intf.attach(intf)

# Attach the Interface and VLAN configuration to EPG
epg.attach(vlan_intf)
epg.set_deployment_immediacy("immediate")

# Push configuration to the APIC
resp = tenant.push_to_apic(session)
if not resp.ok:
    print('Error: Could not push tenant configuration to APIC')

# Push the interface attachment to the APIC
resp = intf.push_to_apic(session)
if not resp.ok:
    print('Error: Could not push interface configuration to APIC')
    print("{}".format(dir(resp)))
    print("{}".format(resp.reason))
    print("{}".format(resp.text))
else:
    print("{}".format(resp.text))

