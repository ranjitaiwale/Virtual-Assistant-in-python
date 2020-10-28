import pyttsx3
import os
import speech_recognition
import webbrowser
import datetime
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()




def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if 0 <= hour < 12:
        speak("Good Morning Ranjit")
    elif 12 <= hour < 16:
        speak("Good afternoon Ranjit")
    elif 16 <= hour <17:
        speak("Good evening Ranjit")
    else:
        speak("Good Night Ranjit")
if __name__ == '__main__':
    wishMe()



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as source:
        print("Listening....")

        r.pause_threshold = 0.9

        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-en')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None
    return query


speak("I am your assistant. please tell me what can i do for you ? ")

while True:
    query = takeCommand().lower()

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")

    elif 'open facebook' in query.lower():
        webbrowser.open("facebook.com")

    elif 'open twitter' in query.lower():
        webbrowser.open("twitter.com")

    elif 'open google' in query.lower():
        webbrowser.open("google.com")

    elif 'open github' in query.lower():
        webbrowser.open("github.com")

    elif 'open' in query.lower():
        webbrowser.open("google.com")


    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\DELL\\Music\\Playlists"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" the time is {strTime}")
        print(strTime)

