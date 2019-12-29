import receiver
import multiprocessing
import ctypes
import time
 


 
 
import multiprocessing as mp
  
multicast_groups = ['224.3.29.71','224.3.29.72']
def run(proc,shared_array,multicast_group):
    receiver.receive(proc,shared_array,multicast_group)



if __name__ == '__main__':
  
    listener_list =[]
    shared_array = mp.Array('d', range(len(multicast_groups)))
    print(len(multicast_groups))
    for proc_num,multicast_group in enumerate(multicast_groups,0):
        print("starting up...",proc_num,multicast_group)
        listener = mp.Process(target=run, args=(proc_num,  shared_array,multicast_group,))
    
        listener_list.append(listener)
        listener.start()
    
    while True:
        time.sleep(2)
        for p,multicast_group in enumerate(multicast_groups,0):
            print("Messages Received: ",multicast_group,shared_array[p])
    
    for l in listener_list:
        l.join()    
