from baseChat import BaseChat,addChatObject

class AustinChat(BaseChat):
  def chat(self, text):
    if text == "what's your name?":
      return "CoreBot"
    
    return None
  
  def help(self):
    return ["what's your name?"]

chatObject = AustinChat()
addChatObject(chatObject)