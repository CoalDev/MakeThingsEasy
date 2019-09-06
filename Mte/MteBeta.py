from MteClass import Mte

#test for your program real name, like youtube for the SpeechRecognition is YouTube
test = input("Want to test the word so you can be sure?: [y/n]").lower()

if test == 'n':
    newmte = Mte()
    newmte.give_data('python', '/home/liorlinux/Desktop/python', False)
    newmte.give_data('YouTube', 'http://youtube.com', True)
    newmte.give_data('DuckDuckGo', 'https://duckduckgo.com', True)
    voice = newmte.record_voice()
    newmte.execute_order(voice)
    print('Done')
else:
    Mte().test_word()