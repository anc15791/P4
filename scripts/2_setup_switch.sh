#!/bin/bash

if [ "$1" = "s1" ]
then
   addr="10.10.1.2"
   flows="../flows/setup_switch_s1_4sw_new.rules"
   log="../history/s1.log"
fi

if [ "$1" = "s2" ]
then
   addr="10.10.2.2"
   flows="../flows/setup_switch_s2_4sw.rules"
   log="../history/s2.log"
fi

if [ "$1" = "s3" ]
then
   addr="10.10.4.2"
   flows="../flows/setup_switch_s3_4sw_new.rules"
   log="../history/s3.log"
fi

if [ "$1" = "s4" ]
then
   addr="192.168.59.103"
   flows="../flows/setup_switch_s4_4sw.rules"
   log="../history/s4.log"
fi

   rm -rf $log
   touch $log
   cmd='../../../../bmv2/tools/runtime_CLI.py --thrift-port 9090' #--thrift-ip '$addr'
   $cmd < $flows
   #full_cmd=$cmd' < '$flows
   #echo "$full_cmd" > "$log"

echo "INFO: Setting up switch" #$addr
