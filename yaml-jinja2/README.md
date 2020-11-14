## Exercise 1
```bash
$ python render.py ex1
hostname leaf-1
!
interface loopback 0
    ip address 192.192.252.1 255.255.255.0
!
banner motd #
UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED

You must have explicit, authorized permission to access or configure this
device.Unauthorized attempts and actions to access or use this system may
result in civil and/or criminal penalties.
All activities performed on this device are logged and monitored.

#
```
## Exercise 2
```bash
$ python render.py ex2
hostname leaf-1
!
interface loopback 0
    ip address 192.168.252.1 255.255.255.255
!
interface 1/1/1
    no shutdown
interface 1/1/2
    no shutdown
interface 1/1/3
    no shutdown
interface 1/1/4
    no shutdown
interface 1/1/48
    no shutdown
```
## Exercise 3
```bash
$ python render.py ex3
leaf-1.netletic.test ansible_user=cisco ansible_ssh_pass=cisco
leaf-2.netletic.test ansible_user=cisco ansible_ssh_pass=cisco
spine-1.netletic.test ansible_user=cisco ansible_ssh_pass=cisco
spine-2.netletic.test ansible_user=cisco ansible_ssh_pass=cisco
```
## Exercise 4
```bash
$ python render.py ex4
admin password placeholder
helpdesk password placeholder
```
## Exercise 5
```bash
$ python render.py ex5
username admin password placeholder
username admin privilege 15
username admin autocommand show version
username helpdesk password placeholder
username helpdesk privilege 2
username helpdesk autocommand show interface status
username rescue password placeholder
username rescue privilege 15
```
## Exercise 6
```bash
$ python render.py ex6
router bgp 64000
    neighbor 1.1.1.1 remote-as 65401
    neighbor 1.1.1.1 description telenet
    no neighbor 2.2.2.2
    neighbor 3.3.3.3 shutdown
    neighbor 4.4.4.4 remote-as 65404
    neighbor 4.4.4.4 description belnet
    neighbor 5.5.5.5 remote-as 65405
    neighbor 5.5.5.5 description bnix
    neighbor 5.5.5.5 route-map INCR_HOP_COUNT_BY_2
```
## Exercise 7
```bash
$ python render.py ex7
!
ip prefix-list bgp-neighbor-4.4.4.4 seq 10 permit 4.4.4.0/24
ip prefix-list bgp-neighbor-4.4.4.4 seq 20 permit 8.8.8.0/23
ip prefix-list bgp-neighbor-5.5.5.5 seq 10 permit 5.5.5.0/21
!
router bgp 64000
    neighbor 1.1.1.1 remote-as 65401
    neighbor 1.1.1.1 description telenet
    !
    no neighbor 2.2.2.2
    !
    neighbor 3.3.3.3 shutdown
    !
    neighbor 4.4.4.4 remote-as 65404
    neighbor 4.4.4.4 description belnet
    neighbor 4.4.4.4 prefix-list bgp-neighbor-4.4.4.4 in
    !
    neighbor 5.5.5.5 remote-as 65405
    neighbor 5.5.5.5 description bnix
    neighbor 5.5.5.5 route-map incr-hop-count-by-2
    neighbor 5.5.5.5 prefix-list bgp-neighbor-5.5.5.5 in
    !
    end
```
## Exercise 8
```bash
$ python render.py ex8
hostname ir-1
!
interface loopback 0
    ip address 192.168.252.1 255.255.255.0
!
banner motd #
UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED

You must have explicit, authorized permission to access or configure this
device.Unauthorized attempts and actions to access or use this system may
result in civil and/or criminal penalties.
All activities performed on this device are logged and monitored.

#
!
ip prefix-list bgp-neighbor-4.4.4.4 seq 10 permit 4.4.4.0/24
ip prefix-list bgp-neighbor-4.4.4.4 seq 20 permit 8.8.8.0/23
ip prefix-list bgp-neighbor-5.5.5.5 seq 10 permit 5.5.5.0/21
!
router bgp 64000
    neighbor 1.1.1.1 remote-as 65401
    neighbor 1.1.1.1 description telenet
    !
    no neighbor 2.2.2.2
    !
    neighbor 3.3.3.3 shutdown
    !
    neighbor 4.4.4.4 remote-as 65404
    neighbor 4.4.4.4 description belnet
    neighbor 4.4.4.4 prefix-list bgp-neighbor-4.4.4.4 in
    !
    neighbor 5.5.5.5 remote-as 65405
    neighbor 5.5.5.5 description bnix
    neighbor 5.5.5.5 route-map incr-hop-count-by-2
    neighbor 5.5.5.5 prefix-list bgp-neighbor-5.5.5.5 in
    !
    end
!
interface 1/1/1
    ip address 10.24.1.1 255.255.255.0
    no shutdown
interface 1/1/2
    ip address 10.24.2.1 255.255.255.0
    no shutdown
```
## Exercise 9
### Node E1
```bash
$ python render.py ex9
hostname E1
!
interface loopback 0
    ip address 192.168.0.2 255.255.255.255 
!
interface GigabitEthernet0/0
    ip address 172.16.1.110 255.255.255.255
!
interface GigabitEthernet0/2
    ip address 10.0.0.21 255.255.255.252
    no shutdown
    ip ospf 1 area 0
interface GigabitEthernet0/1
    ip address 10.0.0.13 255.255.255.252
    no shutdown
    ip ospf 1 area 0

!
router ospf 1
    router-id 192.168.0.2
```
### Node E2
```bash
$ python render.py ex9
hostname E2
!
interface loopback 0
    ip address 192.168.0.4 255.255.255.255 
!
interface GigabitEthernet0/0
    ip address 172.16.1.111 255.255.255.240
!
interface GigabitEthernet0/1
    ip address 10.0.0.17 255.255.255.252
    no shutdown
    ip ospf 1 area 0

!
router ospf 1
    router-id 192.168.0.4
```