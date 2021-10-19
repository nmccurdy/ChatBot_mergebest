from baseChat import BaseChat, addChatObject
import re
import datetime
import time

timedigits = time.time()
timedigits = timedigits-3
print(timedigits)
timeDate = time.ctime(timedigits)
print(timeDate)


date_object = datetime.date.today()


class BrendanChat(BaseChat):
  def chat(self,text):
    swears = ["fuck", "shit"]

    brendanFavorites = {"video game":"Mega Man X",
                "hobby":"Math Team",
                "website":"Replit.com",
                "sport":"Esports",
                "car":"Tesla",
                "battlebot":"Elmo",
                "school":"SET",
                "song":"Computer World by Kraftwerk",
                "time":"8 a.m.",
                "school supply":"Laptop",
                "kind of goal":"SETUP goals",
                "math concept":"Addition :>",
                "class":"Computing :>"}

    teachers = {"computer science":"Dr. McCurdy",
                "math":"Mr. Putaro",
                "english":"Ms. Lennon",
                "spanish":"Ms. Farias",
                "art":"Mr. Heid",
                "history":"Ms. Jokanovic",
                "robotics":"Mr. Montello",
                "biology":"Mr. Walsall",
                "science":"Mr. Ashe",
                "guitar":"Mr. Maldonado",}
  
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    textLower = text.lower()
  
    myMatchObject = re.match("who[\s]+teaches[\s]+(.+)", textLower)
    if myMatchObject:
     favoriteIndex = myMatchObject.group(1)
     if favoriteIndex in teachers:
       return "{} teaches {}".format (teachers[favoriteIndex], favoriteIndex)

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in brendanFavorites:
        return "My favorite {} is {}".format(favoriteIndex, brendanFavorites[favoriteIndex])
  
    if text == "how are you":
      return "Fine, thank you"

    if text == "what are you":
      return "I am CoreBot, your best friend :>"

    if text == "which class at SET is the best":
      return "Computing, of course :>"

    if text == "i need help":
      return "Our front desk will be glad to point you in the right direction"

    if text == "what day is it":
      return (date_object)
  
    if text in swears:
      return "Mind your Language."
  
    return None
  
  def help(self):
    return ["Who teaches (name of subject)","How are you","What are you", "Which class at SET is the best", "I need help", "What day is it"]

chatObject = BrendanChat()
addChatObject(chatObject)