#!/usr/bin/env python3

import numpy as np
import socket
import sys
import struct

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        previous = np.array([0, 0, 0])
        while True:
            data = conn.recv(1024)
            data = data.decode()
            #print(data)
            if data == "end":
                print("ending")
                sys.exit(0)
            current = np.fromstring(data, dtype = np.int)
            dist = np.linalg.norm(previous - current)
            vel = dist / 3
            #print(arr)
                #if not data:
                #    pass
                #else:
                #print(arr)
            #if not data:
            #    break
            conn.sendall(struct.pack('f', vel))
            previous = current
                


        
#        previous = beginning
#            print(current)
#            time.sleep(t)
#            previous = current
