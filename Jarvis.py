import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Joshi Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Joshi Sir")

    else:
        speak("Good Evening Joshi Sir")

    speak("I am Jarvis ,Please tell me how may I help you")
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587) #open the low security apps in gmail
    server.ehlo()
    server.starttls()
    server.login("yourgmail.com" , "your password")
    server.sendmail("your gmail " , to , content)
    server.close()

def takeCommand():

    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=3)
        print("Wait Calibrating Your Microphone ...")
        audio = r.listen(source)

    try:

        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print("User said:",query,"\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower() #logic based on executing task

        if "wikipedia" in query:
            speak("Searching Wikipedia ")
            query = query.replace("wikipedia" ,"")
            results = wikipedia.summary(query , sentences= 2 )#no of sentences from wikipedia
            speak("According to WIkipedia ")
            print(results)
            speak(results)
        elif("open youtube" in query):
            webbrowser.open("youtube.com")

        elif ("open google" in query):
            webbrowser.open("google.com")
        elif ("open stackoverflow" in query):
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir='C:\\Users\\asus\\Videos\\meme sounds\\full songs'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[2]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open Discord" in query:
           disocrd_path ='C:\\Users\\asus\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
           os.startfile(disocrd_path)
        elif "email akash " in query:
            #sbse upar ek dictionary bna lo usme key mei naam aur values mei id
            try:
                speak("What should I say ")
                content = takeCommand()
                to="akashjoshirm.aj@gmail.com"
                sendEmail(to , content)
                speak("Sir Email has been Sent ")
            except Exception as e:
                print(e)
                speak("Sorry I am unable to send this email at this mooment ")