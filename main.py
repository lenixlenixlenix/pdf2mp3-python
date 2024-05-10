from pypdf import PdfReader
from gtts import gTTS
from termcolor import colored
import os
import time


print(colored('''
      
  ____  ____  _____ ____  __  __ ____ _____ 
 |  _ \|  _ \|  ___|___ \|  \/  |  _ |___ / 
 | |_) | | | | |_    __) | |\/| | |_) ||_ \ 
 |  __/| |_| |  _|  / __/| |  | |  __/___) |
 |_|   |____/|_|   |_____|_|  |_|_|  |____/ 
                                            
'''
              , 'green'))

while True:
    try:
        pdfFileName = input("Place file to folder /pdf and type name of file: ")
        reader = PdfReader(os.path.join("pdf", pdfFileName))
        print("--- IN PROGRESS --- FILE WILL BE SAVED IN " + colored("mp3/","red") +  " folder -----")
        break
    except FileNotFoundError:
        print("Invalid name of file")


full_text = ""

for i in range(0, len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    full_text += text


language = "en"

myobj = gTTS(text=full_text, lang=language, slow=False)

filename, _ = os.path.splitext(pdfFileName)

path = os.path.join("mp3", f"{filename}.mp3")

myobj.save(path)
print(colored(f"SAVED {path}", "green"))

