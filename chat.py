import speech_recognition as sr
from googletrans import Translator

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    # Use the speech recognition engine to convert audio to text
    query = recognizer.recognize_google(audio, language='rw')
    print("You said:", query)

    # Translate the text to French
    translation = translator.translate(query, dest='en')
    translated_text = translation.text

    print("Translation (French):", translated_text)

except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")
except sr.RequestError:
    print("Sorry, I encountered an error while making a request to the speech recognition service.")
except Exception as e:
    print("Sorry, an error occurred:", str(e)) 