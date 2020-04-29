import time, socket, sys, pyautogui
import os
import win32process, easygui
from pexecute.thread import ThreadLoom
import tkinter
import tkinter.filedialog
from zipfile import *
fqq=open('title','r',encoding="utf-8")
print(fqq.read())
fqq.close()
print('WELCOME TO THE CHAT, King !')
ff=open('Help For Client','r')
pyautogui.alert(ff.read(),'PLEASE READ THIS CAREFULLY')
ff.close()
time.sleep(1)
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
server_host = input('Ask your friend for their IP address ( displayed in their window ):')
port = 1234
time.sleep(1)
soc.connect((server_host, port))
socb = socket.socket()
shostb = socket.gethostname()
ipb = socket.gethostbyname(shostb)
print('Your Computer Information : ',shostb, '({})'.format(ipb))
portb = 1235
time.sleep(1)
socb.connect((server_host, portb))

def fun1():
    while(True):
        message = soc.recv(1024)
        message = message.decode()
        if(message=='sendfile'):
            pyautogui.alert( 'YOUR Friend WANTS TO SEND A FILE PRESS OK TO RECIEVE', "ALERT")
            with open('recievedfile.zip', 'wb+') as output:
                    rec = soc.recv(9000000)
                    output.write(rec)
                    pyautogui.alert( "FILE RECIEVED",'ALERT')
            continue
        try:
            chat='Client > '+message+'\n'
            f = open("chatlog_Client.txt", "a+")
            f.write(chat)
            f.close()
            pyautogui.alert( message, "Your Friend Says")
        except:
            pass
def fun2():
    while(True):
        messageb = input(str("Me > "))
        if(messageb=='opensecretaccessor'):
            try:
                os.system('Secret_accessor.py')
            except:
                continue
            continue
        if(messageb=='help'):
            fb = open("Help for Client", "r")
            try:
                pyautogui.alert( fb.read(), "HELP ")
                fb.close()
                continue
            except:
                pass
            
        if(messageb=='sendfile'):
            socb.send(messageb.encode())
            try:
                fname = easygui.fileopenbox()
                with ZipFile('sendFILE.zip', 'w') as myzip:
                    myzip.write(fname)
                with open ('sendFILE.zip','rb') as f1:
                    socb.send(f1.read(9000000))
                os.remove('sendFILE.zip')
                pyautogui.alert( 'FILE SENT', "ALERT ")
            except:
                continue            
        meslist=messageb.split()
        messageb=messageb+'\n'
        chatb='You > '+messageb
        fxx = open("chatlog_Client.txt", "a+")
        fxx.write(chatb)
        fxx.close()
        socb.send(messageb.encode())
        if(messageb=='bye'+'\n'):
            exit()
            
loom = ThreadLoom(max_runner_cap=10)
loom.add_function(fun1, [], {})
loom.add_function(fun2, [], {})

output = loom.execute()

