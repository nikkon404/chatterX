from tkinter import *
from scripts.adminPanel import AdminPanel
from scripts.chatUI import ChatUI


window = Tk()


window.title("VFX Cinemas")

window.geometry('150x100+500+300')


def clickAdminButton():
    print('admin')
    window.destroy()
    admP = AdminPanel()


def clickChatButton():
    print('Chat')
    window.destroy()
    chat = ChatUI()

# GUI stuffs
headerLabel = Label(window, text="   VFX Cinemas", font=("Arial Bold", 14))
headerLabel.grid(row=0, column=0)

btn1 = Button(window, text="Admin", command=clickAdminButton) #clickAdmin button function is called then this button is pressed
btn1.grid(row=1, column=0)

separator = Frame(height=6, bd=1, relief=SUNKEN)
separator.grid(row=3)


btn2 = Button(window, text="Chat with Assistant", command=clickChatButton)
btn2.grid(row=8, column=0)


# this loop helps to keep the window running

window.mainloop()
