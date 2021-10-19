import random
import re
from baseChat import BaseChat, addChatObject


class LucasChat(BaseChat):
  def chat(self, text):

    greetingOptions = ["yo", "hello", "hi", "hey","hee"]
    leavingOptions = ["bye", "goodbye", "see ya", "bye bye",]

    sadstatementOptions = ["died", "old", "mean", "sad", "depressed", "bad"]

    sadresponseOptions = ["sorry to hear that", "dang that sucks"]

    happystatementOptions = ["great", "good", "happy", "awesome", "fine"]
    
    happyresponseOptions = ["thats great!", "glad to hear it", "nice!"]

    WeirdQuestion1 = "What are you"
    WeirdQuestion2 = "Who"
    WeirdQuestion3 = "purpose"
    WeirdQuestion4 = "name"

    WeirdQuestionResponse1 = "I am a progra... i meant human"
    WeirdQuestionReponse2 = "My name is dumb robot, given to me by my creator"
    WeirdQuestionResponse3 = "My purpose is to talk to my fellow humans"
    WeirdQuestionResponse4 = ["My name is dumb robot, given to me by my creator", "Chatbot"]

    Questionstatement1 = "how"
    Questionresponse1 = ["good, how about you", "alright, how about you", "ok, how about you"]

    ThanksStatement1 = "Thanks"
    ThanksResponse1 = "yea, no problem"

    errorResponse = ["I am not programmed to understand that", "I dont know what you are saying"]

    Bruhstatement1 = "joe"
    Bruhresponse1 = "mamma"

    myFavorites = {"movie": "Tennet",
              "food": "water",
              "hobby": "talking to dumb people like you",
              "sport": "hockey",
              "kind of music": "Trap",
              "type of music": "Trap",
              "genre of music": "Trap",
              "music": "Trap",
              "song": "Good News - Apashe",
              "animal": "a gibbon",
              "color": "red",
              "flavor of ice cream": "Oreo",
              "ice cream": "Oreo",
              "tv show": "Louder Milk"}

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

    words = text.split(" ")
    for word in words:
      if word.lower() in greetingOptions:
        return random.choice(greetingOptions)
      elif word.lower() in leavingOptions:
        return random.choice(leavingOptions)
      elif word.lower() in sadstatementOptions:
        return random.choice(sadresponseOptions)
      elif word.lower() in happystatementOptions:
        return random.choice(happyresponseOptions)
      elif word.lower() in Questionstatement1: 
        return random.choice(Questionresponse1)
      elif word.lower() in Bruhstatement1:
        return(Bruhresponse1)
      elif word.lower() in ThanksStatement1:
        return(ThanksResponse1)
      elif word.lower() in WeirdQuestion1:
        return(WeirdQuestionResponse1)
      elif word.lower() in WeirdQuestion2:
        return(WeirdQuestionReponse2)
      elif word.lower() in WeirdQuestion3:
        return(WeirdQuestionResponse3)
      elif word.lower() in WeirdQuestion4:
        return random.choice(WeirdQuestionResponse4)
      
    return None

  def help(self):
    return["hee", "hi", "bye", "What's your favorite movie",]


chatObject = LucasChat()
addChatObject(chatObject)

