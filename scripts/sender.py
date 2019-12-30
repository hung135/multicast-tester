import socket
import struct
import sys
import read_multicast
import receiver
import time
NumMessages=1
hertz = 100
message = b'very important data'


 


 
import multiprocessing as mp
  
 
def run(proc,shared_array):
    sender(NumMessages,shared_array)

def strobe(hertz,shared_array):
    sleep_time=(1000/hertz)/1000
    print(sleep_time)
    while True:
        time.sleep(sleep_time)
        
        if shared_array[1]==0:
            print("Time to Send Cycle Blown")
            sys.exit()
            print("xxx")
        shared_array[1]=0

def sender(NumMessages,shared_array):
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

if __name__ == '__main__':
  
    mp_proc_list =[]
    shared_array = mp.Array('d', range(3))
    shared_array[1]=1 #initialize
    multicast_groups = read_multicast.get_my_groups(1)
    #1 process to do all the sending
    proc = mp.Process(target=receiver.sender, args=(0,  shared_array,multicast_groups,))
    strobe = mp.Process(target=receiver.strobe, args=(hertz,  shared_array,))
    mp_proc_list.append(proc)
    mp_proc_list.append(strobe)
    proc.start()
    strobe.start()
    
    while True:
        time.sleep(1)
        total_msg=0
         
        

        total_msg+=int(shared_array[0])
        if shared_array[1]==0:
            print("Time to Send Cycle Blown")
        shared_array[1]=0
        print("Total Messages Sent: ", total_msg)
    for l in mp_proc_list:
        l.join()    
