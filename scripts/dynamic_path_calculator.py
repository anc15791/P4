import time
import os
import sys

total_packet_ingress_s1 = 0
total_packet_ingress_s3 = 0
total_packet_egress_s1 = 0
total_packet_egress_s3 = 0
old_ingress_s1 = 0
old_ingress_s3 = 0
old_egress_s1 = 0
old_egress_s3 = 0

while True:
     print "\n------------------------------------------------------------------"
     print ("     SRC IP     |     DST IP     | PACKET LOSS ")

     src= "192.168.56.2"
     dst= "192.168.60.2"
     sw= "s1"

     proto= "icmp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_icmp_ingress_s1=int(os.popen(cmd).read())

     proto= "tcp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_tcp_ingress_s1=int(os.popen(cmd).read())

     proto= "udp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_udp_ingress_s1=int(os.popen(cmd).read())


     total_packet_ingress_s1 = counter_icmp_ingress_s1 + counter_tcp_ingress_s1 + counter_udp_ingress_s1 - old_ingress_s1
     #print total_packet_ingress_s1

     time.sleep(0.1)
     sw= "s3"

     proto= "icmp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_icmp_ingress_s3=int(os.popen(cmd).read())

     proto= "tcp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_tcp_ingress_s3=int(os.popen(cmd).read())

     proto= "udp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_udp_ingress_s3=int(os.popen(cmd).read())


     total_packet_ingress_s3 = counter_icmp_ingress_s3 + counter_tcp_ingress_s3 + counter_udp_ingress_s3 - old_ingress_s3
     #print total_packet_ingress_s3


     packet_loss_ingress =((total_packet_ingress_s1 - total_packet_ingress_s3)*100.0)/total_packet_ingress_s1

     print  "%-16s|%-16s|%12f" % (src,dst,packet_loss_ingress)




 

     src= "192.168.60.2"
     dst= "192.168.56.2"
     sw= "s1"

     proto= "icmp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_icmp_egress_s1=int(os.popen(cmd).read())

     proto= "tcp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_tcp_egress_s1=int(os.popen(cmd).read())

     proto= "udp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_udp_egress_s1=int(os.popen(cmd).read())


     total_packet_egress_s1 = counter_icmp_egress_s1 + counter_tcp_egress_s1 + counter_udp_egress_s1 - old_egress_s1
     #print total_packet_egress_s1


     sw= "s3"

     proto= "icmp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_icmp_egress_s3=int(os.popen(cmd).read())

     proto= "tcp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_tcp_egress_s3=int(os.popen(cmd).read())

     proto= "udp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter_udp_egress_s3=int(os.popen(cmd).read())


     total_packet_egress_s3 = counter_icmp_egress_s3 + counter_tcp_egress_s3 + counter_udp_egress_s3 - old_egress_s3
     #print total_packet_egress_s3


     packet_loss_egress = ((total_packet_egress_s3 - total_packet_egress_s1)*100.0)/total_packet_egress_s3

     print  "%-16s|%-16s|%12f" % (src,dst,packet_loss_egress)

     if ((packet_loss_ingress > 30.0) or (packet_loss_egress > 30.0)):
        cmd = "./change_topo.sh"
        os.popen(cmd)
	old_ingress_s1 = total_packet_ingress_s1
	old_egress_s1  = total_packet_egress_s1
	old_ingress_s3 = total_packet_ingress_s3
	old_egress_s1  = total_packet_egress_s3
        print "ERROR: Path changed due to heavy packet loss"
     
     time.sleep(3)
