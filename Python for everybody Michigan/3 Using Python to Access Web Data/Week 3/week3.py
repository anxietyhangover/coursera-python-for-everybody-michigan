import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.py4inf.com',80))
sock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
data = sock.recv(512)
while len(data) > 1:
    print(data)
    data = sock.recv(512)
sock.close