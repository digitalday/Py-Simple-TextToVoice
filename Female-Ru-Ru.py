import pyttsx3

# инициализация
engine = pyttsx3.init()

ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
engine.setProperty('voice',ru_voice_id)

# Громкость
engine.setProperty('volume',0.5)
stop = ''
print('Для того чтобы закрыть программу напишите (выход)')


while stop != 'выход':
    Text = input('Сказать:')
    stop = Text
    if stop == 'выход':
        engine.say('До свидания')
        break

    engine.say(Text)
    engine.runAndWait()






