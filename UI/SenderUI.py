#!/usr/bin/python3.7
from tkinter import *
from colors import *
from tkinter import filedialog 
from PIL import ImageTk, Image
import os,sys
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+'/CORE/')
import pingwinServer

# Global variables:    
filename = "./code.txt"
a = None  # Instance for class 
symbol = None
protocols = [0,0,0]
targetIP = ''
Interfaces = []

# One file scan page:
class OneFile(Tk):

    _Singleton = True

    # Constructor:
    def __init__(self,parent):
        Tk.__init__(self,parent)     
        if OneFile._Singleton==True:
            self.parent = parent
            OneFile._Singleton=self
            self.title("PING-WIN")
            self.geometry('800x600')           
            self.configure(background=Gray)
            self.resizable(0,0)
            self.stateVar = StringVar()
            self.stateVar.set("0 0 0")
            self.fileName = StringVar()
            self.fileName.set("File path: ./code.txt")
            self.var1 = IntVar(value=1)
            self.var2 = IntVar(value=1)
            self.var3 = IntVar(value=1)
            # Interfaces:
            self.targetInterface = Interfaces[0]
            self.iplist = StringVar()
            self.iplist.set(Interfaces[0]) # default value
            self.w = OptionMenu(parent, self.iplist, *Interfaces,command=self.InterfaceChoice).place(x=120,y=260)
            # Ip:
            self.ip = Entry(parent)
            self.ip.place(x=520,y=215) 
            self.ip.focus_set()
            self.ip.insert(0, "127.0.0.1")
            self.ip.bind("<Return>",self.Enter)

            self.texts()
            self.buttons()
            self.img()

        else:
            raise Exception(OneFile._Singleton)  

    def InterfaceChoice(self,value):
        self.targetInterface = value

    def texts(self):
       Label(self,text='ONE FILE SCAN',bg=DarkGray,width='800',fg=Black,height='5',font=('ariel',15)).pack()

    def img(self):
        # Symbol image:
        global symbol
        symbol = PhotoImage(file='A.png')
        panel = Label(self , image = symbol)
        panel.place(x=60, y=115, anchor='sw')

    def buttons(self):
        btn1=Button(self, text='Import file',activeforeground=Gray,bg=Silver,fg=Black,width='9',height='1',border=5,command=UploadAction)     
        btn2=Button(self, text='Send',command=lambda:run_file(),activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5)
        btn3=Button(self, text='EXIT',command=lambda:self.destroy(),activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5)

        btn1.place(x=30, y=150)
        btn2.place(x=320, y=260)
        btn3.place(x=600, y=500)
        filePath=Label(self,textvariable=self.fileName,bg=DarkGray,width='65',fg=Black,height='2',font=('ariel',10)).place(x=160,y=150)
        res=Label(self,textvariable=self.stateVar,bg=DarkGray,width='55',fg=Black,height='6',font=('ariel',15)).place(x=30,y=330)

        Label(self,text="Protocols: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',font=('ariel',10),border=5).place(x=30,y=210)            
        Checkbutton(self, text="ICMP", variable=self.var1,width='8',font=('ariel',10)).place(x=130,y=215)       
        Checkbutton(self,text="DNS-TCP", variable=self.var2,width='8',font=('ariel',10)).place(x=230,y=215)
        Checkbutton(self, text="DNS-UDP", variable=self.var3,width='8',font=('ariel',10)).place(x=330,y=215)      

        Label(self,text="Target: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',font=('ariel',10),border=5).place(x=450,y=210) 
        Label(self,text="Interface: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',font=('ariel',10),border=5).place(x=30,y=262) 

    def Enter(self,event):
        global targetIP 
        targetIP = self.ip.get()    

    # check protocols chosen by user:
    def CheckbuttonRes(self):
        global protocols
        protocols[0]=self.var1.get()  
        protocols[1]=self.var2.get() 
        protocols[2]=self.var3.get() 
        return protocols

    def changePathName(self):
        global filename
        self.fileName.set("File path: "+filename)

    # Update label to show packets running on screen    
    def updater(self,l):
        self.stateVar.set(".\nSent 1 packets.\n"+str(l))
        return   

# function to create Singleton:
def Handle():
    #global a
    try:
        a = OneFile(None)
    except Exception as s:
        a = s
    return a

# Import file to machine:
def UploadAction():
    global filename
    #a.updater(code=1)
    filename =filedialog.askopenfilename()
    a.changePathName() 

# Function to activate 'pingwinServer' file 
def run_file(): 
    global filename 
    global protocols
    global a
    protocols = a.CheckbuttonRes()
    pingwinServer.get_filename(filename,a)  
    #a.updater()   
    
def main():
    global Interfaces
    Interfaces = pingwinServer.Ifaces()
    global a
    a = Handle()
    a.mainloop()   

if __name__=='__main__':
     main()



