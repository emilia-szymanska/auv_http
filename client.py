#!/usr/bin/env python3

import socket
import numpy
import time
import numpy as np
import sys
import struct

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

START = np.array([0, 0, 0])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of arguments. Run as './main.py time number_of_signals' ")
    else:
        t = int(sys.argv[1])
        n = int(sys.argv[2])
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(START.tobytes())

            for i in range(n):
                time.sleep(t)
                current = np.random.randint(1, high=30, size=3)
                current = current.tobytes()
                s.sendall(current)
                data = s.recv(1024)
                vel = struct.unpack('f', data)[0]
                print('Current velocity: ', round(vel, 3))
        
            s.sendall(b'end')
