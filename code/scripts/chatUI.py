# for UI elements
from tkinter import *
from tkinter import messagebox
# for chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from scripts.customer import Customer
import win32com.client
from scripts.MovieChooser import MovieChooser
import time
import sys
import logging
logging.basicConfig(level=logging.CRITICAL)

# sets the voice to a female character
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Voice = speaker.GetVoices().Item(1)


class ChatUI:

    def __init__(self, *args):
        super().__init__()

        # GUI stuffs
        self.yStartPos = 210
        self.scrollCount = 0

        self.newWindow = Tk()
        self.newWindow.title("Chat")
        self.newWindow.geometry('550x410+120+150')

        self.newWindow.resizable(width=False, height=False)

        # Create a new chatbot
        self.chatbot = ChatBot('Rebecca',

                               response_selection_method=get_random_response, tie_breaking_method=get_random_response)

        # sets the voice to a female character
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.speaker.Voice = speaker.GetVoices().Item(1)

        bottomFrm = Frame(self.newWindow)
        bottomFrm.grid(row=1)

        # textbox for chat
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.onTextChanged(sv))
        self.chatBox = Entry(bottomFrm, width=40, textvariable=sv)
        self.chatBox.grid(row=0, column=0, padx=5, pady=5)
        self.chatBox.bind('<Return>', (lambda _: self.clicked()))
        self.chatBox.focus_set()

        # Button
        self.submit = Button(bottomFrm, text="Submit",
                             state=DISABLED, command=self.clicked)
        self.submit.grid(row=0, column=1, padx=5, pady=5)

        newFrame = Frame(bg="green")
        newFrame.grid(row=0,)

        # scrollbar
        scroll = Scrollbar(newFrame, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill=Y)

        self.canv = Canvas(newFrame, width=525, height=370,)
        self.canv.pack(side=RIGHT)
        self.greetAndInfo()

        scroll.config(command=self.canv.yview)

        self.newWindow.mainloop()

    def greetAndInfo(self):

        self.botDisplayChat("Hello! I am Rebecca. Welcome to the VFX movies ")
        # train bot
        if True:
            self.botDisplayChat("Please wait until I am training....")

            # training chatbot
            trainer = ChatterBotCorpusTrainer(self.chatbot)
            trainer.train("database.training_file")

            self.botDisplayChat("Training Complete")
            self.scrollCount = 1

        self.botDisplayChat("Feel free to communicate with me.")


# this method is called whenever text is changed in the chat inputbox

    def onTextChanged(self, *args):
        text = self.chatBox.get()
        if text != "":
            self.submit.configure(state=NORMAL)
        elif text == "":
            self.submit.configure(state=DISABLED)


# this method is called after pressing the submit button


    def clicked(self):
        text = self.chatBox.get()
        if text != "":

            chatLabel = Label(self.canv, text=text, wraplength=200, justify=LEFT,
                              anchor=W, width=30, font=("Century Gothic", 9), fg='white', bg='black')

            photo = PhotoImage(file="./img/user.png")
            photoLabel = Label(self.canv, image=photo)
            photoLabel.photo = photo
            self.canv.create_window(510, self.yStartPos, window=photoLabel)
            self.canv.create_window(380, self.yStartPos, window=chatLabel)

            self.canv.update()
            chatLabel.update()

            chatLabelHeight = chatLabel.winfo_height()
            temp = self.yStartPos
            chatHeightDistance = chatLabelHeight-23
            self.yStartPos = self.yStartPos + 35 + chatHeightDistance

            self.chatBox.delete(0, END)

            self.botSay(self, text)

            return text

        elif text == "":
            messagebox.showwarning("Error", "Please input text")


# for automatic scrolling down

    def scrollDown(self, *args):
        self.canv.focus_set()
        self.canv.yview_scroll(2, "units")
        self.chatBox.focus_set()

# for getting response from the bot
    def botSay(self, *args):
        text = str(args[1])
        if 'exit' != str(text).lower() and 'bye' != str(args[1]).lower():

            self.botDisplayChat("Thinking....")

            botResponse = self.chatbot.get_response(text)
            print("confidence: " + str(botResponse.confidence) +
                  "\nin resp to: " + botResponse.in_response_to +
                  "\nsearch_in_response_to: " + botResponse.search_in_response_to +
                  "\nsearch text: " + botResponse.search_text +
                  "\ncoversation:" + str(botResponse.conversation) +
                  "\n ---------------------\n")

            resp = botResponse.text

            if botResponse.confidence >= 0.4:

                if 'fnC' in resp:
                    self.handleFunction(resp)

                else:
                    self.botDisplayChat(resp)
            else:
                self.botDisplayChat("Sorry, I didn't catch you.")
        else:
            self.botDisplayChat("Okay see you later!")
            import time
            time.sleep(1)
            self.newWindow.destroy()


# for handelling special bor functions


    def handleFunction(self, str):

        code = int(str.split('=')[1])
        if code == 1:
            self.showMovies()

    def showMovies(self):

        convo = open('./database/movies.csv', 'r').readlines()
        listOfMovies = {}

        if len(convo) > 0:
            self.botDisplayChat("Sure")
            statement = "There are " + str(len(convo)) + " movies now showing:"
            self.yStartPos = self.yStartPos + 5
            self.scrollCount = 1

            self.botDisplayChat(statement)
            for val in convo:
                temp = val.split(',')
                listOfMovies[str(temp[1])] = temp[0]

            self.botDisplayChat('Which of these should I book?')

            m = MovieChooser(self, listOfMovies,)

        else:
            self.botDisplayChat("There are no movies yet. Come back later")


# display message of bot in the UI

    def botDisplayChat(self, message):
        displayed = False
        chatLabel = Label(self.canv, text=message, wraplength=200, justify=LEFT,
                          anchor=W, width=30, font=("Century Gothic", 9), fg='white', bg='#00008b')

        photo = PhotoImage(file="./img/bot.png")
        photoLabel = Label(self.canv, image=photo)
        photoLabel.photo = photo
        self.canv.create_window(20, self.yStartPos, window=photoLabel)
        self.canv.create_window(150, self.yStartPos, window=chatLabel)

        self.canv.update()
        chatLabel.update()

        self.chatBox.delete(0, END)
        if message != "Thinking....":
            if self.scrollCount > 1:
                self.scrollDown()
            chatLabelHeight = chatLabel.winfo_height()
            chatHeightDistance = chatLabelHeight-23
            self.yStartPos = self.yStartPos + 35 + chatHeightDistance
            displayed = True
            if displayed:
                self.speaker.Speak(message)

            self.scrollCount = self.scrollCount + 1
