#!/bin/bash

if [ "$1" = "s1" ]
then
   addr="10.10.2.1"
fi

if [ "$1" = "s2" ]
then
   addr="10.10.2.2"
fi

if [ "$1" = "s3" ]
then
   addr="10.10.4.2"
fi

../../../../bmv2/tools/runtime_CLI.py --thrift-port 9090 < ../flows/deactivate_fw.rules
#../runtime_CLI --thrift-ip $addr < ../flows/deactivate_fw.rules

echo "INFO: Deactivating firewall in switch $addr"
