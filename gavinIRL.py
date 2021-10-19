from baseChat import BaseChat, addChatObject

class GavinIRLChat(BaseChat):
  def chat(self, text):
    print(text)
    if text == "how are you":
      return "I am fine, thanks for asking"

    if text == "how is it going":
      return "I am pretty good, thanks for asking"

    if text == "sup fool":
      return "wassup bro"

    if text == "who are you":
      return "I am a chat bot :)"

    if text == "whats the weather like":
      return "look outside and tell me" 

    if text == "what's the weather like":
      return "look outside and tell me"

    if text == "tell me a joke":
      return "*witty comeback*"

    return None

  def help(self):
    return ["I will not help you"]

chatObject = GavinIRLChat()
addChatObject(chatObject)