#!/bin/bash

addr="192.168.59.101"
flows="../flows/setup_switch_s1_4sw.rules"
log="../history/s1.log"
rm -rf $log
touch $log
cmd='../runtime_CLI --thrift-ip '$addr' --thrift-port 9090' 
$cmd < $flows
echo "INFO: Setting up switch $addr"




addr="192.168.59.102"
flows="../flows/setup_switch_s2_4sw.rules"
log="../history/s2.log"
rm -rf $log
touch $log
cmd='../runtime_CLI --thrift-ip '$addr' --thrift-port 9090' 
$cmd < $flows
echo "INFO: Setting up switch $addr"



addr="192.168.59.104"
flows="../flows/setup_switch_s3_4sw.rules"
log="../history/s3.log"
rm -rf $log
touch $log
cmd='../runtime_CLI --thrift-ip '$addr' --thrift-port 9090' 
$cmd < $flows
echo "INFO: Setting up switch $addr"
