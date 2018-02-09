sudo ../../../../bmv2/targets/simple_switch/simple_switch -i 1@eth2 -i 2@eth3 --device-id 1 --log-console --thrift-port 9090 --nanolog ipc:///tmp/bm-1-log.ipc ../firewall_switch.json
