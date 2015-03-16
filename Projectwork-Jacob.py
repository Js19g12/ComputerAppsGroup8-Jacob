from Tkinter import *
from PIL import Image, ImageTk
import random
import Tkinter
import tkMessageBox
v = "" 
def close():
    root.destroy()  # def close window
def close_pop():
    tkMessageBox.showinfo("Close", "Are you sure you want to close the program?") #Popup for close-Not yet finished
def Min():
    root.wm_state('iconic')  # def minimize window
def Frame1():
    J1 = Tk() 
    frame1 = Frame(J1, height = 500, width = 500) #Open Frame J1 with size 500x500
    t=Label(J1, text="Blah Blah Blah") # Insert text here for explanation on how to use
    t.grid(row=10, column=0) #Definining position of text
    t.pack()
    frame1.pack() #Leave at end or breaks
def Frame2():
    J2 = Tk()
    frame2 = Frame(J2, bg="Red", height = 500, width = 500)
    frame2.pack() #Leave at end or breaks
def FrameSIM():
    J4 = Tk()
    frame4 = Frame(J4, height = 200, width = 200)
    #Insert Simplify page under here
    enterA = Entry(frame4)
    Aget=enterA.get()
    enterA.grid(row=1, column=1)
    enterB = Entry(frame4)
    Bget=enterB.get()
    enterB.grid(row=1, column=2)
    enterC = Entry(frame4)
    Cget=enterC.get()
    enterC.grid(row=1, column=3)
    #################################################################################################### WIP
    #global A
    #A = enterA.get()
    #global B
   #B = enterB.get()
    #global C
   # C = enterC.get()
    def Factor(a,b,c):
        Flaggy = True
        while Flaggy == True:
            
            random_a1=random.randint(-10,10)
            random_a2=random.randint(-10,10)
            random_c1=random.randint(-10,10)
            random_c2=random.randint(-10,10)
            if random_a1==0 or random_a2 == 0 or random_c1 == 0 or random_c2 == 0:
                pass
            elif (random_a1*random_c2) + (random_a2*random_c1) == b and random_a1/random_c1 != random_a2/random_c2 and random_a1*random_a2==a and random_c1*random_c2==c:
                break
                Flaggy = False
        print "y=(%dx+(%d))(%dx+(%d))" % (random_a1,random_c1,random_a2,random_c2)
        top = Toplevel()
        top.title("Answer")
        msg = Message(top, text = "y=(%dx+(%d))(%dx+(%d))" % (random_a1,random_c1,random_a2,random_c2))
        msg.pack(side=TOP)

    

    Factorer = lambda x = Aget, y = Bget, z = Cget: Factor(x,y,z)
    ###################################################################################################  WIP    
    buttonSim1 = Tkinter.Button(frame4, text="Convert", command=Factorer)
    buttonSim1.grid(row=2, column=3)
    output = Entry(frame4)
    output.grid(row=3, column=3)


  
    frame4.pack() #Leave at end or breaks
def Frame3():
    J3 = Tk()
    frame3 = Frame(J3, height = 600, width = 1000)
    #Insert Graph page under here
    buttonSim = Tkinter.Button(frame3, text="Equation Convertor", command=FrameSIM)
    buttonSim.grid(row=2, column=6, padx=10, pady=10)
    frame3.pack() #Leave at end or breaks





im = Image.open('Title.jpg') #Import Image (Needs to be same directory)

root = Tkinter.Tk() #Open main window
root.configure(background='White') #background colour
tkimage = ImageTk.PhotoImage(im) 
Tkinter.Label(root, image=tkimage).grid(row=1, column=1, padx=10, pady =5) #Image location

button2 = Tkinter.Button(root, text="How to use",command=Frame1)
button2.grid(row=2, column=3, padx=10, pady=10)
button3 = Tkinter.Button(root, padx=10, text="Examples", command=Frame2)
button3.grid(row=4, column=3, padx=10, pady=10)
button4 = Tkinter.Button(root, text="Go to Grapher",command=Frame3)
button4.grid(row=5, column=3, padx=10, pady=30)





root.mainloop()
