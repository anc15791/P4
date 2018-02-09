#!/bin/bash

addr="192.168.59.101"
flows="../flows/setup_switch_s1_4sw_topo_mov.rules"
log="../history/s1.log"
rm -rf $log
touch $log
cmd='usr/local/bmv2/targets/simple_switch/runtime_CLI --thrift-port 9090' #'../runtime_CLI --thrift-ip '$addr' --thrift-port 9090'
$cmd < $flows



addr="192.168.59.103"
flows="../flows/setup_switch_s4_4sw.rules"
log="../history/s4.log"
rm -rf $log
touch $log
cmd='usr/local/bmv2/targets/simple_switch/runtime_CLI --thrift-port 9090'#'../runtime_CLI --thrift-ip '$addr' --thrift-port 9090'
$cmd < $flows



addr="192.168.59.104"
flows="../flows/setup_switch_s3_4sw_topo_mov.rules"
log="../history/s3.log"
rm -rf $log
touch $log
cmd='usr/local/bmv2/targets/simple_switch/runtime_CLI --thrift-port 9090'  #'../runtime_CLI --thrift-ip '$addr' --thrift-port 9090'
$cmd < $flows
