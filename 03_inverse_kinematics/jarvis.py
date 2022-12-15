import cv2
import speech_recognition as sr
import pyttsx3
import move_the_robot as mover
import camara

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)


def command_move(texto, inter):
    camara.take_frame(inter)
    img = cv2.imread('fotos/my_video_frame{}.png'.format(inter))
    vector = camara.find_vector(img, texto)

    if vector == (0, 0):
        print("No se encontró el color deseado en la imagen")
        engine.say("No se encontró el color deseado en la imagen")
        engine.runAndWait()
    else:
        mover.move_to_button2(vector)
        return




def speak():
    """Inicia conversación"""
    i = 1
    j = 1
    with sr.Microphone() as source:
        while i == 1:
            print('**Say your command: Orange / Yellow / Blue / Stop')
            engine.say("Diga un comando")
            engine.runAndWait()
            audio_1 = r.listen(source)

            try:
                text_1 = r.recognize_google(audio_1).lower()
                if text_1 == 'stop':
                    print('Bye')
                    engine.say('Cerrando programa')
                    engine.runAndWait()
                    i = 0

                elif text_1 in ['orange', 'yellow', 'blue']:
                    print('Executing: {}'.format(text_1))
                    engine.say('Ejecutando {}'.format(text_1))
                    engine.runAndWait()
                    command_move(text_1, j)
                    print(j)
                    j += 1

                else:
                    print('Invalid Command ({})'.format(text_1))
                    engine.say('Comando Inválido')
                    engine.runAndWait()

            except:
                print('Sorry could not hear')
                engine.say('Comando no reconocido')
                engine.runAndWait()


speak()
