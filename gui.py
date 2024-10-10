import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
window.geometry('500x300') #Change size of file that is opening
hello = tk.Label(text ="Hello CS 222")
welcome = tk.Label(text = "Welcome to cs 222", foreground = 'red') #changed font to red
clickMe = tk.Button(text = "ok", width =10, height = 3)
hello.grid(column = 0, row= 0)
welcome.grid(column= 1, row = 0)
clickMe.grid(column = 0, row= 1)
#hello.pack() #pack adds hello to the window
#welcome.pack()
#clickMe.pack()
window.mainloop()