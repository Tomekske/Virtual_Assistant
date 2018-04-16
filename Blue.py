import speech_recognition as sr
from colorama import Fore, Back, Style, init
import arrow
import subprocess
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from Weather import Weather
from core_functions import *

##
## @brief      Function to start recording speech
## @return     Speech as a string
##
def speech():
	r = sr.Recognizer() #make an object
	r.energy_threshold = 4000
	r.pause_threshold = 0.8
	#use microphone as source
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration = 1)

		print(Fore.YELLOW + "Say something:")
		audio = r.listen(source) #record speech

	try:
		voice = r.recognize_google(audio) #recognize speech
		return voice
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		return "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
		print("Could not request resulsts from Google Speech Recognition service; {0}".format(e))
		return "Could not request results from Google Speech Recognition service; {0}".format(e)

w = Weather('tokyo')

blue = False

while True:
	init(autoreset=True) #reset letter color to default value

	if not blue:
		voice = speech()
		print(voice)
		
		tok, filtered_tok = process_speech(voice)
		blue = start_command(filtered_tok)
		print(blue)

	else:
		print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Can I do somthing for you ?")

		voice = speech()

		tok, filtered_tok = process_speech(voice)

		if define_command(tok,filtered_tok, find_synonyms("time"), ["what","time"]):
			utc = arrow.utcnow()
			now = utc.format('HH:mm:ss')
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + now)

		elif define_command(tok,filtered_tok, find_synonyms("shut"), ["shut","computer"]):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "What's the super user's password?")
			voice = speech()
			print(voice)
			tok, filtered_tok = process_speech(voice)

			if "Amy" in tok:
				print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Closing computer!")
				subprocess.call('shutdown -s -t 1')
			else:
				print(Fore.YELLOW + 'Blue: ' + Fore.RED + "Password is incorrect!")

		elif define_command(tok,filtered_tok, find_synonyms("restart"), ["restart","computer"]):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "What's the super user's password?")
			voice = speech()
			print(voice)
			tok, filtered_tok = process_speech(voice)

			if "Amy" in tok:
				print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Restarting computer!")
				subprocess.call('shutdown -r -t 1')
			else:
				print(Fore.YELLOW + 'Blue: ' + Fore.RED + "Password is incorrect!")
		elif define_command(tok,filtered_tok, find_synonyms("weather"), ["what","weather"]):
			print('Weather')
		else:
			print(Fore.YELLOW + 'Blue: ' + Fore.RED + "This commmand doesn't exsist!") 

		blue = False