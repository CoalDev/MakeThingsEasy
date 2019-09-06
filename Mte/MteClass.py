from gtts import gTTS 
import speech_recognition as sr
import os
import sys
import webbrowser
import platform

diractories = {}

class Mte():
    def __init__(self):
        self.os = platform.system()
        com = open('commands.txt')
        pro = open('programs.txt')
        web = open('websites.txt')

        self.commands = com.read().split()
        self.programs = pro.read().split()
        self.websites = web.read().split()

    def give_data(self, program, cd, website):
        diractories[str(program)] = str(cd)
        if website == False:
            self.programs.append(str(program))
        else:
            self.websites.append(str(program))

    def test_word(self):
        print(Mte().record_voice())

    def record_voice(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                return r.recognize_google(r.listen(source)).split()
        except Exception as e:
            print("Error, couldn't listen or connect, Exception: "+str(e))
    
    def execute_order(self, audio):
        if len(audio) > 0:
            if audio[0] in self.commands:
                if audio[0] == 'open':
                    if audio[1] in self.programs:
                        os.chdir(diractories[audio[1]])
                        os.system('code .')
                    elif audio[1] in self.websites:
                        webbrowser.open(diractories[audio[1]], new=0, autoraise=True) 
                elif audio[0] == 'close':
                    print('Program terminated by user!')
                    sys.exit()
            else:
                print('Command is not registered! Registered commands: '+str(self.commands))
        else:
            print('Program terminated, no arguments made!')
            sys.exit()