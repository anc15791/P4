#!/bin/bash
#echo "INFO: This command runs on Firewall. It wont show any output unless firewall is activated and initialised"
#echo ""

counter="-1"
if [ "$1" = "192.168.56.2" ]
then
   if [ "$2" = "192.168.60.2" ]
   then 
       case "$3" in
            "icmp")
                 counter="0" ;;
            "tcp")
                 counter="2" ;;
            "udp")	
                 counter="4" ;;
       esac
   else
       echo "ERROR: invalid dest"
       exit
   fi
elif [ "$1" = "192.168.60.2" ]
then
   if [ "$2" = "192.168.56.2" ]
   then 
       case "$3" in
            "icmp")
                 counter="1" ;;
            "tcp")
                 counter="3" ;;
            "udp")
                 counter="5" ;;
       esac
   else
       echo "ERROR: invalid dest"
       exit
   fi
else
   echo "ERROR: invalid src"
   exit
 
fi



if [ "$4" = "s1" ]
then
   addr="192.168.59.101"
fi

if [ "$4" = "s2" ]
then
   addr="192.168.59.102"
fi

if [ "$4" = "s3" ]
then
   addr="192.168.59.104"
fi

cmd1='counter_read pkt_src_counter '$counter
cmd2='/home/ubuntu/p4guard/targets/p4guard/sswitch_CLI firewall.json 9090 '$addr

output="$(echo "$cmd1" | $cmd2 2>/dev/null)"

#echo $output | sed -e ''
nop="0"
nop=$(echo $output | awk -F'[=,]' '{print $3}')
#echo "Number Of "$3" packets = "$nop
echo $nop
