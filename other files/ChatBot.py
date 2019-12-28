from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


unknownBot = ChatBot(
    'PTTDeeplearningVillager',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    )


conv = open('convo.txt', 'r').readlines()

if input('train ? (y/n) ') == 'y':
    print('Training Bot')
    trainer = ChatterBotCorpusTrainer(unknownBot)
    trainer.train("../myown")
    #trainer = ListTrainer(unknownBot)
    # trainer.train(conv)


testVar = input("You : ")

while(testVar != "exit"):
    response = unknownBot.get_response(testVar)
    if response.confidence > 0.1:
        print('Bot: ', response)

    else:
        print('No confidence')

    testVar = input("You : ")
