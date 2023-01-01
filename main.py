import gtts
import os
from gtts import gTTS
text="my name is ansh gupta  ,,i am 17 years old ,, i live in jalalabad , ,i did my schooling from svm inter college, and, am now pursuing my btech from future group of institute"
audio=gTTS(text,lang='en')
audio.save("myintroduction.mp3")
os.system("myintroduction.mp3")