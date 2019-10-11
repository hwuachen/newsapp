import os
from .chatterbot import ChatBot
from ChatterBot.trainers import ListTrainer

bot = ChatBot("AnnaBot")
bot.set_trainer(ListTrainer)

# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path = "/venv1/Lib/site-packages/chatterbot_corpus/data/english"
# abs_file_path = os.path.join(script_dir, rel_path)

# for files in os.listdir(abs_file_path):
#     data = open(abs_file_path+files, 'r').readline()
#     bot.train(data)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while True:
        message = input('You:')        
        if message.strip() == 'Bye':
             print('ChatBot: Bye')
             break
        else:
            reply = bot.get_response(message)
            print('ChatBot:', reply)

