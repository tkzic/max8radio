"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

import socket   # for tcp stuff

# open tcp socket

host = socket.gethostname()
port = 4532                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#s.sendall(b'+F 7012777\n')
#print ("sent nc data")
#data = s.recv(1024)
#s.close()
#print('Received', repr(data))

# define OSC handlers

def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))


def print_f_handler(unused_addr, args, f):
    #print("[{0}] ~ {1}".format(args[0], f))
    print( args[0], f)
    rigstr =  "+F " + str(f) + "\n" 
    bytes_rigstr = str.encode(rigstr)
    s.sendall(bytes_rigstr)  # send message to rigctld


def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=8001, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/filter", print)
  dispatcher.map("/volume", print_volume_handler, "Volume")
  dispatcher.map("/F", print_f_handler, "/F")
  dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()