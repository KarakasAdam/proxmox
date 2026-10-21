import socket
cim=input("Add meg a cimet!: ")
kapcs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
kapcs.connect((cim,80))
kapcs.send(b"GET / HTTP/1.1\r\nHost: "+bytes(cim,"utf8")+b"\r\nConnection: close\r\n\r\n")
valasz=kapcs.recv(10000)
kapcs.shutdown(socket.SHUT_RDWR)
kapcs.close()
print(repr(valasz))






