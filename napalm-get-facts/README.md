# Napalm get_facts
```yaml
$ apb napalm-get-facts.yml --ask-pass
SSH password: 

PLAY [eos] **************************************************************************************************************************************************

TASK [napalm get_facts] *************************************************************************************************************************************
ok: [leaf-1.test]
ok: [leaf-2.test]
ok: [spine-2.test]
ok: [spine-1.test]

TASK [debug] ************************************************************************************************************************************************
ok: [spine-1.test] => 
  napalm_facts:
    fqdn: spine-1
    hostname: spine-1
    interface_list:
    - Ethernet1
    - Ethernet2
    - Ethernet3
    - Ethernet4
    - Ethernet5
    - Ethernet6
    - Ethernet7
    - Ethernet8
    - Management1
    model: vEOS
    os_version: 4.25.0FX-LDP-RSVP-18741113.4250FXLDPRSVP
    serial_number: ''
    uptime: 574
    vendor: Arista
ok: [leaf-2.test] => 
  napalm_facts:
    fqdn: leaf-2
    hostname: leaf-2
    interface_list:
    - Ethernet1
    - Ethernet2
    - Ethernet3
    - Ethernet4
    - Ethernet5
    - Ethernet6
    - Ethernet7
    - Ethernet8
    - Management1
    model: vEOS
    os_version: 4.25.0FX-LDP-RSVP-18741113.4250FXLDPRSVP
    serial_number: ''
    uptime: 573
    vendor: Arista
ok: [leaf-1.test] => 
  napalm_facts:
    fqdn: leaf-1
    hostname: leaf-1
    interface_list:
    - Ethernet1
    - Ethernet2
    - Ethernet3
    - Ethernet4
    - Ethernet5
    - Ethernet6
    - Ethernet7
    - Ethernet8
    - Management1
    model: vEOS
    os_version: 4.25.0FX-LDP-RSVP-18741113.4250FXLDPRSVP
    serial_number: ''
    uptime: 575
    vendor: Arista
ok: [spine-2.test] => 
  napalm_facts:
    fqdn: spine-2
    hostname: spine-2
    interface_list:
    - Ethernet1
    - Ethernet2
    - Ethernet3
    - Ethernet4
    - Ethernet5
    - Ethernet6
    - Ethernet7
    - Ethernet8
    - Management1
    model: vEOS
    os_version: 4.25.0FX-LDP-RSVP-18741113.4250FXLDPRSVP
    serial_number: ''
    uptime: 572
    vendor: Arista

PLAY RECAP **************************************************************************************************************************************************
leaf-1.test                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
leaf-2.test                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
spine-1.test               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
spine-2.test               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```