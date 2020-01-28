import socket as sck

s=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect(("127.0.0.1",5000))
print("connesso")
stringInviare= "Get http://127.0.0.1:5000/register HTTP/1.1 \n\n"
#stringInviare= "Get http://127.0.0.1:5000/login HTTP/1.1 \n\n"
s.sendall(stringInviare.encode())
dataByte=s.recv(4096)
file=open("html.html","w")
while dataByte != b'':
    dataByte = s.recv(4096)
    print(dataByte.decode())
    file.write(dataByte.decode())
file.close()
s.close()
