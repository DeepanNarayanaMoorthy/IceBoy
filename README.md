                    ██╗ ██████╗███████╗██████╗  ██████╗ ██╗   ██╗██╗██╗██╗
                    ██║██╔════╝██╔════╝██╔══██╗██╔═══██╗╚██╗ ██╔╝██║██║██║
                    ██║██║     █████╗  ██████╔╝██║   ██║ ╚████╔╝ ██║██║██║
                    ██║██║     ██╔══╝  ██╔══██╗██║   ██║  ╚██╔╝  ╚═╝╚═╝╚═╝
                    ██║╚██████╗███████╗██████╔╝╚██████╔╝   ██║   ██╗██╗██╗
                    ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   ╚═╝╚═╝╚═╝

                    ╔═╗  ╔═╗┬ ┬┌─┐┌┬┐  ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ┬ ┬┬┌┬┐┬ ┬  ┌─┐  ┌┬┐┬ ┬┬┌─┐┌┬┐  ┬
                    ╠═╣  ║  ├─┤├─┤ │   ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││  ││││ │ ├─┤  ├─┤   │ ││││└─┐ │   │
                    ╩ ╩  ╚═╝┴ ┴┴ ┴ ┴   ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  └┴┘┴ ┴ ┴ ┴  ┴ ┴   ┴ └┴┘┴└─┘ ┴   o

======================================================================
# IceBoy
Ice boy is a full duplex chat software for two persons **A** and **B** connected to the same network. But all of this is nothing but a **Cover-Up** for more interesting process that would be running below.This is essentially a **Surveillance System** disguised as a chat app. This project can also br regarded as a **Spyware** 😉

### Explanation Video
To know more about this, [Watch the working demo of IceBoy by clicking on this link](https://drive.google.com/file/d/14S-4tNPZWRizCM974CNbGAb2ro_Bv4Am/view?usp=sharing)


## Lets see how it works
Make sure the persons **A** and **B** have the following files:
| Person A | Person B |
| ------ | ------ |
| Help for Client | Help for Server
| requirements | requirements
| title | title
| zipfile. py | zipfile. py
| libraries.pyw | libraries.pyw
| Client_Server.py | Setup_Server.py
| Secret_accessor.py

To install the required packages: **```pip install -r requirements```**

Let the persons **A** and **B** run _Client_server.py_ and _Setup_Server.py_ respectively and A has to enter the ip address of B which is displayed in their screen. And now we are set to chat! 

To send a message to the other person, just type it and press _enter_. 
And to send a file, type **sendfile** and press _enter_. 

All your chat will be stored in the chatlog file generated and the files you send and receive with be stored in _sendFile.zip_ and _received.zip_ which is also generated.

## What's behind the curtain?
As said, Ice boy is a full duplex chat software for two persons **A** and **B** connected to the same network. But this is just a cover for **Person A** to access the **victim's (Person B)** PC. While Person B can just chat, send and receive files, Person A can do more than that. 

If Person A types **```opensecretaccessor```** and enters the ip obtained by typing **```secretaccessorip```** , he can
  - Get the wifi details of all the networks the device had been connected previously. 
    -  **```wifipasswordstart```** gives the list of the networks previously connected to.
    -  **```passwordof<space><network_name>```** gives the details of the network including the password.
  - Take screenshot
    -  **```screenshot```** receives the screenshot of the victim's PC at that instance.
  - Record audio
    -  **```audio```** asks for the number of seconds the audio has to be recorded and receives the audio for the given length of time.
  - Take picture from webcam
    - **```webcam```** receives the picture taken from the webcam.
  - Keylog
    - **```keylog```** receives everything typing since the system started.

These received files are stored in _file.zip_. Person A can do these additional things even when B's chat is inactive.

## Explanation Video

See This [Explanation Video](https://drive.google.com/file/d/14S-4tNPZWRizCM974CNbGAb2ro_Bv4Am/view) To know more about this Project







