import socket
import struct
import sys
import read_multicast
import time
NumMessages=50
message = b'very important data'


  
multicast_groups = read_multicast.get_my_groups(1)
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
for xxx in range(1, 1400):
    bytest_string=bytest_string+'1'

x=bytes(bytest_string,'utf8')
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
try:

    # Send data to the multicast group
    msg_sent=0
    while True:
        for xxx in range(0, NumMessages) :
            #print(sys.stderr, 'sending "%s"' % message)
            for group in groups:
                #print(group)
                sent = sock.sendto(x, group)
                msg_sent+=1
 
        print("Going to Sleep 1 sec: Messages sent: ",msg_sent)
        time.sleep(1)
finally:
    print(sys.stderr, 'closing socket')
    sock.close()