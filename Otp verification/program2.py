from tkinter import *
from verificatin import *
from subprocess import call 

class Generate_otp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg = "#FFFFFF")
        self.resizable(False, False)

        self.f = ("Times bold",14)

    def Labels(self):
        self.upper_frame = Frame(self, bg="sky blue", width=1500, height= 130)
        self.upper_frame.place(x=0, y=0)
        self.lower_frame = Frame(self, bg="sky blue", width=1500, height=200)
        self.lower_frame.place(x=0, y=270)
        self.picture = PhotoImage(file="pas.png")
        self.k = Label(self.upper_frame, image=self.picture, bg = "sky blue").place (x=220,y=20)

        self.j = Label(self.upper_frame,text="OTP verification", font="TimesNewRoman 38 bold", bg="blue", fg="white").place(x=330,y=35)
        self.a = Label(self, text="OTP is valid for 10 minutes.", font="TimesNewRoman 14 bold", bg="blue", fg="white").place(x=360,y=290)
        self.b= Label(self, text="Click on the Genrate OTP button to generate OTP.", font="TimesNewRoman 14 bold", bg="blue", fg="white").place(x=260,y=338)

    def Buttons(self):
        self.GenerateOTP = PhotoImage(file="generateOTP.png")
        self.generatebutton = Button(self, image=self.GenerateOTP, command=self.Open, border=0)
        self.generatebutton.place(x=390, y=390)

    def Open(self):
        program2 = self.destroy()
        call(["python", "verificatin.py"])


if __name__ == "__main__":
    window = Generate_otp()

    window.Labels()
    window.Buttons()
    window.mainloop()                                                                                                                        
