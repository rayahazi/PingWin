#!/usr/bin/python3.7

from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+'/UI/')
from ReceiverUI import *

def root_validation():
    if os.geteuid() != 0:
        print("Program must be run as ROOT! ")
        exit(1005)

# Global variables:
root_validation() # Check if user is root
instance = None
running=True
i = open("text.icmp", "wb")
d = open("text.dns", "wb")
t = open("text.tcp", "wb")


def packetHandler(packet):
  global running
  print(packet)
  try:
    if packet[ICMP].type==23 and packet[ICMP].code == 5:
      running=False
      return
  except:
    pass
  try:
    packet[Raw].load
  except:
    return
  if ICMP in packet and packet[ICMP].type == 8:   
    i.write(bytes(packet[Raw].load))  
  elif DNS in packet:
    d.write(bytes(packet[Raw].load))  
  elif TCP in packet and packet[TCP].flags.C:
    t.write(bytes(packet[Raw].load))
      
def Listen():
    # Listen to traffic 
    sniffer = AsyncSniffer(prn=packetHandler)
    sniffer.start()

    while running:  
        time.sleep(0.1)
    else:
        print("End Of Traffic packet received")
        sniffer.stop()
        i.close()
        d.close()
        t.close()
        print("Quitting gracfully")

# Main function
def main(inst=None):
    global instance
    instance=inst 

    Listen() 

    if instance != None:
      instance.updater() 
   
if __name__ == '__main__':
  
  main()











