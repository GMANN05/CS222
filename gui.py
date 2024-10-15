import tkinter as tk
window = tk.Tk() #created blank 
window.title("My first GUI") #title
window.geometry('500x300') #Change size of file that is opening
hello = tk.Label(text ="Hello CS 222") #creates a label
welcome = tk.Label(text = "Welcome to cs 222", foreground = 'green') #changed font to red
clickMe = tk.Button(text = "ok", width =10, height = 3) #Adds button
hello.grid(column = 0, row= 0) #places each object in a row and column
welcome.grid(column= 1, row = 0) #places each object in a row and column
clickMe.grid(column = 0, row= 1) #places each object in a row and column
#hello.pack() #pack adds hello to the window
#welcome.pack()
#clickMe.pack()
window.mainloop()