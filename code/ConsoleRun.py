from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from scripts.customer import Customer
import win32com.client
import time
import sys
import logging
logging.basicConfig(level=logging.CRITICAL)


speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Voice = speaker.GetVoices().Item(1)


chatbot = ChatBot('Rebecca',
                  response_selection_method=get_random_response)

print('\n\n\n\n\n')


def displayAndSay(str):
    print(chatbot.name+': '+str)
    speaker.Speak(str)


def showMovies():
    listOfMovies = {}
    convo = open('database/movies.csv', 'r').readlines()

    if len(convo) > 0:
        displayAndSay("Sure")
        statement = "There are " + str(len(convo)) + " movies now showing:\n"
        displayAndSay(statement)
        for val in convo:
            temp = val.split(',')
            listOfMovies[str(temp[1]).lower()] = temp[0]
            displayAndSay(str(temp[1]))
        displayAndSay('Which of these should I book?')
        while True:
            userMovieInput = input('You: ')
            if userMovieInput.lower() in listOfMovies:
                displayAndSay("You choose " + userMovieInput)
                displayAndSay("Enter you name, number of seat and contact")

                name = input()
                seat = input()
                contact = input()
                movieId = listOfMovies[userMovieInput.lower()]

                newC = Customer(name, movieId, seat, contact)
                displayAndSay(newC.name + " booked " + newC.seat +
                              " seats  for " + userMovieInput+". Contact is " + newC.contact)
                x = 4
                newC.saveCustomerInfo()
                break
            else:
                displayAndSay("Please Input Correctly!")

    else:
        displayAndSay("There are no movies yet. Come back later")


def handleFunction(str):
    code = int(str.split('=')[1])
    if code == 1:
        showMovies()


def mainMethod():

    displayAndSay("Hello! I am Rebecca. Welcome to the Application")
    displayAndSay("Would you like to train me?")

    if 'y' in str(input("Train? : ")):
        displayAndSay("Training in progress")
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train("database.training_file")
        displayAndSay("Training Complete!")

    displayAndSay("Please feel free to communicate with me.\n")

    while (True):
        userInput = str(input("\nYou : "))

        if userInput != str("exit"):
            response = chatbot.get_response(userInput)
            if response.confidence > 0.3:
                print('------------------------------')
                if 'fnC' in response.text:
                    handleFunction(response.text)
                else:
                    displayAndSay(response.text)
                print('------------------------------')
            else:
                displayAndSay("Sorry, didn't catch you there")
            print('confidence: '+str(response.confidence))

        if userInput == str("exit"):
            displayAndSay('Okay See ya Later!')
            break


mainMethod()


def animation():
    a = '-'
    for i in range(20):
        sys.stdout.write("\r" + a)
        time.sleep(0.05)
        a = a + '-'
        length = len(a)
        if length == 7:
            while len(a) > 0:
                a = a[:-1]
                length = len(a)
                sys.stdout.write("\r" + a)
                time.sleep(0.05)
