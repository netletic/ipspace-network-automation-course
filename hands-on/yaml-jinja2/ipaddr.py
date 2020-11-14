from ansible_collections.ansible.netcommon.plugins.filter.ipaddr import ipaddr


mgmt = "172.16.1.111 255.255.255.240"

print(ipaddr(mgmt))