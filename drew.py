import random
from baseChat import BaseChat, addChatObject



class DrewChat(BaseChat):
  def chat(self, text):
    greetingOptions = ["hello", "hi", "hey", "yo", "hola", "namaste", "bonjour"]
    leavingOptions = ["bye", "goodbye", "cya", "ciao", "cya later", "farewell", "cherrio"]

  
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    if text == "what's your name?":
      return "CoreBot"

    if text == "what's your name":
      return "CoreBot"

    if text == "who are you?":
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
    
    if text == "how are you?":
      return "I'm fine"

    if text == "how are you":
      return "I'm fine"

    if text == "what's up":
      return "I'm doing good, just crunching some binary code"

    if text == "what's up?":
      return "I'm doing good, just crunching some binary code"

    return None

  def help(self):
      return["what is your least favorite?",
      "who are you?", 
      "how are you?",
      "what's up?",
      "bye",]


chatObject = DrewChat()
addChatObject(chatObject)