import socket
import sys

sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

HOST_SRC = sys.argv.pop() if len(sys.argv) == 3 else "localhost"
PORT_NUM = 1060

if sys.argv[1:] == ["server"]:
    sock.bind((HOST_SRC,  PORT))
    sock.setsockopt(socket.SO_REUSEADDR, socket.SOL_SOCKET,  1)
    sock.listen(1)
    try:
        print('Connection Success:',  sock.getsockname())
    except:
        TypeError
    src,  namesocket = sock.accept()
    try:
        print('Recieved from',  namesocket)
    except:
        TypeError
    src.shutdown(socket.SHUT_WR)
    mail = b''
    while True:
        beyond = src.recv(80)
        if not beyond:
            break
        mail += beyond
        
    print('Incoming mail has recieved')
    print(mail.decode('ascii'))
    src.close()
    sock.close()
    
else:
    print('testing: connection[client_src[host_dst]', file=sys.stderr)
