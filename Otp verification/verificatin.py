from twilio.rest import Client
import random
import time

from tkinter import*
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x580+200+80')
        self.configure(bg="white")
        self.resizable(False,False)
        self.n = str(self.OTP())
        self.client = Client("AC87478a8a0e79e1e2430f6d4caf0b6175", "65e6884906a17e142856110cee6b2dcc")
        self.client.messages.create(to=("+919356597020"),
                                    from_ = "+12054306823",
                                    body = self.n
                                )
        self.minuteString = StringVar()
        self.secondString = StringVar()
        
        self.minuteString.set("10")
        self.secondString.set("00")


    def Labels(self):
        self.c = Canvas(self,bg="light green", width = 400, height=280)
        self.c.place (x=290,y=120)

        self.minuteTextbox = Entry(self,width=2, bg="#808080", font=("Calibri",20, ""), textvariable = self.minuteString)
        self.secondTextbox = Entry(self,width=2, bg="#808080", font=("Calibri",20, ""), textvariable = self.secondString)

        self.minuteTextbox.place(x=460 , y=270)
        self.secondTextbox.place(x=500 , y=270)
    
        self.upper_frame =Frame(self,bg="green", width=1500,height=130)
        self.upper_frame.place(x=0,y=0)
    
        self.picture = PhotoImage(file="pas.png")
        self.k = Label(self.upper_frame, image = self.picture, bg="green").place(x = 200, y = 25)
       
        self.j= Label(self.upper_frame,text="Verify OTP",font="TimesNewRoman 38 bold", bg="green", fg="white").place(x=290, y=35)
        
    def Entry(self):
        self.User_Name =Text(self, font = "calibri 20", borderwidth = 2, wrap= WORD, width=23, height=1)
        self.User_Name.place(x=330, y=200)    

    def OTP (self):
        return random.randrange(1000,10000)


    def Buttons(self):
            self.submitButtonImage = PhotoImage(file= "submit1.png")
            self.submitButton = Button(self, image=self.submitButtonImage, command = lambda:[self.checkOTP()], border=0)
            self.submitButton.place(x=440, y=330)

            self.resendOTPImage = PhotoImage(file="resend.png")
            self.resendOTP = Button(self, image = self.resendOTPImage, command = self.resendOTP , border = 0)
            self.resendOTP.place(x=420, y=430)
        
    def resendOTP(self):
        self.n = str(self.OTP())
        self.client = Client("AC87478a8a0e79e1e2430f6d4caf0b6175", "65e6884906a17e142856110cee6b2dcc")
        self.client.messages.create(to=("+919356597020"),
                                    from_ = "+12054306823",
                                    body = self.n)
                                

    def checkOTP(self):
            try:
                self.userInput = int(self.User_Name.get(1.0, "end-1c"))
                if self.userInput == int(self.n):
                        messagebox.showinfo("showinfo", "Verification Successfull")
                        self.n = "Done"    
                    
                else: 
                    messagebox.showinfo("showinfo", "Wrong OTP")
                    
            except:
                messagebox.showinfo("showinfo","Invalid OTP")    

    def runTimer(self):
        self.clockTime = int(self.minuteString.get())*60 + int(self.secondString.get())

        while(self.clockTime > -1):
             totalMinutes, totalSeconds = divmod(self.clockTime,60)

             self.minuteString.set("{0:2d}".format(totalMinutes))
             self.secondString.set("{0:2d}".format(totalSeconds))

             self.update()
             self.sleep(1)

             if(self.clockTime == 0):
                 messagebox.showinfo("","Your time has expired!")

             self.clockTime -= 1       



if __name__=="__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.OTP()
    window.Buttons()
    window.update()
    window.mainloop()   