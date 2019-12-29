import socket
import struct
import sys
 
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
    