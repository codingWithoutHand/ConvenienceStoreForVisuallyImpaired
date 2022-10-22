from unittest import getTestCaseNames
from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text,lang='ko')
    filename="sound.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("삼각김밥")