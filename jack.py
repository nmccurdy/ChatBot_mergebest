import random
import re
from baseChat import BaseChat, addChatObject


class JackChat(BaseChat):
  def chat(self, text):
    greetingOptions = ["are you weird?", "hi", "hey", "yo", "hola", "namaste"]

    myFavorites = {"animal":"cat", 
                  "dessert": "cake",
                  "movie": "Finding Nemo",}


    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    
    textLower = text.lower()

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myFavorites:
        return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

    
    words = text.split(" ")
    for word in words:
      if word.lower() in greetingOptions:
        return random.choice(greetingOptions).capitalize()
      
      if word.lower() == "bye":
        return "see ya"
    
    return None

  def help(self):
    return["are you weird?"]


chatObject = JackChat()
addChatObject(chatObject)