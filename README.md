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
To be able to read messages, pn one of the windows you must type the word `client`, and simply follow the instructions on screen. Once you are connected, you will get a notification telling you that you are connected.
To be able to send messages, on the other window you must type the word `messenger`, and simply follow the instructions on screen. Again, once you are connected you will get a notification telling you that you are connected to the server.

### Generating a key
To generate a key, you'll need to use the FilEncrypt scripts (available on the FilEncrypt repository). You'll need to select the key generation for the server (it's directly underneath **unSept**). Provided you follow all instructions correctly, everything should work with no issues.

## 
## Questions you may have
### Is it secure?
The FilEncrypt server started off as an unencrypted server (version 1.0.X) as a test to see what I could do with the server. I then realised I could implement a lot of security into the program, which is where I got the idea of an encrypted chat server. Everything that gets sent to the server is encrypted before it's sent (only on versions 2.X or later), meaning nothing can be understood by people trying to read the data being sent, except for the clients who are:
1. Using the same key
2. Connected to the same server
3. Using the same channel token
If someone only has access to the channel token or is connected to the same server, or both, then the messages will either come out as gibberish, or will be very badly decrypted. The only way to guarantee the decryption of the messages **completely** is to use the exact same key, which is extremely unlikely given the strength of each key's random generation, even for a low character substitution.




## Reporting issues
Feel free to leave comments on the repository, I'll try to respond to them as soon as possible





## Update Log
### 1.0.0
- Basic
