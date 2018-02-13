import time
import os
import sys

sw= sys.argv[1]
icmp_rate_limit = 100
tcp_rate_limit  = 200
udp_rate_limit  = 200

counter1_old   = 0
counter1_new   = 0
counter2_old   = 0
counter2_new   = 0
counter3_old   = 0
counter3_new   = 0
counter4_old   = 0
counter4_new   = 0
counter5_old   = 0
counter5_new   = 0
counter6_old   = 0
counter6_new   = 0

fr = 0
delta_packets = 0
delta_time = 3

while True:
     print "\n------------------------------------------------------------------"
     print ("ID|PROTO|     SRC IP     |     DST IP     |  BW  | DOS ")

     src= "192.168.56.2"
     dst= "192.168.60.2"
     proto= "icmp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter1_old=counter1_new
     counter1_new=int(os.popen(cmd).read())

     delta_packets = (counter1_new - counter1_old)
     fr = delta_packets/delta_time

     if (fr > icmp_rate_limit):
	flood="YES"
        os.popen("./7_stop_icmp.sh "+sw+" 2>/dev/null")
     else:
        flood="no"

     print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)


 
     src= "192.168.56.2"
     dst= "192.168.60.2"
     proto= "tcp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter3_old=counter3_new
     counter3_new=int(os.popen(cmd).read())

     delta_packets = (counter3_new - counter3_old)
     fr = delta_packets/delta_time

     if (fr > tcp_rate_limit):
	flood="YES"
        os.popen("./9_stop_tcp.sh "+sw+" 2>/dev/null")
     else:
        flood="no"

     print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)




     src= "192.168.56.2"
     dst= "192.168.60.2"
     proto= "udp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter5_old=counter5_new
     counter5_new=int(os.popen(cmd).read())

     delta_packets = (counter5_new - counter5_old)
     fr = delta_packets/delta_time

     if (fr > udp_rate_limit):
	flood="YES"
        os.popen("./11_stop_udp.sh "+sw+" 2>/dev/null")
     else:
        flood="no"

     print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)




     dst= "192.168.56.2"
     src= "192.168.60.2"
     proto= "icmp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter2_old=counter2_new
     counter2_new=int(os.popen(cmd).read())

     delta_packets = (counter2_new - counter2_old)
     fr = delta_packets/delta_time

     if (fr > icmp_rate_limit):
	flood="YES"
        os.popen("./9_stop_icmp.sh "+sw+" 2>/dev/null")
     else:
        flood="no"

     print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)




     dst= "192.168.56.2"
     src= "192.168.60.2"
     proto= "tcp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter4_old=counter4_new
     counter4_new=int(os.popen(cmd).read())

     delta_packets = (counter4_new - counter4_old)
     fr = delta_packets/delta_time

     if (fr > tcp_rate_limit):
	flood="YES"
        os.popen("./9_stop_tcp.sh "+sw+" 2>/dev/null")
     else:
        flood="no"

     print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)



     dst= "192.168.56.2"
     src= "192.168.60.2"
     proto= "udp"
     cmd="./count.sh "+src+" "+dst+" "+proto+" "+sw
     counter6_old=counter6_new
     counter6_new=int(os.popen(cmd).read())

     delta_packets = (counter6_new - counter6_old)
     fr = delta_packets/delta_time

     if (fr > udp_rate_limit):
	flood="YES"
        os.popen("./11_stop_udp.sh "+sw+" 2>/dev/null")
     else:
        flood="no"

     print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)


     time.sleep(delta_time)
