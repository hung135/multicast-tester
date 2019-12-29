import socket
import struct
import sys

from bitstring import BitArray

def receive():
    multicast_group = '224.3.29.71'
    server_address = ('', 10000)

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
    msg_received=0
    while True (bool):
        #print(sys.stderr, '\nwaiting to receive message: ',msg_received)
        msg_received+=1
        data, address = sock.recvfrom(1024)
        
        #print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
        #print(sys.stderr, data)
        
        if msg_received%50000==0:
            print(msg_received)
            

        #print(sys.stderr, 'sending acknowledgement to', address)
        #sock.sendto(data, address)