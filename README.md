# FilEncrypt-Server
Encrypted chat server for anonymous messaging

Allows you to send completely encrypted messaages to other people.

This only allows you to encrypt ASCII, and anything that isn't ASCII either won't be read by the scripts or will crash your client.

Made and owned by J4TPlays


## How to use the FilEncrypt Server (version 1.X ~ 2.X)
### Hosting
To host a server, you will need a portforwarded router if you wish to communicate with people on a different network. Simply run the script, type the word `host` and type the port you wish to use. As long as the port isn't in use, your server will work. It's that simple. Just ensure that if you do want to communicate with people on a different network, your router is portforwarded and your computer's firewall isn't blocking incoming and outgoing connections on that port. If people are unable to connect, this is most likely the issue.

### Connecting
To connect, you need to run two instances of the server script. This basically means that you need to open it twice.
To be able to read messages, on one of the windows you must type the word `client`, and simply follow the instructions on screen. Once you are connected, you will get a notification telling you that you are connected.
To be able to send messages, on the other window you must type the word `messenger`, and simply follow the instructions on screen. Again, once you are connected you will get a notification telling you that you are connected to the server.

### Generating a key
To generate a key, you'll need to use the FilEncrypt scripts (available on the [FilEncrypt repository](https://github.com/J4TPlays/FilEncrypt)). You'll need to select the key generation for the server (it's directly underneath **unSept**). Provided you follow all instructions correctly, everything should work with no issues.


## 
## Plans for the future
### 4.0
#### These are some of the updates coming to FE-Server 4.0 and FE-Client 4.0
##### Client / Server separation
- Version 2.X and 3.X are no longer going to be supported. Instead, when new versions of the FilEncrypt server are released, there will be 2 files, called `FE-Server X.X.X.pyw` and `FE-Client X.X.X.pyw`. This will stop confusion when downloading files for your use.
##### Verifying connections
- FilEncrypt server will be more aware of what's being sent. The connected clients will be given a static UUID (Universal Unique Identifier) that will be unique to them, and when messages are send from the clients, the server will receive the message and check the static UUID against a database. If the static UUID is in the database, then the server will send to every client their message, along with a dynamic UUID given only when the user connects. When the user disconnects, their dynamic UUID will be deleted from the server's database - this will not delete their static UUID. However, if the client's static UUID is not in the server's databasea, the server will completely ignore the message. This will be a huge security fix and should almost completely stop DDoS possibilities.
##### Storing server data
- FilEncrypt client will give you a `userdata.info` file when you load up the client for the first time, and will from then on rely on that file so that you don't have to remember all the information to send data to the server. Just remember that the server will be able to remove your static UUID at any time, so if you do give your static UUID out, the server can remove the statid UUID from its database. If someone has your static UUID, you'll have to request a new one from the server host.
##### SFTP (Secure File Transfer Protocol)
- FE-Server 4.0 will have full capability of transferring files over from one client to another. This will work a little differently to most methods of FTP, as the server will not store anything sent by the user. This means that the server will not actually keep track of what is being sent. It will, however, be able to cap the packets being sent. This means users who are requesting a file will not be able to be sent too much data, resulting in filled storage devices. The server will do this by storing the file's size and the length of the key that is used by the file owner.
##### Keys
- FilEncrypt 3.0 now gives the user access to the new binary keys which will stop encrypting set bytes, and instead will encrypt everything that is in the file. This allows things like images, Word documents, etc. to be encrypted without an issue of crashing the scripts.








## 
## Questions you may have
### Is it secure?
The FilEncrypt server started off as an unencrypted server (version 1.0.X) as a test to see what I could do with the server. I then realised I could implement a lot of security into the program, which is where I got the idea of an encrypted chat server. Everything that gets sent to the server is encrypted before it's sent (only on versions 2.X or later), meaning nothing can be understood by people trying to read the data being sent, except for the clients who are:
1. Using the same key
2. Connected to the same server
3. Using the same channel token

If someone only has access to the channel token or is connected to the same server, or both, then the messages will either come out as gibberish, or will be very badly decrypted. The only way to guarantee the decryption of the messages **completely** is to use the exact same key, which is extremely unlikely given the strength of each key's random generation, even for a low character substitution.

Just remember that if you do connect to someone's server from a different network, they will have your public IP address. This means they can do whatever they like with it; they can remove you from the server if they wish, or potentially illegal things as well, such as DDoS attacks (information on DDoSing the chat server is below).


### Can the chat server be DDoSed?
Of course. There's no absolute way to ensure your server isn't DDoSed.
However, there are going to be a lot of precautions in place for the server receiving messages which will ignore messages that don't meet the exact requirements of a message. 


### Where's the GUI? Command line is horrible!
A public **beta test version** of 3.X is available, and includes a graphical user interface (GUI) using Tkinter. If you are running a version of Python 3 that doesn't support Tkinter, you'll need to find a way of installing it since versions 2.X and 3.X will no longer be supported after the release of version 4.0. 


##
## Reporting issues
Feel free to leave comments on the repository, I'll try to respond to them as soon as possible. I'm most interested in the security of the chat server so if you have any issues, I'll do my best to fix them. :)


##
## Update Log

### Version 3.X


#### 3.0.2
- fixed a fatal issue where the client would crash every time it would find an empty message. Empty messages will now be replaced with `[?]`

#### 3.0.1
- fixed the issue when typing `/dc` where the server would constantly add your previous message. The command will now close down your instance of the server. The `/dc` command **may** be removed in version 3.1, depending on its requirement now that the "X" button will send a disconnect message.
- added a label to top left displaying the chat server's version



#### 3.0.0
- Released as a public beta test version. There are bound to be issues with this, so if and when you find issues, please report them as soon as you can.
- Added a GUI using Tkinter. If your computer does not have Tkinter, you might be forced to use the command line version. Again, any issues, report them to me.



### Version 2.X

#### 2.3.0
- Allows messages to be encrypted before they're sent and decrypted when they're received. The only thing the server host will understand is what data is being sent. It will not have a clue what the message is other than that it's been sent by someone, and that it needs to send it out to all of the connected clients.
- Previous versions of 2.X will not be released as they were very unstable and are unnecessary to fix.

### Version 1.X

#### 1.0.0
- Extremely basic communication, which doesn't include any kind of encryption / decryption. This version should only be used if you really don't care about people reading your messages. Version 1.0 will not be updated to include encryption / decryption.





##### Please do not use for illegal purposes. I will not be held liable for any illegal activity caused by this Python program.
