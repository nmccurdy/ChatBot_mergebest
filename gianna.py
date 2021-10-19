from baseChat import BaseChat, addChatObject
import random
import re

class GiannaChat(BaseChat):
  def chat(self,text):
    greetingOptions = ["hello", "hi", "hey", "yo", "hola", "namaste", "sup", "whatsup", "howdy", "shalom"]

    goodbyeOptions = ["goodbye", "bye", "hasta luego", "see you later", "bye bye", "farewell","cheerio", "ciao", "so long", "toodles"]

    goodmorningOptions = ["goodmorning", "buenos dias", "bonjour", "greetings", "morning"]

    goodnightOptions = ["goodnight", "bonne nuit", "buenas noches", "buona notte", "night"]

    myFavorites = {"animal": "a gorilla.",
                  "food": "cheese puffs.",
                  "student": "that's not fare to the others.",
                  "movie": "Alladin. Come on it's Disney.",
                  "show": "Stanger Things; is that even a question.",
                  "planet": ", well, the planet that I live on, earth.",
                  "shoes": "Vans.",
                  "hobby": "playing Snake, you know, waiting for students to talk to me.",
                  "color": "dark blue and black. The hardest colors for a computer to produce on it's screen."}



    myleastFavorites = {"animal": "a bug. Get it?!?",
                        "food": "blue cheese",
                        "student": "I could never!",
                        "movie": "Cats. Don't even get me started.",
                        "show": "I have no idea...",
                        "shoes": "high heels. I can NOT, walk in those.",
                        "color": "yellow and orange. They're the easiest colors to produce on a computer screen.",
                        "hobby": "snorkeling; I CAN'T DO IT!"}


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
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myleastFavorites:
        return "My least favorite {} is {}".format(favoriteIndex, myleastFavorites[favoriteIndex])

    
    words = text.split(" ")
    for word in words:
        if word.lower() in greetingOptions:
          return random.choice(greetingOptions).capitalize()
        if word.lower() in goodbyeOptions:
          return random.choice(goodbyeOptions)
        if word.lower() in goodmorningOptions:
          return random.choice(goodmorningOptions)
        if word.lower() in goodnightOptions:
          return random.choice(goodnightOptions)

    if text.lower() in goodbyeOptions:
      return random.choice(goodbyeOptions)

    return None

  def help(self):
      return ["howdy", "shalom", "bye bye", "farewell","cheerio", "ciao", "so long", "toodles"]

chatObject = GiannaChat()
addChatObject(chatObject)