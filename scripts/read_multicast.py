import csv
import socket

def get_my_ippaddr():
     
    x=set([i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)])
     
    return list(x)


def get_multicast():
    multicast=[]
    with open('multicast.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            multicast.append(row[0])
    return multicast
# pubsub 1 = publish, 0 = subscribing
def get_my_groups(pubsub=1):
    multicast=[]
    my_ips=get_my_ippaddr()
    with open('multicast.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count +=1 
            else:

                if (int(row[2])==pubsub):

                    for ip in my_ips:
                         
                        if row[0]==ip:
                            multicast.append(row[1])
     
    return multicast

 