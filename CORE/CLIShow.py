#!/usr/bin/python3.7
from pingwinServer import *

def logo():
    l = '''
                 .+##*+==.        
             .%@@@%=:.        
            .#=##*:           
            =:   :=            _   _   _   _       _   _   _
          .*-     -=          / \ / \ / \ / \     / \ / \ / \ 
        .+@@.      *#:       ( P | I | N | G |   ( W | I | N )
      .+@%%@-      +@@+.      \_/ \_/ \_/ \_/     \_/ \_/ \_/
     :@%=.#%.      +:+@@=.    
    :%-.  *-       +  .+@+         Author: Raya Hazi 
    :.    :-      .=    .-    
          .*.  ...=.          
        .:-++==+**-:.  
    [+] Author: Raya Hazi
    [+] github: 'https://github.com/rayahazi'
    [+] Description: DL tool through ICMP, DNS, and DNS-TCP protocols.
    Pingwin version  0.1
    '''
    return l

help = '''
Usage: pingwin [options]... [FILE]
Data leak tool through ICMP, DNS, and DNS-TCP protocols.

- [ Options Sender ] -

  -s, --send               Use Sender module to send file
  -f, --file               Path to file 
  -p, --protocol           Select through which protocol to send file. See options below. 
  -i, --interface          Select specific interface
  -t, --ip                 IP target (IPv4 or IPv6)
  -c, --cron               Create schudled task for Pingwin program. 
  -h, --help               Display this help and exit
  -v, --version            Output version information and exit

Example:
  sudo python3 pingwinServer.py                                                     Sends default file to localhost through all protocols.
  sudo python3 pingwinServer.py -t 8.8.8.8  -f "/home/secretFile.txt" -p icmp dns   Sends file to given IP through ICMP and DNS protocols.                                                      

- [ Protocol types ] -
As default file will be sent through all protocols. 
* ICMP
* DNS
* DNS - TCP (write as dnstcp)


- [ Options Receiver ] -

  -r, --receive            Use Receiver module to receive file
  -i, --interface          Select specific interface

Example:
  sudo python3 pingwinClient.py               Receive file from Sender module. 
  sudo python3 pingwinServer.py -r -i lo      Receive file from Sender module only through speficif interface.

- [ Cron task ] -
Make a schudled task for DL check. 
Use: $ pingwinCron.sh [STARS] [USERNAME]
Example:
pingwinCron.sh 10**** Joe    
'''
