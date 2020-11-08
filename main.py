#!/usr/bin/python3

import http.server
import socketserver
import time
import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of arguments. Run as './main.py time number_of_signals' ")
    else:
        t = int(sys.argv[1])
        n = int(sys.argv[2])
        beginning = np.array([0, 0, 0])
        for i in range(n):
            print(i)
            time.sleep(t)



#PORT = 8080
#handler = http.server.SimpleHTTPRequestHandler

#with socketserver.TCPServer(("", PORT), handler) as httpd:
#    print("serving at port ", PORT)
#    httpd.serve_forever()


