import socket
import struct
import sys
import time
 
def receive(proc_num,msg_received,multicast_group):
    
    server_address = ('', 10000+proc_num)

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address
    
    sock.bind(server_address)
    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    # Receive/respond loop
    msg_received[proc_num]=0
    while True :
        #print(sys.stderr, '\nwaiting to receive message: ',msg_received)
        
        data, address = sock.recvfrom(1024)
        msg_received[proc_num]+=1
        
        #print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
        #print(sys.stderr, data)
        

        #print(sys.stderr, 'sending acknowledgement to', address)
        #sock.sendto(data, address)


def strobe(hertz,shared_array):
    sleep_time=(1000/hertz)/1000
    print(sleep_time)
    while True:
        time.sleep(sleep_time)
        
        if shared_array[1]==0:
            print("Time to Send Cycle Blown")
        shared_array[1]=0


def sender(NumMessages,shared_array,multicast_groups):
    
    groups=[]
    
    for inc, group in enumerate(multicast_groups,0):
        groups.append((group, 10000+inc))
        

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(0.2)
    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack('b', 1)
    bytest_string=''
    #may 1400 bytes
    for i in range(1, 1400):
        bytest_string=bytest_string+'1'

    x=bytes(bytest_string,'utf8')
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    try:

        # Send data to the multicast group
        msg_sent=0
        while True:
            if shared_array[1]==0:
                #for xxx in range(0, NumMessages) :
                    #print(sys.stderr, 'sending "%s"' % message)
                for group in groups:
                    #print(group)
                    sent = sock.sendto(x, group)
                    msg_sent+=1
 
                shared_array[0]=msg_sent
                shared_array[1]=1
             
            
    finally:
        print(sys.stderr, 'closing socket')
        sock.close()
