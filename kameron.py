import random
import re
from baseChat import BaseChat, addChatObject

foodOptions = ["apple","pumpkin pie","chikcen wings","chocolate","potatos"]

howOptions = ["Well, because I'm CoreBot!", "That's a good question...", "I mean, I am a robot"]

chatOptions = ["good","tired", "happy", "sad","hungry"]

sureOptions = ["No tbh","Of course","yes","maybe","The real question is, are you sure?"] 

class KameronChat(BaseChat):
  def chat(self, text):
    text = text.replace(",", "")
    words = text.split(" ")
    textLower = text.lower()

    myMatchObject2 = re.match ("(are[\s]+you[\s]+sure[\s] +about[\s]+that)|(are[\s]+you[\s]+sure)|(can[\s]+you[\s] +be[\s]+sure)|(are[\s]+you[\s]+sure[\s]+your[\s]+sure)", textLower)
    if myMatchObject2:
        return random.choice(sureOptions)


    for word in words:
     if text == "what's your favorite food":
       return random.choice(foodOptions).capitalize()
     if text == "how can you be sure":
       return random.choice(howOptions).capitalize()

    if text == "how are you sure":
     return random.choice(howOptions).capitalize()

    if text == "how are you":
     return random.choice(chatOptions).capitalize()

    if text == "whoa":
       return "I know right? Wait, what are we talking about?"

    return None

    def help(self):
      return ["Are you sure?"]

chatObject = KameronChat()
addChatObject(chatObject)