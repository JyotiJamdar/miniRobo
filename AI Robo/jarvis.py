import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning ")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    
    speak("I am your well wisher. How may I help you")

def takeCommand():
    # this function takes microphone input from user and returns string output 
    r= sr.Recognizer()    
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query= r.recognize_google(audio, language= 'en-in')
        print (f"user said : {query} \n")

    except Exception as e:
        print("Kindly repeat again.....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikiedia", "")
            result= wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open insta' in query:
            webbrowser.open("instagram.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'quit' in query:
            quit()
        