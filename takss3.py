import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


r = sr.Recognizer()
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            speak_text("Sorry, I didn't catch that.")
            return None
        return query

def respond_to_query(query):
    if 'hello' in query.lower():
        speak_text("Hello! How can I assist you today?")
    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak_text(f"The current time is {strTime}.")
    elif 'date' in query.lower():
        strDate = datetime.datetime.now().strftime("%d %B %Y")
        speak_text(f"Today's date is {strDate}.")
    elif 'search' in query.lower():
        speak_text("What would you like to search for?")
        search_query = get_audio()
        if search_query:
            url = f"(link unavailable)"
            webbrowser.open(url)
            speak_text(f"Searching for {search_query}...")
    else:
        speak_text("I didn't understand that. Please try again.")

if __name__ == "__main__":
    while True:
        query = get_audio()
        if query:
            respond_to_query(query)