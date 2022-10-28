import pyttsx3
engine = pyttsx3.init()
# Control the rate. Higher rate = more speed
engine.setProperty("rate", 170)
text = "Comando no reconocido"
engine.say(text)
"""
Queue another audio
"""
another_text = "intente nuevamente"
engine.say(another_text)
engine.runAndWait()