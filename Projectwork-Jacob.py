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
    enterA = Entry(frame4) #Input boxes make look pretier  
    enterA.grid(row=1, column=1)
    enterB = Entry(frame4) #Input boxes make look pretier 
    enterB.grid(row=1, column=2)
    enterC = Entry(frame4) #Input boxes make look pretier 
    enterC.grid(row=1, column=3)

    def length(i):   #Quick define Length
      return len(str(i))
    def FacButton():
        a = enterA.get() #Gets values from input box
        b = enterB.get()
        c = enterC.get()
        if length(a) == 3 or length(b) == 3 or length(c) == 3 or length(a) == 0 or length(b) == 0 or length(c) == 0: #Error if number greater than 2 digits
            tkMessageBox.showinfo(title="Error", message="please enter numbers from -99 to 99!") #popup error output
        elif a.isalpha() or b.isalpha() or c.isalpha(): #Error if Letters
            tkMessageBox.showinfo(title="Error", message="please enter numbers not letters!") #popup error output     
        elif (int(b)**2)-(4*int(a)*int(c)) < 0: #Error if sqr > 0
            tkMessageBox.showinfo(title="Error", message="As the squareroot lesss than 0 it wont produce real results") #popup error output 
        else:
            A = int(a) #Set values to integers 
            B = int(b)
            C = int(c)
            result = Factorer(A,B,C) #Output to Ashelys factoriser 
    def Factorer(a,b,c):
        while True:
            random_a1=random.randint(-10,10)
            random_a2=random.randint(-10,10)
            random_c1=random.randint(-10,10)
            random_c2=random.randint(-10,10)
            if random_a1==0 or random_a2 == 0 or random_c1 == 0 or random_c2 == 0:
                pass
            elif (random_a1*random_c2) + (random_a2*random_c1) == b and random_a1/random_c1 != random_a2/random_c2 and random_a1*random_a2==a and random_c1*random_c2==c:
                break
        tkMessageBox.showinfo(title="Answer", message="y=(%dx+(%d))(%dx+(%d))" % (random_a1,random_c1,random_a2,random_c2)) #Output to textbox
        print "y=(%dx+(%d))(%dx+(%d))" % (random_a1,random_c1,random_a2,random_c2) 

    buttonSim1 = Button(frame4, text="Convert", command=FacButton) #Button to activate factoriser
    buttonSim1.grid(row=2, column=3)


  
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
