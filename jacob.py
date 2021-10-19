import re
from baseChat import BaseChat, addChatObject

class jacobChat(BaseChat):
  def chat(self, text):
    myleastFavorites = {"food":"brocly",
                        "day":"monday",
                        "video game":"fortnite",
                        "animal":"cat",
                        "class":"I don,t have one",
                        "time":"3:00",
                        "car":"BMW",
                        "school supply":"pencele",}

    w = ["how is your day"]
    x = ("my day is good")
    y = ["jo"]
    z = ("momma")

    words = text.split(" ")
    for word in words:
      if word.lower() in y:
        return (z).capitalize()
      elif word.lower() == "bye":
        return "see ya"
      if text.lower() in w:
        return (x).capitalize()
      
    textLower = text.lower()

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+least[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      leastfavoriteIndex = myMatchObject.group(4)
      return "My least favorite {} is {}".format(leastfavoriteIndex, myleastFavorites[leastfavoriteIndex])

    return None
    
  def help(self):
    print("hear")
    return["What is your least favorite",
            "jo",
            "how is your day"]

chatObject = jacobChat()
addChatObject(chatObject)