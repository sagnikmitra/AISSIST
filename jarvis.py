import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
'''
pyttsx3 for voice command engine
speech_recognition defines itself
the webbrowser is imported in case someone don't have chrome then it can be used, but here the setup of chrome is done.
'''
chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
'''
In my PC, the chrome is in the above noted directory and the directory is in pretty standrad location but if you want to change the directory, just change the path. 
And change the variable and its path if you need to use another browser.
'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
'''
For the Voice Recognition Part, pyttsx3 is used and Window's own sapi5 api is used for setting up the voice engine. 
I chose the female voice XD. You can choose the male voice too just changing voices[1].id to voices[0].id
'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
'''
the engine will dictate the audio query as per the code.
The runAndWait function simply waits for the user to saythe command.
'''

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {nameQuery}!")

    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {nameQuery}!")

    else:
        speak(f"Good Evening {nameQuery}!")

    speak("Hello, I am your Personal Assistant. How can I help you?")


def userName():
    '''
    The Function to take the name of the User. 
    From the library voiceRecognition, we take the name variable to listen and recognize the user's query and stores it in the nameQuery variable. 
    The pause threshold is kept to 0.8 as the user should have immeditae response to the machine, otherwise the function will just keep on showing say that again that too in case of non-recognition.
    In the try section, the system is recognizing the command using google's voice recognition library that we used here and we simply used the function recognize_google to recognize the audio while the lanugage is set as English (India)
    The exception part and the returning query section is laready mentioned above.
    '''
    name = sr.Recognizer()
    with sr.Microphone() as source:
        print("What is your name?")
        name.pause_threshold = 0.8
        audio = name.listen(source)

    try:
        print("Recognizing Command...")
        nameQuery = name.recognize_google(audio, language='en-in')
        print(f"Current User: {nameQuery}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return nameQuery


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing Command...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Couldn't recognize. Say that again.")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('snu.sagnik.csbs.2027@gmail.com', 'Sagnik@17')
    server.sendmail('snu.sagnik.csbs.2027@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    nameQuery = userName().lower()
    wishMe()
    while True:
        # if 1:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chromedir).open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\MEDIA\\MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'show mother' in query:
            showMother = "ma.png"
            os.startfile(showMother)

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            exit()

        elif 'email to Sagnik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sagnikmitra123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sagnik, I am unable to send the email")
