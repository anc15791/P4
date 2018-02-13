#!/bin/bash

if [ "$2" = "s1" ]
then
   dest_addr="10.10.2.1"
   dest_log="../history/s1.log"
fi


if [ "$2" = "s2" ]
then
   dest_addr="10.10.2.2"
   dest_log="../history/s2.log"
fi

if [ "$1" = "s1" ]
then
   src_addr="192.168.59.101"
   src_log="../history/s1.log"
fi

if [ "$1" = "s2" ]
then
   src_addr="192.168.59.102"
   src_log="../history/s2.log"
fi

while read full_cmd
do
   IFS='<' read -ra  cmd <<< "$full_cmd";
   command=../../../../bmv2/tools/runtime_CLI.py --thrift-port 9090 #'../runtime_CLI --thrift-ip '$dest_addr
   flows="${cmd[1]}"
   $command < $flows
   new_cmd=$command' < '$flows
   echo "$new_cmd" >> "$dest_log"
done < $src_log

#echo "`/bin/sh ./12_deactivate_fw.sh $1`"
#echo "`/bin/sh ./4_activate_fw.sh $2`"


rm -rf $src_log
touch $src_log


echo
echo "INFO: Migrating Firewall from "$src_addr" to "$dest_addr
