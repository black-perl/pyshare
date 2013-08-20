#-------tcp client-------
#--------written by black_perl(ankush sharma) @ 18-08-2012------
#---------this is the client side part of this application------
#----------for using you need to specify the host address you want to connect,keeping the server side running the server script server_share.py--------------
#-----------currently this is the beta version ,soon both client and server scripts will be combined into single script,giving an original peer2peer feel--------------- 
#------for any queries message me at nick-@dustin on dc----------
import socket,time,os
def connection():
    remote_host=raw_input("enter ip of the remote host:")
    port=input("enter the service of remote host to which you want to connect:")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),6700))
    s.connect((remote_host,port))#establishing connection to the host
    print "connected to",s.getpeername()
    return s
def main():
    client=connection()
    line_from_rhost=client.recv(4096)#receives at most 4kb
    print line_from_rhost
    filename=raw_input("enter a qualified name of the file to be received:")
    fob=open(filename,"wb")
    data_now=0
    buff_size=1024*1024*1
    start=time.time()
    buffer=client.recv(buff_size)
    while len(buffer)>0:
       fob.write(buffer)
       data_now+=len(buffer)
       print (data_now/(1024*1024)),"mb------received------\n"
       buffer=client.recv(buff_size)
       if len(buffer)==0:
           end=time.time()
           print '''------file sending successful------ /n socket connection close'''
           size=os.path.getsize(filename)
           print "----------received  ",(size/(1024*1024)),"\n"
           print "-----------average speed   ",((size/(1024*1024))/(end-start))," MB/S"
           fob.close()
           client.close()
if __name__=="__main__":main()



       
    
    
    
