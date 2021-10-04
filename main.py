from mccurdy import McCurdyChat
from austin import AustinChat
from gavin import GavinChat


def chat(text):
  chatBotClasses = [McCurdyChat, AustinChat, GavinChat]

  if text.lower() == "help":
    helpStrings = []
    for cls in chatBotClasses:
      helpStrings.extend(cls.help())

    return "I know how to do the following:\n" + "\n".join(helpStrings)

  for cls in chatBotClasses:
    response = cls.chat(text)

    if response:
      return response

    
  return "I'm still learning.  Try saying hello."

while(True):
  userInput = input(">>> ")
  print(chat(userInput))