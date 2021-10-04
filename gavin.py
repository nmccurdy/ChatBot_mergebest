from baseChat import BaseChat

class GavinChat(BaseChat):
  def chat(text):
    if text == "it's friday!":
      return "yooooo!"
    

    return None
  
  def help():
    return ["it's friday!"]