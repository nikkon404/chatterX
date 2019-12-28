from tkinter import *
from tkinter import messagebox
import random


class AdminPanel:
    def __init__(self):
        initializeComponents()


def initializeComponents():
    window = Tk()

    window.title("VFX Cinemas")

    window.geometry('150x140')

    def clickAddMovie():
        a = addMovie()

    def clickShowMovie():
        s = showMovies()

    def clickViewBookings():
        v = ViewBookings()

    headerLabel = Label(window, text="   Admin Panel", font=("Arial Bold", 14))
    headerLabel.grid(row=0, column=0)

    btn1 = Button(window, text="Add a Movie", command=clickAddMovie)
    btn1.grid(row=1, column=0)

    separator = Frame(height=6, bd=1, relief=SUNKEN)
    separator.grid(row=3)

    btn2 = Button(window, text="Show movies", command=clickShowMovie)
    btn2.grid(row=6, column=0)

    separator = Frame(height=6, bd=1, relief=SUNKEN)
    separator.grid(row=7)

    btn2 = Button(window, text="Show Bookings", command=clickViewBookings)
    btn2.grid(row=8, column=0)

    window.mainloop()


class addMovie():

    def __init__(self):
        super().__init__()

        # GUI stuffs

        self.newWindow = Tk()
        self.newWindow.title("VFX Cinemas")

        self.newWindow.geometry('300x110')

        headerLabel = Label(
            self.newWindow, text=" Add a movie", font=("Arial Bold", 14))
        headerLabel.grid(row=0, column=0)

        lblName = Label(self.newWindow, text="Name", font=("Arial", 12))
        lblName.grid(row=1, column=0)

        self.txtName = Entry(self.newWindow, width=27)
        self.txtName.grid(column=1, row=1)

        lblDesc = Label(self.newWindow, text="Description",
                        font=("Arial", 12),  anchor="w")
        lblDesc.grid(row=2, column=0)

        self.txtDesc = Entry(self.newWindow, width=27)
        self.txtDesc.grid(column=1, row=2)

        btn = Button(self.newWindow, text="Submit", command=self.clicked)
        btn.grid(row=3, column=1)

        # this loop helps to keep the window running
        self.newWindow.mainloop()

    def clicked(self):
        name = self.txtName.get()
        desc = self.txtDesc.get()

        if name != "" and desc != "":
            num = random.randint(0, 100000000)
            path = "./database/movies.csv"

            f = open(path, "r+")
            count = len(f.readlines())

            value = str(num) + "," + name + "," + desc
            if count > 0:
                value = "\n"+value
            f.write(value)
            f.close()

            messagebox.showinfo('Success', 'Movie added')
            self.newWindow.destroy()

        else:
            messagebox.showerror("Error", "Please input all of the fields")


class showMovies():
    def __init__(self):
        super().__init__()
        window = Tk()

        root = Frame(window)
        window.geometry('400x200')
        window.title("List of Movies")
        header = Label(
            window, text="movie ID            - movie Name   -            description               ", justify=LEFT, anchor=W)

        header.grid(row=0, column=0)
        root.grid(row=1, column=0)

        path = "./database/movies.csv"
        f = open(path, "r+")
        lines = f.readlines()
        count = len(lines)
        if count == 0:
            root.destroy()
            messagebox.showinfo('Info', 'No movie added!')

        else:
            height = count
            width = 3
            for i in range(height):  # Rows
                curentLine = lines[i]

                for j in range(width):  # Columns
                    value = curentLine.split(",")
                    if j == 1:
                        cell = Label(root, font=(
                            "Arial Bold", 12), text=value[j], justify=LEFT, anchor=W, fg="black", padx=1, pady=1)
                    else:
                        cell = Label(
                            root, text=value[j], justify=LEFT, anchor=W,   fg="black", padx=1, pady=1)

                    cell.grid(row=i, column=j)

        window.mainloop()


class ViewBookings():
    def __init__(self):
        super().__init__()
        window = Tk()

        root = Frame(window)
        window.geometry('400x200')
        window.title("List of bookings")
        header = Label(
            window, text=" ID - Customer Name - movieID - Seat - Contact  ")

        header.grid(row=0, column=0)
        root.grid(row=1)

        path = "./database/customerInfo.csv"
        f = open(path, "r+")
        lines = f.readlines()
        count = len(lines)
        if count == 0:
            root.destroy()
            messagebox.showinfo('Info', 'No bookings made')

        else:
            height = count
            width = 5
            for i in range(height):  # Rows
                curentLine = lines[i]
                curentLine = curentLine[:-1]
                for j in range(width):  # Columns
                    value = curentLine.split(",")
                    if j != 0:
                        cell = Label(root, font=(
                            "Arial Bold", 12), text=value[j], justify=LEFT, anchor=W, fg="black", padx=2, pady=2)
                    else:
                        cell = Label(
                            root, text=value[j], justify=LEFT, anchor=W, bd=5,  fg="black", padx=2, pady=2)

                    cell.grid(row=i, column=j)

        window.mainloop()
