#!/usr/bin/python3.7
from tkinter import *
from colors import *
from tkinter import filedialog 
from PIL import ImageTk, Image
import os,sys, subprocess
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+'/CORE/')
import pingwinServer

# Global variables:    
filename=""
a=None  # Instance for class 
symbol = None           

WEEKDAYS = ["*",'Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']
MONTHS = ["*",'January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'] 

# One file scan page:
class CronTaskUI(Tk):

    _Singleton = True

    # Constructor:
    def __init__(self,parent):
        Tk.__init__(self,parent)     
        if CronTaskUI._Singleton==True:
            self.parent = parent
            CronTaskUI._Singleton=self
            self.title("PING-WIN")
            self.geometry('800x600')           
            self.configure(background=Gainsboro)
            self.resizable(0,0)  
            self.stateVar = StringVar()

            # Variables:
            self.mi = IntVar(value=0)
            self.h  = IntVar(value=0)
            self.d  = IntVar(value=0)
            self.mo = None
            self.w  = None
            
            # Menu for crontab:
            self.minutes = Spinbox(parent, from_=0,to=60,width=6,font=('ariel',14),textvariable=self.mi).place(x=60,y=190)
            self.hours = Spinbox(parent, from_=0,to=12,width=6,font=('ariel',14),textvariable=self.h).place(x=200,y=190)
            self.days = Spinbox(parent, from_=0,to=365,width=6,font=('ariel',14),textvariable=self.d).place(x=340,y=190)

            # Months:
            self.mon = StringVar()
            self.mon.set(MONTHS[0]) # default value
            self.monthMenu = OptionMenu(parent, self.mon, *MONTHS,command=self.setMonth).place(x=480,y=190)
            
            # Weendays:
            self.weekdays = StringVar()
            self.weekdays.set(WEEKDAYS[0]) # default value
            self.weekMenu = OptionMenu(parent, self.weekdays, *WEEKDAYS,command=self.setWeekDay).place(x=620,y=190)

            self.texts()
            self.buttons()
            self.img()

        else:
            raise Exception(CronTaskUI._Singleton)  

    def setMonth(self,value):
        self.mo = value

    def setWeekDay(self,value):
        self.w = value
    
    def texts(self):
       Label(self,text='Scheduled test',bg=DarkGray,width='800',fg=Black,height='5',font=('ariel',15)).pack()
       Label(self,text='Complete the following form to create schudled test',bg=DarkGray,fg=Black,font=('ariel',10)).place(x=220,y=90)
       Label(self,textvariable=self.stateVar,bg=Gainsboro,fg=Black,height='2',border=5,font=('ariel',10)).place(x=280,y=350)
       

    def img(self):
        # Symbol image:
        global symbol
        symbol = PhotoImage(file='A.png')
        panel = Label(self , image = symbol)
        panel.place(x=60, y=115, anchor='sw')

    def buttons(self):
        btn1=Button(self, text='Save changes',activeforeground=Gray,bg=Silver,fg=Black,width='10',height='2',border=5,command=self.saveChanges)     
        btn2=Button(self, text='EXIT',command=self.destroy,activeforeground=Gray,bg=Silver,fg=Black,width='15',height='2',border=5)
        btn1.place(x=330, y=250)
        btn2.place(x=600, y=500)
        
        Label(self,text="Minutes: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',width='10',font=('ariel',10),border=5).place(x=60,y=150)  
        Label(self,text="Hours: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',width='10',font=('ariel',10),border=5).place(x=200,y=150)  
        Label(self,text="Days: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',width='10',font=('ariel',10),border=5).place(x=340,y=150)  
        Label(self,text="Months: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',width='10',font=('ariel',10),border=5).place(x=480,y=150)  
        Label(self,text="Weekday: ",activeforeground=Gray,bg=DarkGray,fg=Black,height='1',width='10',font=('ariel',10),border=5).place(x=620,y=150)            
 
    # Function to save cron changes into crontab
    def saveChanges(self):
        if self.mi.get() == 0:
            a = "*"
        else:
            a = str(self.mi.get())
        if self.h.get() == 0:
            b = "*"
        else:
            b = str(self.h.get())
        if self.d.get() == 0:
            c = "*"
        else:
            c = str(self.d.get())
        if self.mo == None:
            d = "*"
        else:
            d = str(self.mo)
        if self.w == None:
            e = "*"
        else:
            e = str(self.w)
        s = '/PingWin/CORE/pingwinCron.sh "{} {} {} {} {}"'.format(a,b,c,d,e)
        try:
            subprocess.call(s, shell=True)
            self.stateVar.set("Added scheduled task succesfully")
        except:
            self.stateVar.set("Error in crontab! Please try again")


# function to create Singleton:
def Handle():
    try:
        a = CronTaskUI(None)
    except Exception as s:
        a = s
    return a

def main():
    a = Handle()
    a.mainloop()   

if __name__=='__main__':
    main()


