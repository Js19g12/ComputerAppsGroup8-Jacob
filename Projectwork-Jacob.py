from Tkinter import *
from PIL import Image, ImageTk
import Tkinter
def close():
    root.destroy()  # def close window
def close_pop():
    tkMessageBox.showinfo("Close", "Are you sure you want to close the program?") #Popup for close-Not yet finished
def Min():
    root.wm_state('iconic')  # def minimize window
def Frame1():
    J1 = Tk() 
    frame = Frame(J1, height = 500, width = 500) #Open Frame J1 with size 500x500
    t=Label(J1, text="Blah Blah Blah") # Insert text here for explanation on how to use
    t.grid(row=10, column=0) #Definining position of text
    t.pack()
    frame.pack() #Leave at end or breaks
def Frame2():
    J2 = Tk()
    frame = Frame(J2, bg="Red", height = 500, width = 500)
    frame.pack() #Leave at end or breaks
def Frame3():
    J3 = Tk()
    frame = Frame(J3, bg="Green", height = 500, width = 500)
    #Insert Graph page here

    frame.pack() #Leave at end or breaks


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
