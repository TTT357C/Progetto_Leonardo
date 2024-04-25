import tkinter as tk
import tkinter.font as tkFont
import serial
import time


#s = serial.Serial("COM4", 9600) ####### change name, if needed
#s.open()
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds
 

class App:
    
    
    def __init__(self, root):
        
        # Set the title of the root window to "Controller"
        root.title("Controller")

        
        # Set the default font
        dfont = ""

        # Set the width and height of the window
        width = 580
        height = 620

        # Get the screen width and height
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()

        # Calculate the alignment string for the window
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        # Set the geometry of the root window
        root.geometry(alignstr)

        # Make the window non-resizable
        root.resizable(width=False, height=False)


        #======================================================================
        #Buttons and Lables
        #======================================================================
        
        GButtonUP = tk.Button(root)
        GButtonUP["activebackground"] = "#1872c6"
        GButtonUP["bg"] = "#1f93ff"
        GButtonUP["cursor"] = "trek"
        ft = tkFont.Font(family=dfont, size=38)
        GButtonUP["font"] = ft
        GButtonUP["fg"] = "#ffffff"
        GButtonUP["justify"] = "center"
        GButtonUP["text"] = "⇪"
        GButtonUP.place(x=240, y=100, width=100, height=100)
        GButtonUP.bind("<ButtonPress>", self.GButtonUPCommand)
        GButtonUP.bind("<ButtonRelease>", self.GButtonUPCommandRelease)


        GButtonDOWN=tk.Button(root)
        GButtonDOWN["activebackground"] = "#1872c6"
        GButtonDOWN["bg"] = "#1f93ff"
        GButtonDOWN["cursor"] = "spraycan"
        ft = tkFont.Font(family=dfont,size=38)
        GButtonDOWN["font"] = ft
        GButtonDOWN["fg"] = "#ffffff"
        GButtonDOWN["justify"] = "center"
        GButtonDOWN["text"] = "⇩"
        GButtonDOWN.place(x=240,y=210,width=100,height=100)
        GButtonDOWN.bind("<ButtonPress>",self.GButtonDOWNCommand)
        GButtonDOWN.bind("<ButtonRelease>", self.GButtonDOWNCommandRelease)

        GButtonLEFT=tk.Button(root)
        GButtonLEFT["activebackground"] = "#1872c6"
        GButtonLEFT["bg"] = "#1f93ff"
        GButtonLEFT["cursor"] = "star"
        ft = tkFont.Font(family=dfont,size=38)
        GButtonLEFT["font"] = ft
        GButtonLEFT["fg"] = "#ffffff"
        GButtonLEFT["justify"] = "center"
        GButtonLEFT["text"] = "⇦"
        GButtonLEFT.place(x=130,y=210,width=100,height=100)
        GButtonLEFT.bind("<ButtonPress>", self.GButtonLEFTCommand)
        GButtonLEFT.bind("<ButtonRelease>", self.GButtonLEFTCommandRelease)

        GButtonRIGHT=tk.Button(root)
        GButtonRIGHT["activebackground"] = "#1872c6"
        GButtonRIGHT["bg"] = "#1f93ff"
        GButtonRIGHT["cursor"] = "spider"
        ft = tkFont.Font(family=dfont,size=38)
        GButtonRIGHT["font"] = ft
        GButtonRIGHT["fg"] = "#ffffff"
        GButtonRIGHT["justify"] = "center"
        GButtonRIGHT["text"] = "⇨"
        GButtonRIGHT.place(x=350,y=210,width=100,height=100)
        GButtonRIGHT.bind("<ButtonPress>", self.GButtonRIGHTCommand)
        GButtonRIGHT.bind("<ButtonRelease>", self.GButtonRIGHTCommandRelease)

        GLabelTitle=tk.Label(root)
        GLabelTitle["bg"] = "#0007ff"
        ft = tkFont.Font(family=dfont,size=28)
        GLabelTitle["font"] = ft
        GLabelTitle["fg"] = "#ffffff"
        GLabelTitle["justify"] = "center"
        GLabelTitle["text"] = "Progetto Leonardo"
        GLabelTitle.place(x=130,y=20,width=320,height=50)

        GButtonEmerg=tk.Button(root)
        GButtonEmerg["activebackground"] = "#ffb800"
        GButtonEmerg["bg"] = "#ffd700"
        ft = tkFont.Font(family=dfont,size=38)
        GButtonEmerg["font"] = ft
        GButtonEmerg["fg"] = "#000000"
        GButtonEmerg["justify"] = "center"
        GButtonEmerg["text"] = "☢"
        GButtonEmerg.place(x=130,y=100,width=100,height=100)
        GButtonEmerg.bind("<ButtonPress>", self.GButtonEmergCommand)

        GButtonReset=tk.Button(root)
        GButtonReset["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonReset["font"] = ft
        GButtonReset["fg"] = "#000000"
        GButtonReset["justify"] = "center"
        GButtonReset["text"] = "↺"
        GButtonReset.place(x=350,y=100,width=100,height=100)
        GButtonReset.bind("<ButtonPress>", self.GButtonResetCommand)

        GButtonA2DOWN=tk.Button(root)
        GButtonA2DOWN["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA2DOWN["font"] = ft
        GButtonA2DOWN["fg"] = "#000000"
        GButtonA2DOWN["justify"] = "center"
        GButtonA2DOWN["text"] = "↧"
        GButtonA2DOWN.place(x=210,y=370,width=160,height=50)
        GButtonA2DOWN.bind("<ButtonPress>", self.GButtonA2DOWNCommand)

        GButtonA2UP=tk.Button(root)
        GButtonA2UP["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA2UP["font"] = ft
        GButtonA2UP["fg"] = "#000000"
        GButtonA2UP["justify"] = "center"
        GButtonA2UP["text"] = "↥"
        GButtonA2UP.place(x=210,y=430,width=160,height=50)
        GButtonA2UP.bind("<ButtonPress>", self.GButtonA2UPCommand)

        GButtonA1DOWN=tk.Button(root)
        GButtonA1DOWN["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA1DOWN["font"] = ft
        GButtonA1DOWN["fg"] = "#000000"
        GButtonA1DOWN["justify"] = "center"
        GButtonA1DOWN["text"] = "↧"
        GButtonA1DOWN.place(x=40,y=370,width=160,height=50)
        GButtonA1DOWN.bind("<ButtonPress>", self.GButtonA1DOWNCommand)

        GButtonA1UP=tk.Button(root)
        GButtonA1UP["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA1UP["font"] = ft
        GButtonA1UP["fg"] = "#000000"
        GButtonA1UP["justify"] = "center"
        GButtonA1UP["text"] = "↥"
        GButtonA1UP.place(x=40,y=430,width=160,height=50)
        GButtonA1UP.bind("<ButtonPress>", self.GButtonA1UPCommand)

        GButtonA3DOWN=tk.Button(root)
        GButtonA3DOWN["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA3DOWN["font"] = ft
        GButtonA3DOWN["fg"] = "#000000"
        GButtonA3DOWN["justify"] = "center"
        GButtonA3DOWN["text"] = "↧"
        GButtonA3DOWN.place(x=380,y=370,width=160,height=50)
        GButtonA3DOWN.bind("<ButtonPress>", self.GButtonA3DOWNCommand)

        GButtonA3UP=tk.Button(root)
        GButtonA3UP["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA3UP["font"] = ft
        GButtonA3UP["fg"] = "#000000"
        GButtonA3UP["justify"] = "center"
        GButtonA3UP["text"] = "↥"
        GButtonA3UP.place(x=380,y=430,width=160,height=50)
        GButtonA3UP.bind("<ButtonPress>", self.GButtonA3UPCommand)

        GButtonA4LEFT=tk.Button(root)
        GButtonA4LEFT["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA4LEFT["font"] = ft
        GButtonA4LEFT["fg"] = "#000000"
        GButtonA4LEFT["justify"] = "center"
        GButtonA4LEFT["text"] = "↤"
        GButtonA4LEFT.place(x=40,y=550,width=240,height=50)
        GButtonA4LEFT.bind("<ButtonPress>", self.GButtonA4LEFTCommand)

        GLabel1A=tk.Label(root)
        GLabel1A["bg"] = "#1e90ff"
        ft = tkFont.Font(family=dfont,size=23)
        GLabel1A["font"] = ft
        GLabel1A["fg"] = "#ffffff"
        GLabel1A["justify"] = "center"
        GLabel1A["text"] = "Linear 1"
        GLabel1A.place(x=60,y=330,width=120,height=30)

        GLabel2A=tk.Label(root)
        GLabel2A["bg"] = "#1e90ff"
        ft = tkFont.Font(family=dfont,size=23)
        GLabel2A["font"] = ft
        GLabel2A["fg"] = "#ffffff"
        GLabel2A["justify"] = "center"
        GLabel2A["text"] = "Linear 2"
        GLabel2A.place(x=230,y=330,width=120,height=30)

        GLabel3A=tk.Label(root)
        GLabel3A["bg"] = "#1e90ff"
        ft = tkFont.Font(family=dfont,size=23)
        GLabel3A["font"] = ft
        GLabel3A["fg"] = "#ffffff"
        GLabel3A["justify"] = "center"
        GLabel3A["text"] = "Linear 3"
        GLabel3A.place(x=400,y=330,width=120,height=30)

        GButtonA4RIGHT=tk.Button(root)
        GButtonA4RIGHT["bg"] = "#f0f0f0"
        ft = tkFont.Font(family=dfont,size=28)
        GButtonA4RIGHT["font"] = ft
        GButtonA4RIGHT["fg"] = "#000000"
        GButtonA4RIGHT["justify"] = "center"
        GButtonA4RIGHT["text"] = "↦"
        GButtonA4RIGHT.place(x=300,y=550,width=240,height=50)
        GButtonA4RIGHT.bind("<ButtonPress>", self.GButtonA4RIGHTCommand)

        GLabel4A=tk.Label(root)
        GLabel4A["bg"] = "#1e90ff"
        ft = tkFont.Font(family=dfont,size=23)
        GLabel4A["font"] = ft
        GLabel4A["fg"] = "#ffffff"
        GLabel4A["justify"] = "center"
        GLabel4A["text"] = "Linear 4"
        GLabel4A.place(x=230,y=510,width=120,height=30)
        
        #======================================================================
        
    
    #======================================================================
    # Events
    #======================================================================


    def GButtonUPCommand(self, event):
        s.write('A'.encode("ascii"))
        
    def GButtonUPCommandRelease(self, event):
        s.write('X'.encode("ascii"))

    def GButtonDOWNCommand(self, event):
        s.write('B'.encode("ascii"))
        
    def GButtonDOWNCommandRelease(self, event):
        s.write('X'.encode("ascii"))

    def GButtonLEFTCommand(self, event):
        s.write('C'.encode("ascii"))
        
    def GButtonLEFTCommandRelease(self, event):
        s.write('X'.encode("ascii"))

    def GButtonRIGHTCommand(self, event):
        s.write('D'.encode("ascii"))
    
    def GButtonRIGHTCommandRelease(self, event):
        s.write('X'.encode("ascii"))

    def GButtonEmergCommand(self, event):
        s.write('0'.encode("ascii"))
        s.close()
        
    def GButtonResetCommand(self, event):
        s.write('6'.encode("ascii"))
        
    def GButtonA1DOWNCommand(self, event):
        s.write('7'.encode("ascii"))

    def GButtonA1UPCommand(self, event):
        s.write('8'.encode("ascii"))
        
    def GButtonA2DOWNCommand(self, event):
        s.write('9'.encode("ascii"))

    def GButtonA2UPCommand(self, event):
        s.write('10'.encode("ascii"))

    def GButtonA3DOWNCommand(self, event):
        s.write('11'.encode("ascii"))

    def GButtonA3UPCommand(self, event):
        s.write('12'.encode("ascii"))

    def GButtonA4LEFTCommand(self, event):
        s.write('13'.encode("ascii"))

    def GButtonA4RIGHTCommand(self, event):
        s.write('14'.encode("ascii"))
        
    #======================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()