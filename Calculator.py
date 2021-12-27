from tkinter import * #allows us to create our Gui

window = Tk() #Creating our Gui (window)

window.title("Calculator")

window.geometry("355x475") #width x height

window.configure(bg="#0a0a0f") #giving the window background colour(https://www.w3schools.com/colors/colors_picker.asp?colorhex=E88SCE)

window.iconbitmap("calc2.ico")#Changing the icon of the window(www.flaticon.com),Icon downloaded is in 'pgn' format we have to convert it into 'ico' format (https:icoconvert.com)

window.resizable(width=False,height=False)#or (False,False)#Resizable method so that we can have a default window size 


expression = ""
def press(num): #variable num created and store it in another variable expression and setting it to an empty string
    global expression #global keyword

    expression = expression + str(num) #keeps on adding on the entry box whatever we keep on pressing

    equation.set(expression) #to show in the entry box whatever expression and calculation/evaluation we press
    

def equalpress():
    global expression

    try:#
        total=str(eval(expression)) #eval bult in(solves the expression and returns it to the total

        equation.set(total)#to show the total on the entry box/screen after expression has

        #reseting our expression varible so that when we are done with one expression/evaluation it resets the expession,in order to be able to solve another problem
        expression=""
    except:
        equation.set("Error")
        expression=""

def clear():
    global expression

    expression=""
    equation.set("0") #when the user resets or clears the entry box displays a zero

button_frame=Frame(window,bg="#00001a")#Frame helps us to place the buttons exactly where we want in our window
button_frame.pack() #Frame,we can't see it, its made to hold things eg buttons

equation=StringVar()#Making the textvariable of type string
equation.set("0")#
expression_field = Entry(button_frame,textvariable=equation,justify="right",font=("arial",20,"bold"),bg="#9999ff")#(<where to lacate it>,<Grabs whatever the user enters in the entry box>,<Make text to apper to the right>
#expression_field.pack() we deleted this so that we can pack everything together eg.entry box,buttons at the same time

button1 = Button(button_frame,text="1",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(1))#Relief(boarderwidth button size/style("flat","raised",sunken,ridge,solid,groove),bd=boarderwidth,lambda=to send something over

button2 = Button(button_frame,text="2",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(2))

button3 = Button(button_frame,text="3",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(3))

addition = Button(button_frame,text="+",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#39004d",fg="#00b8e6",width=8,height=3,command=lambda:press("+"))

button4 = Button(button_frame,text="4",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(4))

button5 = Button(button_frame,text="5",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(5))

button6 = Button(button_frame,text="6",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(6))

subract = Button(button_frame,text="-",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#39004d",fg="#00b8e6",width=8,height=3,command=lambda:press("-"))

button7 = Button(button_frame,text="7",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(7))

button8 = Button(button_frame,text="8",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(8))

button9 = Button(button_frame,text="9",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(9))

multiply = Button(button_frame,text="x",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#39004d",fg="#00b8e6",width=8,height=3,command=lambda:press("*"))

button0 = Button(button_frame,text="0",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(0))

decimal = Button(button_frame,text=".",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press("."))

clear = Button(button_frame,text="C",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=clear)

division = Button(button_frame,text="/",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#39004d",fg="#00b8e6",width=8,height=3,command=lambda:press("/"))

equal = Button(button_frame,text="=",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#ff0066",fg="#00b8e6",width=17,height=3,command=equalpress)

bracket1 = Button(button_frame,text="(",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press("("))

bracket2 = Button(button_frame,text=")",font=("times new roman",12,"bold"),relief="ridge",bd=1,
          bg="#00001a",fg="#00b8e6",width=8,height=3,command=lambda:press(")"))
#Placing all the things we created in our window
expression_field.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=25,pady=15)#(row,column),columnspan(to span up to 4 columns because we want the other buttons below to fit properly)
#ipadx - making the expression field wide, ipady - making the expression field taller,
#separation between the tittle bar and the entry box also and the buttons we use pady (separation up and down)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
addition.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
subract.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
multiply.grid(row=3,column=3)

button0.grid(row=4,column=0)
decimal.grid(row=4,column=1)
clear.grid(row=4,column=2)
division.grid(row=4,column=3)

equal.grid(row=5,column=2,columnspan=2)
bracket1.grid(row=5,column=0)
bracket2.grid(row=5,column=1)




window.mainloop()#does what you instruct eg a button to do
                 


