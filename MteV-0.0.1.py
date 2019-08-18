from gtts import gTTS 
import speech_recognition as sr
import os
import sys
import webbrowser

commands = ['open', 'close']
websites = ['Google', 'YouTube']
aliases = ['python', 'CSharp']
folders = ['Text to speech']

path = "/home/liorlinux/Desktop/"
mytext = ' '
language = 'en'


# obtain audio from the microphone
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        message = r.recognize_google(audio)
        print(message)
        data = message.split() #split string into a list
        print(data)
        if len(data) > 1:
            if data[0] in commands:
                if data[1] in websites:
                    mytext = 'opening ' + data[1]
                    myobj = gTTS(text=mytext, lang=language, slow=False) 
                    myobj.save("CommandTTS.mp3") 
                    os.system("play CommandTTS.mp3") 

                    webbrowser.open('http://youtube.com', new=0, autoraise=True)
                    continue
                if data[1] == 'python':
                    mytext = 'opening ' + data[1]
                    myobj = gTTS(text=mytext, lang=language, slow=False) 
                    myobj.save("CommandTTS.mp3") 
                    os.system("play CommandTTS.mp3") 

                    path += data[1]
                    os.chdir(path)
                    os.system("code .")
        elif data[0] == 'close':
            mytext = 'Closing program you genius'
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("CommandTTS.mp3") 
            os.system("play CommandTTS.mp3") 
            break
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))