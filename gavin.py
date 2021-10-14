from baseChat import BaseChat, addChatObject

class GavinChat(BaseChat):
  def chat(self,text):
    if text == "it's friday":
      return "yooooo!"
    

    return None
  
  def help(self):
    return ["it's Friday!"]

chatObject = GavinChat()
addChatObject(chatObject)