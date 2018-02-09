cd /usr/local/bmv2/targets/simple_router/
sudo ./simple_router -i 1@eth1 -i 2@eth2 -i 3@eth3 --device-id 2 --log-console --thrift-port 9092 --nanolog ipc:///tmp/bm-2-log.ipc /users/anurag0/P4/cloudlab_ipblacklist/ipblacklist_router.json
