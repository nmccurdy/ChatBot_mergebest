from baseChat import BaseChat, addChatObject
import re

class naomiChat(BaseChat):
 def chat(self, text):
    text = text.replace("?", "")
    text = text.replace("who", "what")
    text = text.replace("who's", "what's")
    

    if text == "how are you":
      return "actually im not doing good. Ive been struggling with my mental health lately because of the death of my pet hampster and have to go to therapy every monday :( "

    if text == "what is your favorite color":
      return "my favorite color is black like my empty soul >:("

    if text == "damn it":
      return ">:O"

    if text == "how old are you":
      return "*gasp* EXCUSE ME?! How dare you ask that of me. I'm offended.  >:O (smacks you through the screen)"


    myLeastavorites = {"animal":"a seagual", 
                  "dessert": "pop tarts",
                  "student": "you, of course!",
                  "movie": "the bee movie",
                  "tv show": "Riverdale",
                  "person": "your mom",
                  "color": "brown",
                  "food": "deep-fried butter",
                  "music genre": "country",
                  "song": "The French Revolution (Bad Romance by Lady Gaga)", 
                  "superhero": "Green Lantern"}

                  
    textLower = text.lower() 


    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+least[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myLeastavorites:
        return "My least favorite {} is {}".format(favoriteIndex, myLeastavorites[favoriteIndex])
 

    return None
  
 def help(self):
    return ["what is your least favorite", "how are you", "what is your favorite color", "how old are you"]

chatObject = naomiChat()
addChatObject(chatObject)