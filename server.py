#!/usr/bin/env python3

import numpy as np
import socket
import sys
import struct
import time

HOST = '127.0.0.1' 
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        previous = conn.recv(1024)
        previous = np.fromstring(previous.decode(), dtype = np.int)
        t_start = time.time()

        while True:
            data = conn.recv(1024)
            t_end = time.time()
            data = data.decode()
            if data == "end":
                print("Last position has been sent. Ending server's work")
                s.close()
                sys.exit(0)
            current = np.fromstring(data, dtype = np.int)
            dist = np.linalg.norm(previous - current)
            vel = dist / (t_end - t_start)
            conn.sendall(struct.pack('f', vel))
            previous = current
            t_start = t_end
