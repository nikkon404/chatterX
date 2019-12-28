from tkinter import *


class MovieChooser():
    def __init__(self, *args):

        self.status = False
        self.LOM = args[1]
        self.bot = args[0]
        self.newWindow = Tk()
        self.newWindow.title("Choose movie")
        self.newWindow.resizable(width=False, height=False)
        OPTIONS = []

        for val in self.LOM:
            OPTIONS.append(val)

        print(OPTIONS)

        self.variable = StringVar(self.newWindow)
        self.variable.set(OPTIONS[0])  # default value

        headerLabel = Label(
            self.newWindow, text=" Choose a movie", font=("Arial Bold", 14))
        headerLabel.grid(row=0, column=0)

        lblMovie = Label(self.newWindow, text="Movie:", font=("Arial", 12))
        lblMovie.grid(row=1, column=0)

        self.dropDown = OptionMenu(self.newWindow, self.variable, *OPTIONS)
        self.dropDown.grid(row=1, column=1)

        lblName = Label(self.newWindow, text="You name:", font=("Arial", 12))
        lblName.grid(row=2, column=0)

        self.txtName = Entry(self.newWindow, width=27)
        self.txtName.grid(row=2, column=1)

        lblSeat = Label(self.newWindow, text="Number of Seat:",
                        font=("Arial", 12))
        lblSeat.grid(row=3, column=0)

        self.txtSeat = Entry(self.newWindow, width=2)
        self.txtSeat.grid(row=3, column=1)

        lblContact = Label(self.newWindow, text="Contact",
                           font=("Arial", 12),  anchor="w")
        lblContact.grid(row=4, column=0)

        self.txtContact = Entry(self.newWindow, width=27)
        self.txtContact.grid(column=1, row=4)

        btn = Button(self.newWindow, text="Submit", command=self.clicked)
        btn.grid(row=5, column=1)

        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.newWindow.mainloop()

    def clicked(self):
        name = self.txtName.get()
        seat = self.txtSeat.get()
        contact = self.txtContact.get()

        if name != "" and seat != "" and contact != "":
            movieId = self.LOM[self.variable.get()]

            from scripts.customer import Customer
            newC = Customer(name, movieId, seat, contact)

            newC.saveCustomerInfo()
            messagebox.showinfo('Success', 'Movie booked!')
            self.newWindow.destroy()
            self.status = True
            self.bot.botDisplayChat(
                ' '+name + ' I have booked ' + seat + ' seat for you to watch ' + self.variable.get())
            self.bot.botDisplayChat('I hope you will enjoy your movie ')

        else:
            messagebox.showerror("Error", "Please input all of the fields")

    def on_closing(self):
        self.newWindow.destroy()
        self.bot.botDisplayChat(
            'Looks like you are not interested to watch a movie.')
