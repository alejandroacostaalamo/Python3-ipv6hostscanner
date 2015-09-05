#!/usr/bin/python3

import threading
import sys
import ipaddress
import subprocess
import time

CURRENTPINGS=0 # Number of simultaneous ping at a time

def DOPING6(IPv6ADDRESS):
  global MAXPINGS, CURRENTPINGS
  CURRENTPINGS+=1
  CMD="ping6 -c 3 "+str(IPv6ADDRESS) + " 2> /dev/null > /dev/null"
  return_code = subprocess.call(CMD, shell=True) 
  if return_code == 0:  #If ping was succesful
    print (IPv6ADDRESS," is alive")
  
  CURRENTPINGS-=1
  
def main():
  global MAXPINGS, CURRENTPINGS
  if len(sys.argv) != 3: #Validate how many parameters we are receiving 
    print("  Not enough or too many parameter")
    print("  Usage: ./scanipv6.py IPv6Prefix/lenght MAXPINGS")
    print("  Example: ./scanipv6.py 2001:db8::/64 20")
    print("  Prefix lenght can be between 64-128")
    print("  MAXPINGS corresponds to how many pings will be running at the same time")
    exit()

  SUBNET,MASK=sys.argv[1].split("/")
  MAXPINGS=int(sys.argv[2])

  for addr in ipaddress.IPv6Network(sys.argv[1]):  #Let's loop for each address in the Block
    ping_thread=threading.Thread(target=DOPING6,args=(addr,))

    while CURRENTPINGS >= MAXPINGS: # With this while we make it possible to run max simultaneous pings
      time.sleep(1)  # Let's wait one second before proceeding
      #print ("Interrumping...., CURRENTPINGS > MAXPINGS") #Uncomment this line just for debugging

    ping_thread.start()

main()
