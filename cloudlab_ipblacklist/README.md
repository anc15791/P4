Implementing Basic IP blacklisting


Introduction

Objective of this exercise is to implement a basic IP blacklisting
functionality. For this to work the switch must perform the basic operations of
IPv4 forwarding like (i) update the source and destination MAC addresses,
(ii) decrement the time-to-live (TTL) in the IP header, and (iii) forward the
packet out the appropriate port.
Apart from these functionalities the switch should also check the destination mac address against a list of blacklisted IPs and if allow only non-blacklisted IPs to go through.

Code Breakdown


We perform above operations by using 4 tables:
1. ipv4_lpm: 
2. forward:
3. send_frame:
4. firewall: 

There are two control blocks:
1. ingress:
2. egress:

Other Program Blocks:
1. Headers:
2. Parser:
3. Deparser:

Flow of Execution:

Flow Entries:
1. table_set_default
2. table_add
3. table_modify

Thrift Controller:
1. Running the CLI:
2. Useful commands:


Steps to Execute

1. Compile:
2. Start the topology:
3. Push Table entries:
4. Test:
5. Update table Entries:
6. Test:
7. Analyze: 
8. Cleanup:



