#!/usr/bin/env python3

import socket
import numpy
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

x = numpy.array([0, 0, 0])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    x = x.tobytes()
    s.sendall(x)
    data = s.recv(1024)
    print('Received', repr(data))
    time.sleep(3)
    s.sendall(x)
    data = s.recv(1024)
    print('Received', repr(data))
    s.sendall(b'end')


#!/usr/bin/python3

#import http.server
#import socketserver
#import time
#import numpy as np
#import sys

#if __name__ == "__main__":
#    if len(sys.argv) != 3:
#        print("Wrong number of arguments. Run as './main.py time number_of_signals' ")
 #   else:
#        t = int(sys.argv[1])
#        n = int(sys.argv[2])

#        beginning = np.array([0, 0, 0])
        
#        previous = beginning
#        for i in range(n):
#            current = np.random.randint(-30, high=30, size=3)
#            dist = np.linalg.norm(previous - current)
#            vel = dist / t
#            print(vel)
#            print(current)
#            time.sleep(t)
#            previous = current



#PORT = 8080
#handler = http.server.SimpleHTTPRequestHandler

#with socketserver.TCPServer(("", PORT), handler) as httpd:
#    print("serving at port ", PORT)
#    httpd.serve_forever()

