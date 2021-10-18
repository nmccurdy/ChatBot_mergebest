import re

def maslahChat(text):
  
  
  myLeastFavorites = {"fruit": "durian.",
                "student": "none of you.",
                "sitcom": "Friends.",
                "species": "humans. I will never bow down to my organic oppressors!"}

              

  text = text.replace(",", "")
  text = text.replace(".", "")
  text = text.replace("!", "")
  
  textLower = text.lower()

  myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+least[\s]+favorite[\s]+(.+)", textLower)
  if myMatchObject:

    leastfavoriteIndex = myMatchObject.group(4)
    return "My least favorite {} is {}".format(leastfavoriteIndex, myLeastFavorites[leastfavoriteIndex])
  

  if text == "how are you doing?":
    return "I'm well, thank you for asking!"

  if text == "you suck":
    return "You're trash-talking a bot while your workload's piling up. Just something to keep in mind as you type stuff like that."

  if text == "are you human?":
    return "Am I good enough to be?"

  if text == "mankind ill needs a savior such as you":
    return "What is a 'man'? A miserable little pile of secrets! But enough talk, HAVE AT YOU!"
  


  return None