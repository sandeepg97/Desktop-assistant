import pyttsx3
import speech_recognition as sr
import calendar
import random
from gtts import gTTS
import os
import wikipedia
import webbrowser
import sys
import smtplib
import datetime


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


# Record audio and return it as string
def recording():
	#record the audio
	r=sr.Recognizer()#creating the recognizer object
	#open the microphone and start recording
	with sr.Microphone() as source:
		print('listening...')
		#r.energy_threshold = 400
		r.pause_threshold=1

		audio=r.listen(source)
	#use google speech recognition

	try:
		data=""
		print('recognizing...')
		data=r.recognize_google(audio,language='en-in')
		print(f"you said :{data}")
		
	except Exception as e:
		print('say that again plaease')
	return data
#a function for wake word or phrase
'''def wakewords(text):
	wake=['hey computer','ok computer'] #list of wake phrase
	text=text.lower()  #converting the text to lower case
	#check to see if the user's command contains wake word or not
	for phrase in wake:
		if phrase in text:
			return True
	return False'''

#a function to get current date and time
def getDate():
	now=datetime.datetime.now()
	my_day=datetime.datetime.today()
	week_day=calendar.day_name[my_day.weekday()]  #friday
	month_num=now.month
	day_num=now.day
	month_name=['January','February','March','April','May','June','July','August','September','October','November','December']
	ordinal_num=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
	return 'Today is '+week_day+' '+month_name[month_num-1]+ ' '+ordinal_num[day_num-1] +'.'
	
def greeting(text):
	greeting_inputs=['hi','hello','hey']
	greeting_responce=['howday','hello','hey there']

	for word in text.split():
		if word in greeting_inputs:
			return random.choice(greeting_responce)
	return ""

def getPerson(text):
	wordlist=text.split()
	for i in range(0,len(wordlist)):
		if i+3<=len(wordlist)-1 and wordlist[i].lower()=='who' and wordlist[i+1].lower()=='is':
			return wordlist[i+2]+' '+wordlist[i+3]

def sendEmail(to,content):
	server =smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('yourmail','PASSWORD')
	server.sendmail('yourmail',to,content)
	server.close()



def thank(text):
	phrase=[text]
	th=['thank you' ,'thanks','good job']
	rsp=['heppy to help','thats why i am here for']
	for word in phrase:
		if word in th:
			return random.choice(rsp)
	return 'none'

	
if __name__ == '__main__':
	speak("Hey i am your virtual assistant, how can in help you")
	recording()
	while True:
		text=recording().lower()
		response=''

		if ('date' in text):
			get_date=getDate()
			response=response+' '+get_date
			print(response)
			speak(response)

		elif ('wikipedia' in text):
			person=getPerson(text)
			wiki=wikipedia.summary(person,sentences=2)
			response=response+' '+wiki
			speak('according to wikipedia..')
			speak(response)

			#check to see if the user has said toknow about time
		elif ('time' in text):
			now=datetime.datetime.now()
			meridiem=''
			if now.hour>=12:
				meridiem='p.m'
				hour=now.hour-12
			else:
				meridiem='a.m'
				hour=now.hour
			#convert minute into proper string
			if now.minute<10:
				minute='0'+str(now.minute)
			else:
				minute=str(now.minute)

			response=response+' '+'it is '+str(hour)+':'+minute+' '+meridiem+'.'
			print(response)
			speak(response)


		elif 'who is' in text or 'when' in text or 'how' in text:
			speak('searching on google for'+text)
			say=text.replace(" ","+")
			webbrowser.open('http://www.google.co.in/search?q='+text)
			

		elif ('open youtube' in text):
			webbrowser.open('youtube.com')

		elif ('open google' in text):
			webbrowser.open('google.co.in')

		elif 'bye' in text or 'stop' in text:
			speak('Bye, have a great day.')
			sys.exit()

		elif 'hi' in text or 'hello' in text:
			gr=greeting(text)
			response=response+gr
			speak(response)

		
		elif 'how are you' in text:
			speak('i am good')
			speak('how can i help you')

		elif 'thank you' in text or 'thanks' in text or 'good job' in text:
			op=thank(text)
			response=response+op
			speak(response)

		elif 'email' in text or 'mail' in text:
			try:
				speak('whom you want to send email?')
				to=recording().lower()
				to=str(to.replace(" ",""))
				print(to)
				speak('what should i say?')
				content=recording()
				sendEmail(to,content) 
				speak("email has been sent")
			except Exception as e:
				speak("sorry!! couldn't send your email")

		elif "open email" in text:
			webbrowser.open("https://mail.google.com/")

		elif "open spotify" in text:
			path="C:\\Users\\Sandeep Kumar GIri\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe" #path
			os.startfile(path)

		elif "play music" in text:
			music_dir="D:\\New Folder" #path
			songs=os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs[0]))

			
			



		
			

		





			
			 


	
