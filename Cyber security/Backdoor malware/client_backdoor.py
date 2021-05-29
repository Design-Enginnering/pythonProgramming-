import os 
import socket 

s = socket.socket()
port = 8082
host = input(str('please enter the server address :  '))
try:
    s.connect((host, port))
    print('')
    print('connected to the server successfully')
    print('')
    exit = 1 

    while exit:
       command = s.recv(1024)
       command = command.decode()
       print('command recived')
       print('')
       if command == 'view_cwd':
          files = os.getcwd()
          files = str(files)
          
          s.send(files.encode())
          
          print('command has been excuted successfully... ')
       
       elif command == 'custom_dir':
            user_input = s.recv(5000)
            user_input = user_input.decode()
            files = os.listdir(user_input)
            print(files)
            files = str(files)
            s.send(files.encode())
            print('command has been successfully...')
            print('')
            
       elif command == 'download_file':
            file_path = s.recv(5000)
            file_path = file_path.decode()
            file = open(file_path, 'rb')
            data = file.read()
            s.send(data)
            print('')
            print('File has been send succeessfully \n')
       elif(command == 'exit'):
            s.close()
            exit = 0      
              
       else:
          print('')
          print('command is not recongnised')   
          
          
except:
     print('')
     print("Server isn't found please try again later ......\n")      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
