import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("voice", "spanish")  # Puede requerir ajuste según sistema operativo

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()
