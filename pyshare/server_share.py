#----tcp server---------
#-----for instructions see tcp client script---------
#--------written by black_perl(ankush sharma) @ 19-08-2013----------

import socket
def connection():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),6209))#put the host address in a tuple
    s.listen(1)#listening at the address to which socket is bounded
    print "listening at",s.getsockname()
    (k,addr)=s.accept()#a client socket k is created to addr
    print "connected to",k.getpeername()
    return k,addr
def fileinput():
    filename=raw_input("Enter the qualified name of the file:")
    f=open(filename,"rb")
    return f,filename
def main():
    client,addr=connection()
    fob,f_name=fileinput()
    client.send("{} is ready for download".format(f_name))
    data_now=0
    buff_size=1024*1024*20
    buffer=fob.read(buff_size)
    data_sent=client.send(buffer)
    while  data_sent>0:#send function returns no. of bytes sent
          data_now+=data_sent
          print (data_now/1048576),"mb---sent-----  \n"
          buffer=fob.read(buff_size)
          data_sent=client.send(buffer)
          if data_sent==0:
              print '''------file sending successful------ /n socket connection close'''
              client.close()

if __name__=="__main__":main()
# a combination of 10 and 20 is best       
                 
    
    
