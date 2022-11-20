"""
pip install wikipedia
pip install SpeechRecognition
pip install ecapture
pip install pyjokes
pip install beautifulsoup4
pip install requests 
"""

import subprocess,pyttsx3,json
import speech_recognition as sr
import datetime,wikipedia,webbrowser,os
import winshell,pyjokes,ctypes,time,requests,shutil


from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning !")

	elif hour>= 12 and hour<16:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	speak("I am your Assistant.")
	

def username():
	speak("What should i call you ?")
	uname = takeCommand()
	speak("Welcome")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you?")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime(" %H:%M")
			speak(f"the time is {strTime}")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")
        
        

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query
            

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me your assistant")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Shreya & Ishita.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to the world" in query:
			speak("You should know as you created me.")


		elif "who are you" in query:
			speak("I am your virtual assistant.")

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.com/maps/place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "assistant" in query:
			
			wishMe()
			speak("Assistant in your service ")
			speak(assname)
			
		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you")
			speak(assname)	

        