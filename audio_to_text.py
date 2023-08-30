# pip install SpeechRecognition 
# pip install gTTS
# pip install playsound 
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def sound():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Say something: ")

        speak = microfone.listen(source)
    try:

        phrase = microfone.recognize_google(speak, language='pt-BR')
        print("You say: " + phrase)
        tts = gTTS(phrase, lang= 'pt-br')
        tts.save('hello.mp3')
        print("Im learning what you say!")
        playsound("sounds/hello.mp3")

    except:
        print("i didn't' understand...")

phrase = sound()
print("------------Its Okayyy!-------------")

