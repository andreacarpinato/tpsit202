import socket as sck
import random



def generate():
    numeri=[]
    name=[]
    numeri=['10','99','98','74','2000','2001','01','77']
    name=['andrea','andre','marco','filippo','lollo','elena','alice','maria']
    na=random.randint(0,7)
    nu=random.randint(0,7)
    print(name[na])
    nome=name[na]+numeri[nu]
    password=random.randint(1000,999999)
    print(nome)
    print(password)
    lunghezza=len(nome)+len(str(password))+30
    print(lunghezza)
    return nome,password,lunghezza

#def registraBot():
IP="127.0.0.1"
s=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect((IP,5000))
print("connesso")
name,password,lenght=generate()
stringInviare= "Post /register HTTP/1.1\r\n"+ \
    "Host: 127.0.0.1:5000\r\n" + \
    "Content-Length:"+str(lenght)+"\r\n" + \
    "Content-Type: application/x-www-form-urlencoded\r\n\r\n" + \
    "username="+name+"&password="+str(password)+"&confirmPassword="+str(password)
s.sendall(stringInviare.encode())
dataByte=s.recv(4096)
file=open("html.html","w")

while dataByte != b'':
    dataByte = s.recv(4096)
    print(dataByte.decode())
    file.write(dataByte.decode())
file.close()
s.close()



