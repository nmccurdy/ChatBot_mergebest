from baseChat import BaseChat

class AustinChat(BaseChat):
  def chat(text):
    if text == "what's your name?":
      return "CoreBot"
    
    return None
  
  def help():
    return ["What's your name?"]