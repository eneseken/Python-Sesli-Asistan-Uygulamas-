import speech_recognition as sr
import pyttsx3
import wikipedia
from PIL import Image, ImageSequence

# Konuşma tanıma öğesi
r = sr.Recognizer()

# Sesli yanıt öğesi
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


# GIF dosyası öğesi
gif_path = "asistan.gif"

# Yanıt vermek ve sesli olarak okumak için fonksiyon
def speak(text):
    engine.say(text)
    engine.runAndWait()
    with Image.open(gif_path) as im:
        for frame in ImageSequence.Iterator(im):
            frame = frame.convert('RGB')
            imdata = frame.tobytes()
            frame.show()
        engine.stop()

# Sesli olarak kullanıcı girdisi almak için fonksiyon
def get_audio():
    with sr.Microphone() as source:
        print("Ne söylemek istersin?")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="tr-TR")
            print("Söyledin: " + said)
        except Exception as e:
            print("Ses anlaşılamadı: " + str(e))

    return said

# Kullanıcının sorusuna yanıt vermek için fonksiyon
def get_answer(user_input):
    wikipedia.set_lang("tr")
    try:
        result = wikipedia.summary(user_input, sentences=3)
        return result
    except:
        return "Üzgünüm, aradığın konuda bilgi bulunamadı."

# Uygulamayı çalıştırmak için ana fonksiyon
def run():
    while True:
        user_input = get_audio()
        if "dur" in user_input:
            break
        answer = get_answer(user_input)
        speak(answer)
        

run()
