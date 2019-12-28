
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)

con = ["Hello", "Hi there!", "How are you doing?", "I'm doing great.",
                "That is good to hear", "Thank you.", "You're welcome."]
c = ChatBot('Export Example Bot')

trainer = ListTrainer(c)
trainer.train(con)


testVar = input("You : ")

while(testVar != "exit"):
    response = c.get_response(testVar)
    print("Bot: "+response.text)
    testVar = input("You: ")
print("\n")
