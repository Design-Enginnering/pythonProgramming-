from cryptography.fernet import Fernet
import os 

class Encrypt:
    def __init__ (self,filename, key):
        self.filename = filename 
        self.key = key 
    
    def encrypt(self): 
      f = Fernet(self.key)
      with open(self.filename, 'rb') as file:
        file_data = file.read()
      encrypted_data = f.encrypt(file_data)
      with open(self.filename, 'wb') as file:
         file.write(encrypted_data)
class Decrypt:
      def __init__(self, filename, key): 
         self.filename = filename
         self.key  = key 
      def decrypt(self):
         f = Fernet(self.key)
         with open(self.filename, 'rb') as file:
           encrypted_data = file.read()
         decrypted_data = f.decrypt(encrypted_data)
         with open(self.filename, 'wb') as file:
             file.write(decrypted_data)
def load_key(filename):
    key = Fernet.generate_key()
    with open(filename , 'wb') as key_file:
       key_file.write(key)
    return open(filename, 'rb').read()



choise = int(input('Enter you choise\n 1. Encryption \t 2. Decryption\n'))
filename = input('Enter filename with extention : ') 


if(choise == 1):
   create_dir = filename.replace('.', '_dir_')
   try:
       os.mkdir(create_dir)
       fileName  =  create_dir+'/'+filename+ str('.key')
       key = load_key(fileName)
       encryption=  Encrypt(filename,key)
       encryption.encrypt()
   except:
       fileName  =  create_dir+'/'+filename+ str('.key')
       key = load_key(fileName)
       encryption=  Encrypt(filename,key)
       encryption.encrypt()    
elif(choise == 2):    
     create_dir = filename.replace('.', '_dir_')
     fileName  =  create_dir+'/'+filename+ str('.key')
     try:
         key = open(fileName, 'rb').read()
         decryption = Decrypt(filename,key)
         decryption.decrypt()
     except FileNotFoundError  as fnf:
       print('\n ***** Please first Encrypt file then Decrypt file  ****')
    
else : 
   print('*************** Invaild Input ****************') 
    

