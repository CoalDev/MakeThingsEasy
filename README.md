# Talk to execute
#### A voice recognition program made in python using Googles voice recognition and a couple simple libraries.
##### for now it is made for Linux although you can just change some variables in there to fit it for windows.

Usage: ``` python MteV-X.py ```
MteV-X where X is the latest version of the program.

##### **Make sure to download the libraries/APIs!**
#### How to download them?
1. Like this(Just type that in your native terminal):
    - This is for the Speech Recognition library ``` pip install SpeechRecognition ``` 
    - This is for the Text2Speech API ``` pip install gTTS ``` 

#### *Only when it says: "Say something:" it will register what you're saying*
1. Registered "commands":
    - open [alias]
    - close
2. Registered "aliases"
    - Python
    - YouTube
    - DuckDuckGo
    
###### Updates:
1. September 6, 2019
    - Added a full class for faster, easier and efficient code
    - Removed manually adding porgrams/cd/websites
    - Added a new way to add programs/cd/websites
    - Added a 'Word Test' mode
    
#### How to use the Mte() class
1. give_data
    - give_data expects 3 arguments, (Program, cd/website, Website{true/false})
    - for example I want to add python, I'd say give_data('python', 'home/python', False)
    - and for a website I'd say give_data('YouTube', 'https://youtube.com', True)
2. test_word
    - test_word does not expect any argumants
    - test_word is only for testing how the speechrecogntion detects the word
    - for example instead of detecing youtube like that, it detects it as YouTube
3. record_voice
    - record_voice does not expect any argumants
    - as the name says it just records your voice and stores it in a list to then execute when needed
    - record_voice returns a list
4. execute_order
    - execute_order expects 1 argumant and that is a list
    - you get that list from the returned value by the record_voice function, just give it the list and it will execute what you said
    
###### *At this version(0.0.2) you need to make sure that the program is matched to what the speechrecognition thinks it is, for this we added a 'Word Test' mode!*
