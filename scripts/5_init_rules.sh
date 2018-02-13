#!/bin/bash

if [ "$1" = "s1" ]
then
   addr="10.10.1.2"
   log="../history/s1.log"
fi

if [ "$1" = "s2" ]
then
   addr="10.10.2.2"
   log="../history/s2.log"
fi

if [ "$1" = "s3" ]
then
   addr="10.10.4.2"
   log="../history/s3.log"
fi

cmd='../../../../bmv2/tools/runtime_CLI.py --thrift-port 9090'  #'../runtime_CLI --thrift-ip '$addr
flows='../flows/init.rules'

$cmd < $flows
full_cmd=$cmd' < '$flows

echo "$full_cmd" >> "$log"

echo "INFO: Enabling ICMP Check in the firewall of the switch $addr"
echo "INFO: Enabling TCP Check in the firewall of the switch $addr"
echo "INFO: Enabling UDP Check in the firewall of the switch $addr"
