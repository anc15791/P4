import time
import os
import sys
import socket

storm_option = sys.argv[1]
sw           = sys.argv[2]
interface    = sys.argv[3]

icmp_rate_limit = 50
tcp_rate_limit  = 200
udp_rate_limit  = 200

permissible_bw = .25

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
count = 1

def find_bandwidth(sw ,intf):
    if sw=="s1":
	sw_addr = "192.168.59.101"
    elif sw=="s2":
	sw_addr = "192.168.59.102"
    elif sw=="s3":
	sw_addr = "192.168.59.104"
    elif sw=="s4":
	sw_addr = "192.168.59.103"

    data = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (sw_addr, 9091)
    sock.connect(server_address)

    try:
	 message = '%s'%intf
	 sock.sendall(message)
	 data = sock.recv(4)
    finally:
   	 sock.close
    return data
 
while True:
     print "\n------------------------------------------------------------------"
     if storm_option == "pps":
     	print ("ID|PROTO|     SRC IP     |     DST IP     |  PPS  | TRAFFIC_STORM ")

     	src= "192.168.56.2"
     	dst= "192.168.60.2"
     	proto= "icmp"
     	cmd="./count_pkts.sh "+src+" "+dst+" "+proto+" "+sw
     	counter1_old=counter1_new
     	counter1_new=int(os.popen(cmd).read())
        
        if (count == 1) :
            delta_packets = 0
	else:
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
     	cmd="./count_pkts.sh "+src+" "+dst+" "+proto+" "+sw
     	counter3_old=counter3_new
     	counter3_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
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
     	cmd="./count_pkts.sh "+src+" "+dst+" "+proto+" "+sw
     	counter5_old=counter5_new
     	counter5_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
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
     	cmd="./count_pkts.sh "+src+" "+dst+" "+proto+" "+sw
     	counter2_old=counter2_new
     	counter2_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
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
     	cmd="./count_pkts.sh "+src+" "+dst+" "+proto+" "+sw
     	counter4_old=counter4_new
     	counter4_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
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
     	cmd="./count_pkts.sh "+src+" "+dst+" "+proto+" "+sw
     	counter6_old=counter6_new
     	counter6_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter6_new - counter6_old)
     	fr = delta_packets/delta_time

     	if (fr > udp_rate_limit):
		flood="YES"
        	os.popen("./11_stop_udp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)
        time.sleep(delta_time)

     elif storm_option=="bps":
        bandwidth_mbps= int(find_bandwidth(sw, interface))
        bandwidth_bps = bandwidth_mbps * 1000 * 1000
        bandwidth_Bps = bandwidth_bps/8

     	print ("ID|PROTO|     SRC IP     |     DST IP     |  BPS  | TRAFFIC_STORM ")

     	src= "192.168.56.2"
     	dst= "192.168.60.2"
     	proto= "icmp"
     	cmd="./count_bytes.sh "+src+" "+dst+" "+proto+" "+sw
     	counter1_old=counter1_new
     	counter1_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter1_new - counter1_old)
     	fr = delta_packets/delta_time

     	if (fr > bandwidth_Bps*permissible_bw ):
		flood="YES"
        	os.popen("./7_stop_icmp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)


 
     	src= "192.168.56.2"
     	dst= "192.168.60.2"
     	proto= "tcp"
     	cmd="./count_bytes.sh "+src+" "+dst+" "+proto+" "+sw
     	counter3_old=counter3_new
     	counter3_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter3_new - counter3_old)
     	fr = delta_packets/delta_time

     	if (fr > bandwidth_Bps*permissible_bw ):
		flood="YES"
        	os.popen("./9_stop_tcp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)




     	src= "192.168.56.2"
     	dst= "192.168.60.2"
     	proto= "udp"
     	cmd="./count_bytes.sh "+src+" "+dst+" "+proto+" "+sw
     	counter5_old=counter5_new
     	counter5_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter5_new - counter5_old)
     	fr = delta_packets/delta_time

     	if (fr > bandwidth_Bps*permissible_bw ):
		flood="YES"
        	os.popen("./11_stop_udp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)




     	dst= "192.168.56.2"
     	src= "192.168.60.2"
     	proto= "icmp"
     	cmd="./count_bytes.sh "+src+" "+dst+" "+proto+" "+sw
     	counter2_old=counter2_new
     	counter2_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter2_new - counter2_old)
     	fr = delta_packets/delta_time

     	if (fr > bandwidth_Bps*permissible_bw ):
		flood="YES"
        	os.popen("./9_stop_icmp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)




     	dst= "192.168.56.2"
     	src= "192.168.60.2"
     	proto= "tcp"
     	cmd="./count_bytes.sh "+src+" "+dst+" "+proto+" "+sw
     	counter4_old=counter4_new
     	counter4_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter4_new - counter4_old)
     	fr = delta_packets/delta_time

     	if (fr > bandwidth_Bps*permissible_bw ):
		flood="YES"
        	os.popen("./9_stop_tcp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)



     	dst= "192.168.56.2"
     	src= "192.168.60.2"
     	proto= "udp"
     	cmd="./count_bytes.sh "+src+" "+dst+" "+proto+" "+sw
     	counter6_old=counter6_new
     	counter6_new=int(os.popen(cmd).read())

        if (count == 1) :
            delta_packets = 0
	else:
     	    delta_packets = (counter6_new - counter6_old)
     	fr = delta_packets/delta_time

     	if (fr > bandwidth_Bps*permissible_bw ):
		flood="YES"
        	os.popen("./11_stop_udp.sh "+sw+" 2>/dev/null")
     	else:
        	flood="no"

     	print  "%-2s|%-5s|%-16s|%-16s|%7s|%3s" % (sw,proto,src,dst,fr,flood)
        time.sleep(delta_time)
     else:
        print "ERROR: Invalid option"
        break

     count = count + 1
