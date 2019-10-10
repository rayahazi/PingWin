#!/usr/bin/python3.7
from tkinter import *
from colors import *
from tkinter import filedialog 
from PIL import ImageTk, Image
import os,sys
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+'/CORE/')
import pingwinClient

# Global variables:
filename=""
ctr=0
string=[]
a=None
symbol = None

class OneFileReceiver(Tk):
    
    _Singleton = True
    
    def __init__(self,parent):
        Tk.__init__(self,parent) 
        if OneFileReceiver._Singleton==True:
            self.parent = parent
            OneFileReceiver._Singleton=self
            self.title("PING-WIN")
            self.geometry('800x600')
            self.configure(background=Gainsboro)
            self.resizable(0,0)
            self.stateVar = StringVar()
            self.stateVar.set('File')
            self.texts()
            self.buttons()
            self.img()
        else:
            raise Exception(OneFileReceiver._Singleton)

    def texts(self):
       Label(self,text='RECEIVER',bg=DarkGray,width='800',fg=Black,height='5',font=('ariel',15)).pack()

    def img(self):
        # Symbol image:
        global symbol
        symbol = PhotoImage(file='A.png')
        panel = Label(self , image = symbol)
        panel.place(x=60, y=115, anchor='sw')

    def buttons(self):       
        btn1=Button(self, text='Start scanning',command=lambda:pingwinClient.main(a),activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5)     
        btn2=Button(self, text='EXIT',command=self .destroy,activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5)
        btn1.place(x=320, y=150)
        btn2.place(x=600, y=500)
        
        res=Label(self,textvariable=self.stateVar,bg=DarkGray,width='50',fg=Black,height='5',font=('ariel',15)).place(x=50,y=220)
        
    def change(self): 
        Button(self, text="text.icmp",command=lambda:openFolder("text.icmp"),activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5).place(x=50, y=350)
        Button(self, text="text.dns",command=lambda:openFolder("text.dns"),activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5).place(x=250, y=350)
        Button(self, text="text.tcp",command=lambda:openFolder("text.tcp"),activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5).place(x=450, y=350)  

    # Update label to show fList running on screen      
    def updater(self):
        global ctr        
        if ctr < len(string):
            self.stateVar.set(string[ctr])
            self.after(50, self.updater)
            ctr += 1           
        else:
            ShowRes()
            #sentence = str(Receiver.packetsLen)+' packets captured\n0 packets dropped by kernel'
            sentence = 'End of sniffing\nAll packets captured by system\nPress the buttons below to open received files'
            self.stateVar.set(sentence)     
            return
      
    # Change output in label 'res'       
    def changeString(self,g):
        global string     
        string.append(g) 

# function to create Singleton:
def Handle():
    global a
    try:
        a = OneFileReceiver(None)
    except Exception as s:
        a = s
    return a
          
def openFolder(nameOfFile):
    os.system("xdg-open /PingWin/UI/"+nameOfFile)

def ShowRes():  
    global a 
    a.change()

if __name__=='__main__':
    a = Handle()
    a.mainloop()   

