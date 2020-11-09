#!/usr/bin/env python3

import numpy as np
import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data = data.decode()
            #print(data)
            if data == "end":
                print("ending")
                sys.exit(0)
            arr = np.fromstring(data, dtype = np.int)
            #print(arr)
            arr = arr.tobytes()
                #if not data:
                #    pass
                #else:
                #print(arr)
            #if not data:
            #    break
            conn.sendall(arr)
                


