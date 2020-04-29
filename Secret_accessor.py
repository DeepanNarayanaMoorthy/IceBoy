import time, socket, sys, pyautogui
def popup2(a):
    pyautogui.alert(str(a), "ALERT")
print('Client Server...')
time.sleep(1)
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
port = 1244
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")

while 1:
    message = input("Your Message: ")
    if(message=='bye'):
        exit()
    soc.send(bytes(message,'UTF-8'))
    if (message == 'webcam'):
        message = input("press s to recieve the image(press after 6 seconds for best quality): ")
        soc.send(bytes(message,'UTF-8'))
    if (message == 'audio'):
        message = input("ENTER NUMBER OF SECONDS: ")
        soc.send(bytes(message,'UTF-8'))
        message = input("PRESS s TO START: ")
        soc.send(bytes(message,'UTF-8'))
    with open('file.zip', 'wb+') as output:
        rec = soc.recv(9000000)
        output.write(rec)
    popup2("FILE RECIEVED")
soc.close()


