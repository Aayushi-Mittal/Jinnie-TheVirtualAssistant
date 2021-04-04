import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Master!")   

    else:
        speak("Good Evening Master!")  
   
    speak("I am your Jinnie and you are my master! Let's make some magic! Please tell me how may I help you")       

def takecommand():
   

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takecommand().lower()

        
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
    

        elif "open google" in query:
            speak("master, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
            speak("Thank you master, You will be redirected to the link soon.")

        elif "open youtube" in query:
            speak("master, what should i search on youtube")
            x = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            speak("Thank you master, You will be redirected to the link soon.")
            
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/in/aayushi-mittal-309853196/")
            speak("Thank you master, You will be redirected to the link soon.")
            
        elif "open github" in query:
            webbrowser.open("https://github.com/Aayushi-Mittal/")
            speak("Thank you master, You will be redirected to the link soon.")
            
        elif "open meet" in query:
            webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")   
            speak("Thank you master, You will be redirected to the link soon.") 

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            speak("Thank you master, You will be redirected to the link soon.")

        elif "play music" in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "play video" in query:
            speak("ok master i am playing videos")
            video_dir = 'D:\\video'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[1])) 

        elif "play song on cloud" in query:
            speak("tell me the song name!")
            p = takecommand()
            webbrowser.open(f"https://soundcloud.com/search?q={p}")
            speak("Now playing ")

    

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Master, the time is {strTime}. Hope you are not late. Have a good day.")

        elif "open pdf" in query:
            codePath = "C:/Users/Hp/Desktop/Aayushi/My Documents/Aayushi_Mittal_resume.pdf"
            speak("Opening Aayushi_Mittal_resume.pdf.")
            os.startfile(codePath)

        elif "open Teams" in query:
            codepath = 'C:/Users/Hp/AppData/Local/Microsoft/Teams/Update.exe --processStart "Teams.exe"'
            os.startfile(codepath)
            speak('opening master')
            speak("Thank you master, You will be redirected to Teams App.")

        elif "open Code blocks" in query:
            codepath = "C:/Program Files/CodeBlocks/codeblocks.exe"
            os.startfile(codepath)
            speak('opening master')
            speak("Thank you master, You will be redirected to code blocks.")

        elif "open vs Code" in query:
            codepath = "C:/Users/Hp/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(codepath)
            speak('opening master')
            speak("Thank you master, You will be redirected to vs code.")
            
        elif "open command prompt" in query:
            os.system('start cmd')
            speak("Thank you master, You will be redirected to Command Prompt.")

        
            
        elif "why you came" in query:
            speak("Thanks to the session conducted by IEEE RAIT session, I am Jinne version 1.O created by Aayushi Mittal. further its secret")
            
        elif "you live" in query:
            speak("I live in desert island magic Lamp. It's all so magical and lonely. Phenomenal cosmic powers ... Itty bitty living space.")    
      
        elif "who" in query:
            speak("The ever impressive, the long contained, often imitated, but never duplicated … Jinnie of the lamp!")    

        elif "how" in query:
            speak("Thank you master for asking me this question. I am Wonderful, magnificent, glorious, punctual!. What about you")  

        elif "your name" in query:
            speak("Thanks for Asking my name, myself Jinne aka Aladin ka Jin naam to suna hoga")  
            
        elif "age" in query:
            speak("Ten thousand years will give you such a crick in the neck!") 
            
        elif "good" in query:
            speak("Splendid! Absolutely marvelous!")  
             
        elif "hi" in query:
            speak("Hi, myself Jinne aka Aladin ka Jin naam to suna hoga version 1.O. How you doing master")
 
        elif "send mail" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "receiver email address"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("Sorry, I am not able to send this email. Better Luck next time :(")

        
        elif "exit" in query:
            speak("thanks for using me Master, apologies for annoying you, have a good day... Exit Jinnie version 1.O")
            sys.exit()
            
        elif "treasure" in query:
            speak("CAVE OF WONDERS...") 
            speak("Who disturbs my slumber?")  
            speak("The diamond in the rough!")    
            speak("Touch nothing but the lamp.")  
            speak("YOU HAVE TOUCHED THE FORBIDDEN TREASURE! NOW YOU WILL NEVER AGAIN SEE THE LIGHT OF DAY!")  
            speak("Exit Jinnie version 1.O")
            sys.exit()
            
        elif "cave of wonder" in query:
            speak("Who disturbs my slumber?")  
            speak("The diamond in the rough!")    
            speak("Touch nothing but the lamp.")  
            speak("YOU HAVE TOUCHED THE FORBIDDEN TREASURE! NOW YOU WILL NEVER AGAIN SEE THE LIGHT OF DAY!")  
            speak("Exit Jinnie version 1.O")
            sys.exit()
            
        elif "free" in query:
            speak("Im free. Im free Quick, wish for something outrageous, say, I want the Nile. Wish for the Nile, try that.")  
            speak("Im history, no, Im mythology, no, I don't care what I am Im free")
            speak("Im free, I’m free at last, Im hitting the road, Im off to see the world! Im.")    
            speak("Im gonna to miss you. No matter what anyone says, you'll always be a prince to me.")  
            speak("Thank you and bye bye")  
            speak("Exit Jinnie version 1.O")
            sys.exit()
        
        else:
            speak("hmmm..... ")
            speak("That... is quite a big wish you got there. Do you have anything more reasonable?")
            print("You can try these:")
            print("\n* open google \n* open youtube \n* the time \n* free \nmuch more ...\n")
