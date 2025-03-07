import pyttsx3, datetime, wikipedia, webbrowser, os, smtplib, random

import speech_recognition as sr

engine = pyttsx3.init('sapi5')
#sapi5 is a vouce asst. api
voices = engine.getProperty('voices')

email_dict = {
    "email id 1": "----",  #<email id 1>
    "email id 2": "----"   #<email id 2>
}

engine.setProperty('voices',voices[0].id)
#voices[0] is the voice of DAVID whose voice is inbuilt in our system

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Dragneel. How may I help you")

def takeCommand():
    #takes mic input from user & returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        #you can control how you want to speak, i.e for how much duration you wish to speak & with what voice strength
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        #recognize_google is a function to recognize in google. Select Ctrl & click on it to open recognize_google function
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Kindly repeat what you said")
        return "None"
    return query

def sendEmail(to, content):
    #using smtplib package we can send email through gmail
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    v = open("password.txt", 'r')
    password = v.readline()
    v.close()
    server.login('<sender>@gmail.com',password)
    server.sendmail('<sender>@gmail.com',to,content)
    server.close()

if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            #here "sentences=2" means 2 sentences would be read from wikipedia.
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Youtube opening, what do want to search ?")
            command = takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query=" + command)
            # search URL for youtube is https://www.youtube.com/results?search_query=
            # you can search anything in youtube now

        elif 'open google' in query:
            speak("google opening, what do want to search ?")
            command = takeCommand()
            webbrowser.open("https://google.com/?#q="+command)
            # search URL for google is https://google.com/?#q=
            # you can search anything in google now

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail opened")

        elif 'search in gmail' in query:
            speak("What do you want to search ?")
            command = takeCommand()
            webbrowser.open("https://mail.google.com/mail/u/0/#search/" + command)
            # search URL for gmail is https://mail.google.com/mail/u/0/#search/
            # you can search any email in gmail now


        elif 'open stackoverflow' in query:
            speak("stackoverflow opening, what do want to search ?")
            command = takeCommand()
            webbrowser.open("https://stackoverflow.com/search?q="+command)
            # search URL for stackoverflow is "https://stackoverflow.com/search?q="
            # you can search anything in stackoverflow now

        elif 'play music' in query:
            music_dir = '<music directory path>'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            #above line lists all songs under the given directory
            print(random_song)
            os.startfile(os.path.join(music_dir,random_song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'open virtual studio code' in query:
            codePath = "<VS Code path>"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            codePath = "<pycharm path>"
            os.startfile(codePath)

        elif 'open paint' in query:
            codePath = "<paint path>"
            os.startfile(codePath)

        elif 'open snipping tool' in query:
            codePath = "<snipping path>"
            os.startfile(codePath)

        elif 'open d drive' in query:
            codePath = "D:\\"
            os.startfile(codePath)

        elif 'open c drive' in query:
            codePath = "C:\\"
            os.startfile(codePath)

        elif 'email to' in query:
            if '<email id keyword 1>' in query:
                try:
                    speak("What should I write")
                    content = takeCommand()
                    to = email_dict["email id 1"]
                    sendEmail(to, content)
                    speak("Your Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry. I was unable to email pubali")
            elif '<email id keyword 2>' in query:
                try:
                    speak("What should I write")
                    content = takeCommand()
                    to = email_dict["email id 2"]
                    sendEmail(to, content)
                    speak("Your Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry. I was unable to email selfless gaming")
