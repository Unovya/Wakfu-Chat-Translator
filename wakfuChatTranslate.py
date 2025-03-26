import os
import time
from deep_translator import GoogleTranslator
from langdetect import detect


logfile = r"C:\Program Files (x86)\Steam\steamapps\common\Wakfu\preferences\logs\wakfu_chat.log"
channels = [
   'Community',
   'Trade',
   'Recruitment',
   'Vicinity',
   'Private',
   'Guild',
]




def readLastLine():
   with open(logfile, "r", encoding='utf-8') as logs:
       lastLine = None
       for line in logs:
           lastLine = line.strip()
       return lastLine


def watchChat():
   lastChanged = os.path.getmtime(logfile)
   lastLine = None
   translator = GoogleTranslator(source='auto', target='en')


   while True:
       time.sleep(0.1)
       newChange = os.path.getmtime(logfile)


       if newChange != lastChanged:
           lastChanged = newChange
           newLastLine = readLastLine()


           if newLastLine is not None and newLastLine != lastLine:
               lastLine = newLastLine
               cleanMsg = lastLine.split(":", 2)[-1].split('-', 1)[1]
               messagePart = cleanMsg.split(':', 1)
               messageLang = detect(messagePart[-1])
               if messageLang != 'en':
                   messagePart[1] = translator.translate(messagePart[1])
               try:
                   for channel in channels:
                       if channel in messagePart[0]:
                           finalMsg = f'[{messageLang}] || {messagePart[0]}: {messagePart[1]}'
                           print(finalMsg)
                           return finalMsg


               except:
                   print('error')






def main():
    print('AutoTranslator is now Online')
    watchChat()


if __name__ == '__main__':
    main()

    #Use Flet to make app