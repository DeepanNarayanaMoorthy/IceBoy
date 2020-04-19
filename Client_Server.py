import time, socket, sys, pyautogui
import ctypes  # An included library with Python install.
import os
import win32process, easygui
from pexecute.thread import ThreadLoom
import tkinter
import tkinter.filedialog
from zipfile import *
def popup(b):
    ctypes.windll.user32.MessageBoxW(0, str(b), 'ALERT', 1)
    ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
def popup2(a):
    pyautogui.alert(str(a), "Title")
print('WHECOME TO THE CHAT Client')
f = open("chatlog_Client.txt", "a")
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
            try:
                ctypes.windll.user32.MessageBoxW(0, 'YOUR Friend WANTS TO SEND A FILE PRESS OK TO RECIEVE'
                                                 , "ALERT", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
            except:
                pass
            with open('recievedfile.zip', 'wb+') as output:
                    rec = soc.recv(9000000)
                    output.write(rec)
                    popup2("FILE RECIEVED")
            continue
        try:
            chat='Client > '+message+'\n'
            f.write(chat)
            ctypes.windll.user32.MessageBoxW(0, message, "Your Friend Says", 1)
            ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
        except:
            pass
def fun2():
    while(True):
        messageb = input(str("Me > "))
        if(messageb=='help'):
            fb = open("Help for Client.txt", "r")
            try:
                ctypes.windll.user32.MessageBoxW(0, fb.read(), "HELP ", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
                fb.close()
                continue
            except:
                pass
            
        if(messageb=='sendfile'):
            socb.send(messageb.encode())
            root = tkinter.Tk()
            root.withdraw() 
            fname = tkinter.filedialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
##            dname = easygui.enterbox("ENTER THE ADDRESS OF THE DIRECTORY")
##            fname = easygui.enterbox("ENTER THE NAME OF THE FILE")
##            fname=dname+'/'+fname
            fname=list(fname)
            fname=['//' if x=='/' else x for x in fname]
            str1 = " " 
            fname=str1.join(fname)
            fname=fname.replace(' ','',100)
            
            with ZipFile('sendFILE.zip', 'w') as myzip:
                myzip.write(fname)
            with open ('sendFILE.zip','rb') as f1:
                socb.send(f1.read(9000000))
            try:
                ctypes.windll.user32.MessageBoxW(0, 'FILE SENT', "ALERT ", 1)
                ctypes.user32.ShowWindow(ctypes.kernel32.GetConsoleWindow(), 0)
            except:
                pass
            continue
        meslist=messageb.split()
        messageb=messageb+'\n'
        chatb='You > '+messageb
        f.write(chatb)
        socb.send(messageb.encode())
        if(messageb=='bye'+'\n'):
            f.close()
            exit()
            
loom = ThreadLoom(max_runner_cap=10)
loom.add_function(fun1, [], {})
loom.add_function(fun2, [], {})

output = loom.execute()

