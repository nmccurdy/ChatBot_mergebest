import random
import re
from baseChat import BaseChat, addChatObject


class DrewChat(BaseChat):
  def chat(self, text):
    greetingOptions = ["hello", "hi", "hey", "yo", "hola", "namaste", "bonjour"]
    leavingOptions = ["bye", "goodbye", "cya", "ciao", "cya later", "farewell", "cherrio"]

    myFavorites = {"animal":"a dog", 
                  "dessert": "peanut butter balls",
                  "student": "you, of course!",
                  "movie": "Die Hard",}

    myLeastfavorites = {"book":"The Hardy Boys",
                      "drink": "Diet Coke",
                      "tv show": "Friends",
                      "sport": "Ultimate Frisbee",
                      "color": "red",
                      "video game": "Minecraft",}

  
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    textLower = text.lower()

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myFavorites:
        return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+least[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      leastfavoriteIndex = myMatchObject.group(4)
      if leastfavoriteIndex in myLeastfavorites:
        return "My least favorite {} is {}".format(leastfavoriteIndex, myLeastfavorites[leastfavoriteIndex])


    if text == "what's your name":
      return "CoreBot"

    if text == "who are you":
      return "CoreBot"

    words = text.split(" ")
    for word in words:
      if word.lower() in greetingOptions:
        return random.choice(greetingOptions).capitalize()

    words = text.split(" ")
    for word in words:
      if word.lower() in leavingOptions:
        return random.choice(leavingOptions).capitalize()

    if text == "how are you":
      return "Could be better"

    if text == "what's up":
      return "I'm doing good, just crunching some binary code"

    if text == "it's friday":
      return "yooooo!"

    return None

  def help(self):
      return["hello",
      "what is your least favorite?",
      "what is your favorite?",
      "what's your name?",
      "who are you?", 
      "how are you?",
      "what's up?",
      "it's friday!",
      "bye"]


chatObject = DrewChat()
addChatObject(chatObject)