#!/usr/bin/python3.7
from scapy.all import *
import sys,os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+'/UI/')
from SenderUI import *
from CLIShow import *


def root_validation():
    if os.geteuid() != 0:
        print("Program must be run as ROOT! ")
        exit(1005)

# Global variables (default attributes):
root_validation() 
f = './code.txt'
filename = open(f, "r")
hostname = "127.0.0.1"
a = None
targetInterface = None
protocols = [1,1,1]
protocolsNames = ["ICMP","DNS","DNSTCP"]
version = 0.1

def get_filename(fileFromUser, x):
    '''
    Function for UI - get filename from the user's choice
    get instance of SenderUI class as a
    '''
    global filename
    global a
    global hostname
    global f
    hostname = targetIP
    filename = open(fileFromUser, "r")
    f = fileFromUser
    a = x # instance
    main()

def endSession():
    '''
    Function to send ICMP packet that represents EOF. 
    '''
    send(IP(dst=hostname)/ICMP(type=23,code=5))
    print("Send end")

def sendProtocols():
    '''
    Function to send the file chosen by user or default through specific protocols:
    ICMP, DNS, DNS-TCP
    '''
    global targetInterface
    global filename
    global protocols
    # If there is UI
    if a != None:
        protocols = a.CheckbuttonRes()

    # ICMP    
    if protocols[0]==1:  
        try:
            for l in filename.read(16284):  
                send(IP(dst=hostname)/ICMP()/Raw(load=l),iface=targetInterface)
        # Case of IMG files:
        except:
                filename = open(f, "rb")
                for l in filename.read(16284):  
                    send(IP(dst=hostname)/ICMP()/Raw(load=l),iface=targetInterface)
     # DNS_UDP
    if protocols[1]==1:     
        filename.seek(0)
        try:
            for l in filename.read(16284):  
                send(IP(dst=hostname)/UDP()/DNS()/Raw(load=l),iface=targetInterface)
        except:
                filename = open(f, "rb")
                for l in filename.read(16284):  
                    send(IP(dst=hostname)/UDP()/DNS()/Raw(load=l),iface=targetInterface)
    # DNS_TCP
    if protocols[2]==1:
        filename.seek(0)
        try:
            for l in filename.read(16284):  
                send(IP(dst=hostname)/TCP( flags="C")/Raw(load=l),iface=targetInterface)
        except:
                filename = open(f, "rb")
                for l in filename.read(16284):  
                    send(IP(dst=hostname)/TCP( flags="C")/Raw(load=l),iface=targetInterface)

def Ifaces():
    ''' 
    Function to return list of interfaces from the user's computer
    '''
    output = subprocess.check_output("ifconfig -a | sed 's/[ \t].*//;/^$/d'", shell=True)
    output=output.decode("utf-8") 
    IfaceNum = output.count("\n")
    i=0
    j=1
    IfaceArr = []
    IfaceArr = IfaceArr + [0]*(IfaceNum - len(IfaceArr))
    while IfaceNum:
        IfaceArr[i] = output.split(":\n",j)[i] 
        i += 1
        j += 1
        IfaceNum -= 1
    return IfaceArr

def main():
    sendProtocols()
    endSession() 

def err_message(val):
    m = "pingwin: invalid option -- '{}'\nTry 'pingwin --help' for more information.".format(val)
    print(m)
    exit()

def cronTabTask(stars,user):
    s = "'cronjob='{} /PingWin/CORE/Sender.py' (crontab -u {} -l; echo '$cronjob' ) | crontab -u {} -".format(stars,user,user)
    os.system(s) 
    print("[+] Cronjob created successfully")
    exit()

clear = lambda: os.system('clear') 

def Menu():
    global filename
    global targetInterface
    global hostname
    global protocols
    global f

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            clear()
            print(logo(),help)
            exit()
        if sys.argv[i] == "-v" or sys.argv[i] == "--version":
            print("Pingwin version " ,version)
            exit()
        if sys.argv[i] == "-c" or sys.argv[i] == "--cron":
            aa = re.match(r"^\\s*($|#|\\w+\\s*=|(\\?|\\*|(?:[0-5]?\\d)(?:(?:-|\/|\\,)(?:[0-5]?\\d))?(?:,(?:[0-5]?\\d)(?:(?:-|\/|\\,)(?:[0-5]?\\d))?)*)\\s+(\\?|\\*|(?:[0-5]?\\d)(?:(?:-|\/|\\,)(?:[0-5]?\\d))?(?:,(?:[0-5]?\\d)(?:(?:-|\/|\\,)(?:[0-5]?\\d))?)*)\\s+(\\?|\\*|(?:[01]?\\d|2[0-3])(?:(?:-|\/|\\,)(?:[01]?\\d|2[0-3]))?(?:,(?:[01]?\\d|2[0-3])(?:(?:-|\/|\\,)(?:[01]?\\d|2[0-3]))?)*)\\s+(\\?|\\*|(?:0?[1-9]|[12]\\d|3[01])(?:(?:-|\/|\\,)(?:0?[1-9]|[12]\\d|3[01]))?(?:,(?:0?[1-9]|[12]\\d|3[01])(?:(?:-|\/|\\,)(?:0?[1-9]|[12]\\d|3[01]))?)*)\\s+(\\?|\\*|(?:[1-9]|1[012])(?:(?:-|\/|\\,)(?:[1-9]|1[012]))?(?:L|W)?(?:,(?:[1-9]|1[012])(?:(?:-|\/|\\,)(?:[1-9]|1[012]))?(?:L|W)?)*|\\?|\\*|(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(?:(?:-)(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?(?:,(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(?:(?:-)(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?)*)\\s+(\\?|\\*|(?:[0-6])(?:(?:-|\/|\\,|#)(?:[0-6]))?(?:L)?(?:,(?:[0-6])(?:(?:-|\/|\\,|#)(?:[0-6]))?(?:L)?)*|\\?|\\*|(?:MON|TUE|WED|THU|FRI|SAT|SUN)(?:(?:-)(?:MON|TUE|WED|THU|FRI|SAT|SUN))?(?:,(?:MON|TUE|WED|THU|FRI|SAT|SUN)(?:(?:-)(?:MON|TUE|WED|THU|FRI|SAT|SUN))?)*)(|\\s)+(\\?|\\*|(?:|\\d{4})(?:(?:-|\/|\\,)(?:|\\d{4}))?(?:,(?:|\\d{4})(?:(?:-|\/|\\,)(?:|\\d{4}))?)*))$",sys.argv[i+1])
            if aa != None:
                stars = sys.argv[i+1]
            else:
                err_message(sys.argv[i])
            try:
                pwd.getpwnam(sys.argv[i+2])
                user = sys.argv[i+2]
            except KeyError:
                print('User name does not exist.')
                err_message(sys.argv[i])
            cronTabTask(stars,user)
            exit()
        if sys.argv[i] == "-i":
            interfaces = Ifaces()
            if sys.argv[i+1] in interfaces:
                targetInterface = sys.argv[i+1]
            else:
                err_message(sys.argv[i])
        elif sys.argv[i] == "-t":
            aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",sys.argv[i+1])
            if aa != None:
                hostname = sys.argv[i+1]
            else:
                err_message(sys.argv[i])
        elif sys.argv[i] == "-f":
            if os.path.isfile(sys.argv[i+1]) == True:
                f = sys.argv[i+1]
                filename = sys.argv[i+1]
            else:
                err_message(sys.argv[i])
        elif sys.argv[i] == "-p":
            protocols = [0,0,0]
            try:
                while '-' not in sys.argv[i+1]:
                    if sys.argv[i+1].upper() in protocolsNames:
                        if sys.argv[i+1] == "ICMP" or sys.argv[i+1] == "icmp":
                            protocols[0] = 1
                            print("i")
                        elif sys.argv[i+1] == "DNS" or sys.argv[i+1] == "dns":
                            protocols[1] = 1
                            print("d")
                        elif sys.argv[i+1] == "DNSTCP" or sys.argv[i+1] == "dnstcp":
                            protocols[2] = 1
                        i += 1
                    else:
                        err_message(sys.argv[i])
            except:
                pass

if __name__=='__main__':
    '''
    If program runs from CLI  
    '''  
    Menu() # in CLIShow module
    main()
