import speech_recognition as sr
import pyttsx3
from move_the_robot import s as robot
import move_the_robot as mover

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def command_move(texto):
    if texto == "red":
        mover.move_robot_to_xyz(robot, 100, 0, 150)
    if texto == "blue":
        mover.move_robot_to_xyz(robot, -50, 0, 150)
    if texto == "green":
        mover.move_robot_to_xyz(robot, 50, 0, 150)


def speak():
    """Inicia conversación"""
    i = 1
    with sr.Microphone() as source:
        while i == 1:
            print('**Say your command: Red / Blue / Green / Stop')
            engine.say("Diga un comando")
            engine.runAndWait()
            audio_1 = r.listen(source)

            try:
                text_1 = r.recognize_google(audio_1).lower()
                if text_1 == 'stop':
                    print('Bye')
                    engine.say('Muy bien, adios')
                    engine.runAndWait()
                    i = 0

                elif text_1 in ['red','blue', 'green']:
                    print('Executing: {}'.format(text_1))
                    engine.say('Ejecutando {}'.format(text_1))
                    engine.runAndWait()
                    command_move(text_1)

                else:
                    print('Invalid Command ({})'.format(text_1))
                    engine.say('Comando Inválido')
                    engine.runAndWait()


            except:
                print('Sorry could not hear')
                engine.say('Lo siento, no escuché bien')
                engine.runAndWait()

speak()
