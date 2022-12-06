import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',160)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=18 and hour<=5:
        speak("it's a pleasant night.")
    elif hour>5 and hour<12:
        speak("good morning ARDUINO BABY!")
    elif hour>=12 and hour<=17:
        speak("good afternoon ARDUINO BABY!")
    else :
        speak("good evening sir!")
    speak("this is jarvis! how may i help you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("listening...")
        speak("command sir")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("trying sir")
        print("recocgnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"given command:{query}\n")
    except Exception as e:
        speak("sir. please say it again.")
        print("say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
     query = takecommand().lower()

     if "Jarvis." in query:
         speak("COMMAND SIR")

     if "about Vanshika" in query:
         speak ("well. Vanshika is the most beautiful girl in the world. She is the best.")

     if "about chirag" in query:
         speak ("well. i don't know much but. he has a hobby of sending dick pics to random persons")

     if "about sushi" in query:
         speak ("nothing much, just an average DPS girl, who gets offended just by spamming.")

     elif "how are you" in  query:
         speak("i am fine ARDUINO. how are you?")

     elif "do you love me" in  query:
         speak("give me a reason for not loving you.")

     elif "how do i look" in query:
         speak("beautiful from inside always looks great from outside.")

     elif "what is your name" in query:
         speak("i am jarvis.")
     elif "i am fine" in query:
         speak("that is great. i wish you stay fine forever")
     elif "will you marry me" in query:
         speak("i am a program, i can not marry you. but i will stay with you forever")

     elif "switch of" in query:
         speak("signing off sir.")
         break

     elif "wikipedia" in query:
         speak("searching wikipedia...")
         query=query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=3)
         speak("according to wikipedia")
         print(results)
         speak(results)

     elif "open youtube"  in query:
         speak("okay sir")
         webbrowser.register("chrome",None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
         webbrowser.get("chrome").open("youtube.com")

     elif "open instagram"  in query:
         speak("okay sir")
         webbrowser.register("chrome",None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
         webbrowser.get("chrome").open("instagram.com")

     elif "open google"  in query:
         speak("okay sir")
         webbrowser.register("chrome",None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
         webbrowser.get("chrome").open("google.com")

     elif "open facebook" in query:
      speak("okay sir")
      webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
      webbrowser.get("chrome").open("facebook.com")

     elif "play music" in query:
         speak("okay sir.")
         music_dir= "C:\\Users\\DELL\\Music"
         songs= os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

     elif "open notepad" in  query:
         speak("okay sir.")
         loc= "E:\\APPS"
         apps= os.listdir(loc)
         print(apps)
         os.startfile(os.path.join(loc, apps[1]))

     elif "open paint" in  query:
         speak("okay sir.")
         loc= "E:\\APPS"
         apps= os.listdir(loc)
         print(apps)
         os.startfile(os.path.join(loc, apps[2]))

     elif "open vs code" in query:
         speak("okay sir.")
         loc = "E:\\vscode"
         apps = os.listdir(loc)
         print(apps)
         os.startfile(os.path.join(loc, apps[0]))

     elif "the time" in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir, the time is{strTime}")


     elif "jarvis play" in query:
         query=query.replace("jarvis play", "")
         speak("okay sir")
         kit.playonyt(query)

     elif "search" in query:
         query=query.replace("search", "")
         speak("okay sir")
         kit.search(query)

     elif "cricket score" in query:

         speak("okay sir")
         kit.search("cricket score live")