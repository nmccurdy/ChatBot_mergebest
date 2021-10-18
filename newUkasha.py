import random
import re
from baseChat import BaseChat, addChatObject


class UkashaChat(BaseChat):
  def chat(self, text):
    greetingOptions = ["hello", "hi", "hey", "yo", "hola", "wazzup", "sup"]

    sarGreetings = ["It's SoOoOo good to see you...", "Oh it's you...", "iM sO GlAd tO sEe yOU!", "*turns head the other way*"]
    

    myFavorites = {"animal":"chiwawa", 
                  "dessert": "oreo icecream",
                  "movie": "Nacho Lebre",}


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
      
      if word.lower() == "cya":
        return "LEAVE NOW, MORTAL!"
    
    return None

  def help(self):
    return["Wazzup", "sup", "cya"]


chatObject = UkashaChat()
addChatObject(chatObject)