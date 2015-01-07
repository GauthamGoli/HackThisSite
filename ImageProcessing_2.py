# Program written to complete HTS Programming Challenge 2
# PIL Image.getdata() function has been used to get the pixel values as an array
# reversetab is just inverse mapping of morse code
# pyperclip.copy() to copy the key to clipboard cuz I'm lazzy!! :P

import pyperclip
import PIL
from PIL import Image

reversetab = {'..--.-': '_', '..-': 'u', '--..--': ',', '....-': '4', '-.-.-.': ';', '.----.': "'", '-..-': 'x', '.-.': 'r', '--.-': 'q', '--..': 'z', '.--': 'w', '-..-.': '/', ' ': ' ', '..---': '2', '.-': 'a', '..': 'i', '-.-.': 'c', '...--': '3', '-.--': 'y', '-': 't', '.': 'e', '.-..': 'l', '--.': 'g', '...': 's', '-.--.-': '(', '..--..': '?', '.----': '1', '.--.': 'p', '-----': '0', '-.-': 'k', '-..': 'd', '----.': '9', '-....': '6', '.---': 'j', '---': 'o', '.-.-.-': '.', '--': 'm', '-.': 'n', '....': 'h', '---..': '8', '...-': 'v', '--...': '7', '.....': '5', '---...': ':', '-....-': '-', '..-.': 'f', '-...': 'b'}
img = Image.open("download.png")
test = list(img.getdata())
offset=0
text=''
key=''
for i in range(len(test)):
    if(test[i]==1):
        text += (chr(i-offset))
        offset = i
tim = text.split()
for i in tim:
    key += reversetab[i]

print key

pyperclip.copy(key)

        
