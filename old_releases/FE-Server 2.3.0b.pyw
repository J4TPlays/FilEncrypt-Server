import socket
import threading
import sys
import random as rd
ver="2.3.0"
user_token=""
recv_username=""
recv_ch_token=""
user_cmds=["/help","/dc","/afk","/newtoken","/changetoken","/currenttoken"]
keydir=""
last_username="00000000"
msngr_afk="0"
tmp=""
user_has_ch_token=""
allowed_token_chars=["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C",
"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
"U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
print(str("\nJ4T's Chat Server\nBETA TEST VERSION "+ver+"\n"))
print("\nWhat are you connecting as?\n\"host\"       - allows you to host the server\n\"client\"     - allows you to read messages sent after you have connected\n\"messenger\"  - allows you to send messages")
user_connection=input("\n> ")
if user_connection=="messenger":
    while user_token=="":
        user_token=input("\nWhat is your name?\n\n> ")
        if user_token=="":
            print("Invalid name.")
if user_connection in ("client","messenger"):
    target_ip=input("Enter the target's IP address followed by the port:\neg. \"127.0.0.1:27015\"\n\n> ")
    print("Warning! The host will have your public IP address when you connect.\nPlease be aware of this!")
    target_port=target_ip.split(":")[1]
    target_ip=target_ip.split(":")[0]
    while keydir=="":
        enc=[]
        print("\nPlease drag the FilEncrypt server key file here.")
        keydir=input("\n> ")
        if keydir[0]==keydir[-1] and keydir[0] in ("'",'"'):
            keydir=keydir[1:-1]
        try:
            keyfile=[0,0]
            keyfile[0]=open(keydir,"r")
            keyfile[1]=keyfile[0].read()
            keyfile[0].close()
            if keyfile[1][-9:]!="/-server-":
                print("")
            elif keyfile[1][-9:]=="/-server-":
                us_ab=[]
                enc_type="server"
                keyfile[1]="%s"%"".join(keyfile[1][0:-9])
                us_key_length=int((len(keyfile[1])-95)/95)
                for i in range(95):
                    try:
                        enc.append(keyfile[1][i*us_key_length:(i*us_key_length)+us_key_length])
                    except IndexError:
                        print("\nInvalid / corrupted key file.")
                        keydir=""
                for i in range(95):
                    try:
                        us_ab.append(keyfile[1][i+(95*us_key_length)])
                    except:
                        print("Invalid / corrupted key file.")
                        keydir=""
        except FileNotFoundError:
            keydir=""
            print("\nFile not found.")
        except OSError:
            keydir=""
            print("\nInvalid file.")
    while user_has_ch_token=="":
        print("\nDo you have a channel token?")
        user_has_ch_token=input("\n> ")
        if user_has_ch_token not in ("Y","y","N","n"):
            print("\nInvalid response.")
            user_has_ch_token=""
        else:
            if user_has_ch_token in ("Y","y"):
                print("\nPlease enter the channel token.")
                channel_token=input("\n> ")
                if not (4<=len(channel_token)<=8):
                    print("Invalid token length")
                    user_has_ch_token=""
                else:
                    for i in range(len(channel_token)):
                        if channel_token[i] not in allowed_token_chars:
                            user_has_ch_token=""
                            print("Invalid token.")
                        else:
                            pass
                        if i==len(channel_token)-1 and user_has_ch_token!="":
                            print("Token accepted.")
            elif user_has_ch_token in ("N","n"):
                channel_token=allowed_token_chars[rd.randint(0,61)]
                for i in range(rd.randint(3,7)):
                    channel_token=str(channel_token+allowed_token_chars[rd.randint(0,61)])
                print(str("Your channel token is:     "+channel_token))
elif user_connection=="host":
    host_port=input("What port do you want to open this server on?\nMust be between 0 and 65535\n\n> ")
    if not 0<=int(host_port)<=65535:
        user_connection="ERROR"
class Server:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connections=[]
    def __init__(self):
        self.sock.bind(("0.0.0.0",int(host_port)))
        self.sock.listen(1)
    def handler(self,c,a):
        while True:
            try:
                data=c.recv(1024)
                for connection in self.connections:
                    try:
                        connection.send(data)
                    except:
                        pass
                if not data:
                    break
            except ConnectionResetError:
                pass
    def run(self):
        while True:
            c,a=self.sock.accept()
            cThread=threading.Thread(target=self.handler,args=(c,a))
            cThread.daemon=True
            cThread.start()
            self.connections.append(c)
            print(self.connections[-1])
class Client:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self,address,port):
        self.sock.connect((address,int(port)))
        print("\nConnected!\n\n")
        last_username="00000000"
        while True:
            try:
                data=self.sock.recv(1024)
            except ConnectionResetError as e:
                print(str(e))
                break
            if not data:
                break
            data=str(data)
            try:
                data_strip=data.split(",")[3:]
                msg_type=data.split(",")[1]
                recv_ch_token=data.split(",")[2]
                recv_username=data.split(",")[0][2:]
                data_strip[-1]=str("%s"%"".join(data_strip[-1][0:-1]))
                data_strip="%s"%",".join(data_strip)
                data_decrypt=[]
                if recv_ch_token==channel_token:
                    for i in range(int(int(len(data_strip))/int(len(enc[0])))):
                        try:
                            data_decrypt.append(us_ab[enc.index("%s"%"".join(data_strip[(i*int(len(enc[0]))):(i*int(len(enc[0])))+int(len(enc[0]))]))])
                        except ValueError:
                            pass
                    if msg_type=="msg":
                        if "%s"%"".join(data_decrypt)!="":
                            if last_username!=recv_username:
                                print(str("\n"+recv_username+":\n    "+("%s"%"".join(data_decrypt))))
                            else:
                                print(str("    "+("%s"%"".join(data_decrypt))))
                            last_username=recv_username
                    elif msg_type=="con":
                        print(str("\n"+recv_username+" has joined the chat room."))
                        last_username=""
                    elif msg_type=="dis":
                        print(str("\n"+recv_username+" has left the chat room."))
                        last_username=""
                    elif msg_type=="afk":
                        print(str("\nUSER \""+recv_username+"\" is now AFK"))
                        last_username=""
                    elif msg_type=="btk":
                        print(str("\nUSER \""+recv_username+"\" is no longer AFK"))
                        last_username=""
            except:
                pass
class Messenger:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def sendMsg(self):
        global channel_token
        self.sock.send(bytes(str(user_token+",con,"+channel_token+", "),"utf-8"))
        msngr_afk="0"
        while True:
            your_message=input(str("\nYOU> "))
            to_write=[]
            for i in range(len(your_message)):
                try:
                    if enc_type=="server":
                        to_write.append(enc[us_ab.index(your_message[i])])
                except IndexError:
                    pass
                except ValueError:
                    pass
            if len(your_message)>0:
                try:
                    if (your_message.split(" ")[0][0])!="/":
                        try:
                            while your_message[-1]==" ":
                                your_message=str("%s"%"".join(your_message[0:-1]))
                            to_write=str("%s"%"".join(to_write))
                            if your_message!="":
                                if msngr_afk=="0":
                                    self.sock.send(bytes(str(user_token+",msg,"+channel_token+","+to_write),"utf-8"))
                                else:
                                    print("You are AFK! Type \"/afk\" to send messages.")
                        except ConnectionResetError as e:
                            print(str("\n"+e))
                            break
                    else:
                        used_cmd=your_message.split(" ")
                        if used_cmd[0] in user_cmds:
                            if used_cmd[0]==user_cmds[0]:
                                print("\n\n")
                                print("\"/help\"                - brings up this help menu")
                                print("\"/dc\"                  - disconnects from the server")
                                print("\"/afk\"                 - enables / disables AFK")
                                print("\"/newtoken <length>\"   - generates a new channel token")
                                print("\"/changetoken <token>\" - lets you switch channels")
                                print("\"/currenttoken\"        - displays your current token")
                                print("\n")
                            elif used_cmd[0]==user_cmds[1]:
                                self.sock.send(bytes(str(user_token+",dis,"+channel_token+", "),"utf-8"))
                                print("\n\nYou have disconnected from the server.\nPlease close this window as it is no longer needed.\n")
                                break
                            elif used_cmd[0]==user_cmds[2]:
                                if msngr_afk=="0":
                                    self.sock.send(bytes(str(user_token+",afk,"+channel_token+",  "),"utf-8"))
                                    msngr_afk="1"
                                elif msngr_afk=="1":
                                    self.sock.send(bytes(str(user_token+",btk,"+channel_token+", "),"utf-8"))
                                    msngr_afk="0"
                            elif used_cmd[0]==user_cmds[3]:
                                if len(used_cmd)==1:
                                    channel_token=allowed_token_chars[rd.randint(0,61)]
                                    for i in range(rd.randint(3,7)):
                                        channel_token=str(channel_token+allowed_token_chars[rd.randint(0,61)])
                                elif len(used_cmd)==2:
                                    try:
                                        if 4<=int(used_cmd[1])<=8:
                                            channel_token=allowed_token_chars[rd.randint(0,61)]
                                            for i in range(int(used_cmd[1])):
                                                channel_token=str(channel_token+allowed_token_chars[rd.randint(0,61)])
                                        else:
                                            print("\nInvalid length.")
                                    except:
                                        pass
                                elif len(used_cmd)>2:
                                    print("Invalid arguments")
                            elif used_cmd[0]==user_cmds[4]:
                                if len(used_cmd)!=2:
                                    print("Invalid arguments.")
                                else:
                                    channel_token=used_cmd[1]
                            elif used_cmd[0]==user_cmds[5]:
                                print(str("\nYour channel token is:     "+channel_token))
                        else:
                            print("Type \"/help\" for a list of commands")
                except:
                    pass
    def __init__(self,address,port):
        self.sock.connect((address,int(port)))
        
        print("\nConnected!\n\n")
        iThread=threading.Thread(target=self.sendMsg)
        iThread.daemon=True
        iThread.start()
        while True:
            try:
                data=self.sock.recv(1024)
            except ConnectionResetError as e:
                print(str("\n"+e))
                break
            if not data:
                break
            data=str(data)
            data_strip=data.split(",")[1:]
            recv_username=data.split(",")[0][2:]
            data_strip[-1]=str("%s"%"".join(data_strip[-1][0:-1]))
if user_connection=="client":
    client=Client(target_ip,target_port)
elif user_connection=="host":
    print(str("Working!\nOpened server on port "+host_port))
    server=Server()
    server.run()
elif user_connection=="messenger" and user_token!="":
    messenger=Messenger(target_ip,target_port)
else:
    print("An error occurred.")
finish=input("Press ENTER to exit.")
