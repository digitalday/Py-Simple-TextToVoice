import pyttsx3

# инициализация
engine = pyttsx3.init()

en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',en_voice_id)

# Volume
engine.setProperty('volume',0.5)

stop = ''
print('For exit pls print (exit)')


while stop != 'exit' :

    Text = input('Say:')
    stop = Text
    if stop == 'exit':
        engine.say('Good Bye')
        break

    engine.say(Text)
    engine.runAndWait()



engine.runAndWait()