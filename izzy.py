
import re
from baseChat import BaseChat, addChatObject

class IzzyChat(BaseChat):
  def chat(self,text):
    print("good")

    if text == "what are you doing":
      return " nothing because im a bot now do your homework"

    if text == " how are you today":
      return " i don't feel anything i'm a robot"

    myFavorites = {"ice cream":"rocky road", 
                  "animal": "cats",
                  "sport": "basketball",
                  "tv show": "greys anatomy",}

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
    return ["how are you today"]

chatObject = IzzyChat()
addChatObject(chatObject)

