import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak():
    with sr.Microphone() as source:
        """Inicia conversación"""
        print('Say your command: Red / Blue / Green')
        engine.say("Diga un comando")
        engine.runAndWait()
        audio_1 = r.listen(source)

        try:
            text_1 = r.recognize_google(audio_1)
            print('You said: {}'.format(text_1))
            engine.say('Ejecutando {}'.format(text_1)) #Ingresar funciones
            engine.runAndWait()

        except:
            print('Sorry could not hear')
            engine.say('Lo siento, no escuché bien')
            engine.runAndWait()
    reset_speak()


def reset_speak():
    """Reiniciar comando"""
    with sr.Microphone() as source:
        while True:
            print('Do you want to try again?: Yes/No')
            engine.say('¿Quieres probar denuevo?')
            engine.runAndWait()
            audio_2 = r.listen(source)
            try:
                text_2 = r.recognize_google(audio_2)
                if text_2 == "no":
                    engine.say('Muy bien, adios')
                    engine.runAndWait()
                    break
                elif text_2 == "yes":
                    engine.say('Reiniciando traductor')
                    engine.runAndWait()
                    speak()
                    break
                else:
                    print('Sorry, answer with yes or no')
                    engine.say('Lo siento, responda con un si o un no')
                    engine.runAndWait()

            except:
                print('Sorry could not hear')
                engine.say('Lo siento, no escuché bien')
                engine.runAndWait()

speak()
