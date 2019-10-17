import socket
import threading
import sys
from tkinter import *
import random as rd
root=Tk()
root.geometry("850x480")
root.resizable(False,False)
root.configure(background="#2c2c2c")
root.wm_title("FilEncrypt Server")
client_connect_request="0"
ver="3.0.0"
recv_username=""
user_cmds=["/help","/dc","/afk","/newtoken","/changetoken","/currenttoken"]
keydir=""
last_username=False
msngr_afk="0"
command_line_used="0"
frame=Frame(root)
user_can_send_msg="1"
messages_to_view=""
temp=[]
client_is_connected_to_svr="0"
enc_2=[]
allowed_token_chars=["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C",
"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
"U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
text_check_index=0

keydir=""








"""
while keydir=="":
    keydir="/mnt/chromeos/MyFiles/J4T-Folder/python/fe-server/WORKING_J4T_SERVER_sv.key"
    enc=[]
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
"""





tmp=""
if command_line_used=="1":
    user_connection=input("\n> ")
    if user_connection=="messenger":
        while user_token=="":
            user_token=input("\nWhat is your name?\n\n> ")
            if user_token=="":
                print("Invalid name.")
    if user_connection in ("client","messenger"):
        target_ip=input("Enter the target's IP address followed by the port:\neg. \"127.0.0.1:27015\"\n\n> ")
        print("Warning! The host will now have your public IP address.\nPlease be aware of this!")
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
                    us_key_length=int((len(keyfile[1])-96)/96)
                    for i in range(96):
                        try:
                            enc.append(keyfile[1][i*us_key_length:(i*us_key_length)+us_key_length])
                        except IndexError:
                            print("\nInvalid / corrupted key file.")
                            keydir=""
                    for i in range(96):
                        try:
                            us_ab.append(keyfile[1][i+(96*us_key_length)])
                        except:
                            print("Invalid / corrupted key file.")
                            keydir=""
            except FileNotFoundError:
                keydir=""
                print("\nFile not found.")
            except OSError:
                keydir=""
                print("\nInvalid file.")
    elif user_connection=="host":
        host_port=input("What port do you want to open this server on?\nMust be between 0 and 65535\n\n> ")
        if not 0<=int(host_port)<=65535:
            user_connection="ERROR"

class Startup:
    def choice_host():
        """
        client_button.place_forget()
        host_button.place_forget()
        back_button.place(x=20,y=20)
        host_port_but.place(x=298,y=250)
        host_port_ent.place(x=273,y=220)
        host_port_lab.place(x=300,y=100)
        """
        print("HOSTING HASN'T BEEN IMPLEMENTED YET!")
    def choice_client():
        client_button.place_forget()
        host_button.place_forget()
        ip_and_port_ent.place(x=273,y=152)
        ip_and_port_lab.place(x=300,y=100)
        get_their_username_ent.place(x=273,y=222)
        get_their_username_lab.place(x=300,y=200)
        get_their_ch_token_ent.place(x=273,y=292)
        generate_random_token.place(x=590,y=289)
        get_their_ch_token_lab.place(x=300,y=270)
        get_their_sv_key_ent.place(x=273,y=362)
        get_their_sv_key_lab.place(x=300,y=340)
        back_button.place(x=20,y=20)
        ip_and_port_go.place(x=300,y=450)
        root.bind("<Return>",Startup.connect_button)
    def go_back():
        host_button.place(x=150,y=200)
        client_button.place(x=500,y=200)
        back_button.place_forget()
        ip_and_port_ent.delete(0,END)
        get_their_username_ent.delete(0,END)
        get_their_ch_token_ent.delete(0,END)
        get_their_sv_key_ent.delete(0,END)
        generate_random_token.place_forget()
        ip_and_port_ent.place_forget()
        ip_and_port_lab.place_forget()
        ip_and_port_go.place_forget()
        host_port_but.place_forget()
        host_port_ent.place_forget()
        host_port_lab.place_forget()
        error_lab.place_forget()
        get_their_ch_token_lab.place_forget()
        get_their_ch_token_ent.place_forget()
        get_their_username_lab.place_forget()
        get_their_username_ent.place_forget()
        get_their_sv_key_ent.place_forget()
        get_their_sv_key_lab.place_forget()
        scrollbar_cnv.place_forget()




    def connect():
        global target_ip,target_port,enc_2,enc_type,us_ab,user_token,channel_token
        error_lab.place_forget()
        tmp="NO_ERRORS_CONNECTION_STARTING"
        try:
            tmp="NO_ERRORS_STARTUP.CONNECT"
            target_ip=str(ip_and_port_ent.get())
            target_port=target_ip.split(":")[1]
            target_ip=target_ip.split(":")[0]
            """
            client=Client(target_ip,target_port)
            messenger=Messenger(target_ip,target_port)
            """
        except:
            error_lab.place(x=596,y=152)
            ip_and_port_ent.delete(0,END)
            tmp="ARE_ERRORS_STARTUP.CONNECT"
        if tmp=="NO_ERRORS_STARTUP.CONNECT":
            try:
                tmp="NO_ERRORS_GETTING_THEIR_USERNAME"
                temp=[]
                user_token=str(get_their_username_ent.get())
                for i in range(len(user_token)):
                    if user_token[i]!=" ":
                        temp.append(user_token[i])
                user_token=str("%s"%"".join(temp[0:]))
                if len(user_token)<2 or len(user_token)>8:
                    tmp="ARE_ERRORS_GETTING_THEIR_USERNAME"
                    error_lab.place(x=596,y=222)
            except:
                error_lab.place(x=596,y=222)
                tmp="ARE_ERRORS_GETTING_THEIR_USERNAME"
                get_their_username_ent.delete(0,END)
        if tmp=="NO_ERRORS_GETTING_THEIR_USERNAME":
            try:
                tmp="NO_ERRORS_GETTING_THEIR_CH_TOKEN"
                temp=[]
                channel_token=str(get_their_ch_token_ent.get())
                for i in range(len(channel_token)):
                    if channel_token[i]!=" ":
                        temp.append(channel_token[i])
                channel_token=str("%s"%"".join(temp[0:]))
                if not (4<=len(channel_token)<=8):
                    tmp="ARE_ERRORS_GETTING_THEIR_CH_TOKEN"
                    error_lab.place(x=666,y=292)
            except:
                tmp="ARE_ERRORS_GETTING_THEIR_CH_TOKEN"
        if tmp=="NO_ERRORS_GETTING_THEIR_CH_TOKEN":
            try:
                tmp="NO_ERRORS_GETTING_THEIR_KEY"










                keydir=str(get_their_sv_key_ent.get())
                if keydir[0]==keydir[-1] and keydir[0] in ("'",'"'):
                    keydir=keydir[1:-1]
                try:
                    enc_2=[]
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
                                enc_2.append(keyfile[1][i*us_key_length:(i*us_key_length)+us_key_length])
                            except IndexError:
                                tmp="ARE_ERRORS_GETTING_THEIR_KEY1"
                                get_their_sv_key_ent.delete(0,END)
                                error_lab.place(x=596,y=362)
                                keydir=""
                        for i in range(95):
                            try:
                                us_ab.append(keyfile[1][i+(95*us_key_length)])
                            except:
                                tmp="ARE_ERRORS_GETTING_THEIR_KEY2"
                                get_their_sv_key_ent.delete(0,END)
                                error_lab.place(x=596,y=362)
                                keydir=""
                except FileNotFoundError:
                    keydir=""
                    tmp="ARE_ERRORS_GETTING_THEIR_KEY3"
                    get_their_sv_key_ent.delete(0,END)
                    error_lab.place(x=596,y=362)
                except OSError:
                    keydir=""
                    tmp="ARE_ERRORS_GETTING_THEIR_KEY4"
                    get_their_sv_key_ent.delete(0,END)
                    error_lab.place(x=596,y=362)


            except FileNotFoundError:
                tmp="ARE_ERRORS_GETTING_THEIR_KEY5"
                get_their_sv_key_ent.delete(0,END)
                error_lab.place(x=596,y=362)



                





        if tmp=="NO_ERRORS_GETTING_THEIR_KEY":
            client_thr=threading.Thread(target=Client,args=(target_ip,target_port))
            messenger_thr=threading.Thread(target=Messenger,args=(target_ip,target_port))
            client_thr.start()
            messenger_thr.start()
        else:
            print("NO_ERRORS_GETTING_THEIR_KEY")
            print(tmp)





    def client_clear_to_connect():
        global target_ip,target_port
        try:
            client_thr=threading.Thread(target=Client,args=(target_ip,target_port))
            messenger_thr=threading.Thread(target=Messenger,args=(target_ip,target_port))
            ip_and_port_ent.place_forget()
            ip_and_port_go.place_forget()
            ip_and_port_lab.place_forget()
            back_button.place_forget()
            client_thr.start()
            messenger_thr.start()
            message_to_send_ent.place(x=288,y=350)
            message_to_send_but.place(x=600,y=348)
            message_rcv_txt.pack(side="left",fill="y")
            message_rcv_scb.pack(side="right",fill="y")
            get_their_username_ent.place_forget()
            get_their_username_lab.place_forget()
            get_their_ch_token_ent.place_forget()
            get_their_ch_token_lab.place_forget()
            get_their_sv_key_lab.place_forget()
            get_their_sv_key_ent.place_forget()
            generate_random_token.place_forget()
            error_lab.place_forget()
            scrollbar_cnv.place(x=94,y=20)
            root.bind("<Return>",Startup.send_message)
        except:
            error_lab.place(x=296,y=20)
            print("error :(")
            client_thr._stop()
            messenger_thr._stop()



    def connect_button(event):
        Startup.connect()




    def disconnect():
        target_ip=""
    def host():
        print("HOST SERVER BUTTON")
    def send_message(event):
        Startup.send_msg_button()
    def send_msg_button():
        your_message=str(message_to_send_ent.get())
        FilEncrypt.encrypt(your_message)
        
        message_to_send_ent.delete(0,END)

    def generate_token():
        channel_token=[]
        for i in range(rd.randint(4,8)):
            channel_token.append(allowed_token_chars[rd.randint(0,61)])
        channel_token="%s"%"".join(channel_token[0:])
        get_their_ch_token_ent.delete(0,END)
        get_their_ch_token_ent.insert(0,channel_token)



host_button=Button(root,text="Host",command=Startup.choice_host,width=20,height=5,fg="#f1f1f1",bg="#bb0000")
client_button=Button(root,text="Client",command=Startup.choice_client,width=20,height=5,fg="#f1f1f1",bg="#1f1f1f")
ip_and_port_lab=Label(root,text="Enter the IP and Port\ne.g. \"127.0.0.1:27015\"",width=35,height=2,fg="#f1f1f1",bg="#1f1f1f")
host_port_but=Button(root,text="Host Server",command=Startup.host,width=35,height=3,fg="#f1f1f1",bg="#1f1f1f")
host_port_ent=Entry(root,width=50,fg="#f1f1f1",bg="#1f1f1f")
host_port_lab=Label(root,text="Enter the port\nMust be between 0 and 65535",width=35,height=5,fg="#f1f1f1",bg="#1f1f1f")
host_button.place(x=200,y=200)
client_button.place(x=500,y=200)
error_lab=Label(root,text="Invalid input!",fg="#f1f1f1",bg="#ff0000")
message_to_send_ent=Entry(root,width=45,fg="#f1f1f1",bg="#1f1f1f")
message_to_send_but=Button(root,text="Send",command=Startup.send_msg_button,fg="#f1f1f1",bg="#1f1f1f")
ip_and_port_ent=Entry(root,width=50,fg="#f1f1f1",bg="#1f1f1f")

get_their_username_ent=Entry(root,width=50,fg="#f1f1f1",bg="#1f1f1f")
get_their_username_lab=Label(root,text="Username",width=35,height=1,fg="#f1f1f1",bg="#1f1f1f")

get_their_ch_token_ent=Entry(root,width=50,fg="#f1f1f1",bg="#1f1f1f")
get_their_ch_token_lab=Label(root,text="Channel Token",width=35,height=1,fg="#f1f1f1",bg="#1f1f1f")
generate_random_token=Button(root,text="Generate",command=Startup.generate_token,fg="#f1f1f1",bg="#1f1f1f")

get_their_sv_key_ent=Entry(root,width=50,fg="#f1f1f1",bg="#1f1f1f")
get_their_sv_key_lab=Label(root,text="Server Key Location",width=35,height=1,fg="#f1f1f1",bg="#1f1f1f")


ip_and_port_go=Button(root,text="Connect",command=Startup.connect,width=35,height=1,fg="#f1f1f1",bg="#1f1f1f")
back_button=Button(root,text="Back",command=Startup.go_back,width=5,height=2,fg="#f1f1f1",bg="#1f1f1f")


scrollbar_cnv=Frame(root,height=200)
message_rcv_scb=Scrollbar(scrollbar_cnv)
message_rcv_txt=Text(scrollbar_cnv, height=20, width=80,fg="#f1f1f1",bg="#1f1f1f",spacing1=0,state="disabled")
message_rcv_scb.config(command=message_rcv_txt.yview)
message_rcv_txt.config(yscrollcommand=message_rcv_scb.set,wrap=WORD)
message_rcv_txt.insert(END, messages_to_view)





"""
message_to_send_ent.place(x=288,y=150)
"""






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
    print("CLIENT")
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self,address,port):
        global messages_to_view,client_thr,messenger_thr,target_ip,target_port
        print("initialised client.__init__")
        try:
            Client.sock.connect((address,int(port)))
            client_is_connected_to_svr="1"
        except:
            client_is_connected_to_svr="0"
            try:
                client_thr=threading.Thread(target=Client,args=(target_ip,target_port))
                messenger_thr=threading.Thread(target=Messenger,args=(target_ip,target_port))
            except FileNotFoundError:
                print("FAILURE INITIALISING CLIENT")
        if client_is_connected_to_svr=="1":
            Startup.client_clear_to_connect()
        while client_is_connected_to_svr=="1":
            try:
                last_username=False
                try:
                    data=str(Client.sock.recv(1024))
                except FileNotFoundError:
                    pass
                if not data:
                    print("error NOT DATA")
                FilEncrypt.decrypt(str(data))
                
            except FileNotFoundError:
                pass
class Messenger:
    print("MESSENGER")
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    msngr_afk="0"
    def sendMsg(z_unused_var_Messenger_sendMsg):
        try:
            your_message=str(message_to_send_ent.get())
        except:
            pass







        to_write=[]
        print("TO WRITE IS EMPTY")
        for i in range(len(your_message)):
            try:
                if enc_type=="server":
                    to_write.append(enc[us_ab.index(your_message[i])])
            except IndexError:
                pass
            except ValueError:
                pass
        if len(your_message)>0:
            print("you made it this far ;)")
            if (your_message.split(" ")[0][0])!="/":
                try:
                    while your_message[-1]==" ":
                        your_message=str("%s"%"".join(your_message[0:-1]))
                    to_write=str("%s"%"".join(to_write))
                    if your_message!="":
                        if msngr_afk=="0":
                            self.sock.send(bytes(str(user_token+",msg,"+to_write),"utf-8"))
                        else:
                            print("You are AFK!")
                except ConnectionResetError as e:
                    print(str("\n"+e))
            else:
                print("hai there stranger")
                used_cmd=your_message.split(" ")
                if used_cmd[0] in user_cmds:
                    if used_cmd[0]==user_cmds[0]:
                        print("\"/help\" - brings up this help menu")
                        print("\"/dc\"   - disconnects from the server")
                        print("\"/afk\"  - enables / disables AFK")
                    elif used_cmd[0]==user_cmds[1]:
                        self.sock.send(bytes(str(user_token+",dis, "),"utf-8"))
                        user_can_send_msg="0"
                    elif used_cmd[0]==user_cmds[2]:
                        if msngr_afk=="0":
                            self.sock.send(bytes(str(user_token+",afk, "),"utf-8"))
                            msngr_afk="1"
                        elif msngr_afk=="1":
                            self.sock.send(bytes(str(user_token+",btk, "),"utf-8"))
                            msngr_afk="0"
                else:
                    print("Type \"/help\" for a list of commands")
    def __init__(self,address,port):
        try:
            self.sock.connect((address,int(port)))
            Messenger.sock.send(bytes(str(user_token+",con,"+channel_token+", "),"utf-8"))
            print("\nConnected!\n\n")
            iThread=threading.Thread(target=self.sendMsg,args=())
            iThread.daemon=True
            iThread.start()
            try:
                data=self.sock.recv(1024)
            except ConnectionResetError as e:
                print(str("\n"+e))
            if not data:
                print("error NOT DATA MSNGR")
            data=str(data)
            data_strip=data.split(",")[1:]
            recv_username=data.split(",")[0][2:]
            data_strip[-1]=str("%s"%"".join(data_strip[-1][0:-1]))
        except:
            pass

class FilEncrypt:
    def encrypt(text_to_encrypt):
        global msngr_afk,channel_token,last_username
        if len(text_to_encrypt)>0:
            if str(text_to_encrypt).split(" ")[0] not in user_cmds:
                if msngr_afk=="0":
                    print("THIS IS IT!!!")
                    to_write=[]
                    enc=enc_2
                    for i in range(len(text_to_encrypt)):
                        try:
                            if enc_type=="server":
                                to_write.append(enc[us_ab.index(text_to_encrypt[i])])
                        except IndexError:
                            pass
                        except ValueError:
                            pass
                    your_message="%s"%"".join(to_write)
                    message_to_send=str(user_token+",msg,"+channel_token+","+your_message)
                    Messenger.sock.send(bytes(message_to_send,"utf-8"))
                else:
                    message_rcv_txt.insert(END,"\nYou are AFK!")
                    last_username=False
            else:







                used_cmd=text_to_encrypt.split(" ")
                if used_cmd[0] in user_cmds:
                    message_rcv_txt.configure(state="normal")
                    if used_cmd[0]==user_cmds[0]:
                        message_rcv_txt.insert(END,str("\n\n"
                        +"\n\"/help\"                - brings up this help menu"
                        +"\n\"/dc\"                  - disconnects from the server"
                        +"\n\"/afk\"                 - enables / disables AFK"
                        +"\n\"/newtoken <length>\"   - generates a new channel token"
                        +"\n\"/changetoken <token>\" - lets you switch channels"
                        +"\n\"/currenttoken\"        - displays your current token"
                        +"\n\n"))
                    elif used_cmd[0]==user_cmds[1]:
                        Messenger.sock.send(bytes(str(user_token+",dis,"+channel_token+", "),"utf-8"))
                        message_rcv_txt.insert(END,str("\n\nYou have disconnected from the server.\nPlease close this window as it is no longer needed.\n"))
                        client_thr._stop()
                        messenger_thr._stop()
                        iThread._stop()
                    elif used_cmd[0]==user_cmds[2]:
                        if msngr_afk=="0":
                            Messenger.sock.send(bytes(str(user_token+",afk,"+channel_token+",  "),"utf-8"))
                            msngr_afk="1"
                        elif msngr_afk=="1":
                            Messenger.sock.send(bytes(str(user_token+",btk,"+channel_token+", "),"utf-8"))
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
                                    message_rcv_txt.insert(END,"\nInvalid token length.")
                            except:
                                message_rcv_txt.insert(END,"\nInvalid token length.")


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
                last_username=False
                message_rcv_txt.configure(state="disabled")




                
                
                
                
                
                
                message_rcv_txt.configure(state="disabled")
                message_rcv_txt.see("end")
                    


    def decrypt(text_to_decrypt):
        global messages_to_view,last_username,channel_token,user_token
        try:
            data_strip=text_to_decrypt.split(",")[3:]
            msg_type=text_to_decrypt.split(",")[1]
            recv_ch_token=text_to_decrypt.split(",")[2]
            recv_username=text_to_decrypt.split(",")[0][2:]
            data_strip[-1]=str("%s"%"".join(data_strip[-1][0:-1]))
            data_strip="%s"%",".join(data_strip)
            data_decrypt=[]
            enc=enc_2
            if recv_ch_token==channel_token:
                for i in range(int(int(len(data_strip))/int(len(enc[0])))):
                    try:
                        data_decrypt.append(us_ab[enc.index("%s"%"".join(data_strip[(i*int(len(enc[0]))):(i*int(len(enc[0])))+int(len(enc[0]))]))])
                    except ValueError:
                        pass
                if msg_type=="msg":
                    if "%s"%"".join(data_decrypt)!="":
                        if last_username!=recv_username:
                            received_message=str("\n\n"+recv_username+":\n    "+("%s"%"".join(data_decrypt)))
                        else:
                            received_message=str("\n    "+("%s"%"".join(data_decrypt)))
                        last_username=recv_username
                elif msg_type=="con":
                    received_message=str("\n\n"+recv_username+" has joined the chat room.")
                    last_username=False
                elif msg_type=="dis":
                    received_message=str("\n\n"+recv_username+" has left the chat room.")
                    last_username=False
                elif msg_type=="afk":
                    received_message=str("\n\nUSER \""+recv_username+"\" is now AFK")
                    last_username=False
                elif msg_type=="btk":
                    received_message=str("\n\nUSER \""+recv_username+"\" is no longer AFK")
                    last_username=False
                message_rcv_txt.configure(state="normal")
                message_rcv_txt.insert(END,received_message)
                message_rcv_txt.configure(state="disabled")
                message_rcv_txt.see("end")
        except FileNotFoundError:
            pass








root.mainloop()







"""
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
"""