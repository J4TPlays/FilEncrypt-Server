import socket
import threading
import sys
ver="1.0.0"
user_token=""
recv_username=""
user_cmds=["/help","/dc"]
print(str("\nJ4T's Chat Server\nBETA TEST VERSION "+ver+"\n"))
print("\nWhat are you connecting as?\n\"host\" - you will host the server\n\"client\" - you will read messages sent after you connect\n\"messenger\" [ IN TESTING ] - allows you to send the messages")
user_connection=input("\n> ")
if user_connection=="messenger":
    user_token=input("\nWhat is your name?\n\n> ")
if user_connection in ("client","messenger"):
    target_ip=input("Enter the target's IP address followed by the port:\neg. \"127.0.0.1:27015\"\n\n> ")
    print("Warning! The host will now have your public IP address.\nPlease be aware of this!")
    target_port=target_ip.split(":")[1]
    target_ip=target_ip.split(":")[0]
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
        while True:
            try:
                data=self.sock.recv(1024)
            except ConnectionResetError as e:
                print(e)
                break
            if not data:
                break
            data=str(data)
            print(data[2:-1])
class Messenger:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def sendMsg(self):
        while True:
            your_message=input(str("\nYOU> "))
            if len(your_message)>0:
                if (your_message.split(" ")[0][0])!="/":
                    try:
                        while your_message[-1]==" ":
                            your_message=str("%s"%"".join(your_message[0:-1]))
                        if your_message!="":
                            self.sock.send(bytes(str(user_token+",msg,"+your_message),"utf-8"))
                    except ConnectionResetError as e:
                        print(e)
                        break
                else:
                    used_cmd=your_message.split(" ")
                    if used_cmd[0] in user_cmds:
                        if used_cmd[0]==user_cmds[0]:
                            print("\"/help\" - brings up this help menu")
                            print("\"/dc\"   - disconnects from the server")
                    else:
                        print("Type \"/help\" for a list of commands")
    def __init__(self,address,port):
        self.sock.connect((address,int(port)))
        iThread=threading.Thread(target=self.sendMsg)
        iThread.daemon=True
        iThread.start()
        while True:
            try:
                data=self.sock.recv(1024)
            except ConnectionResetError as e:
                print(e)
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