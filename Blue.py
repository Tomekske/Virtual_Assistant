#===============================================================================#
#Title           :blue                                                          #
#Description     :Virtual assitant                                              #
#Author          :joostenstomek@gmail.com                                       #
#Date            :29/04/2018                                                    #
#Version         :1.0.12                                                        #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



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
import os
import ConfigHandler
import sys


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



argc = len(sys.argv)
if argc > 1:
	if sys.argv[1] == '-s':		
		init(autoreset=True) #reset letter color to default value

		consoleWrite(Fore.YELLOW, 'Installing modules!')

		os.system('call download_modules.bat')

		nltk.download()
		exit(1)


c = ConfigHandler.Config()
while True:
	init(autoreset=True) #reset letter color to default value

	voice = speech()
	
	tok, filtered_tok = process_speech(voice)
	print('Tokenized:', tok)
	print('filtered_tok:', filtered_tok)


	if define_command(tok,filtered_tok, find_synonyms("time"), ["what","time"]):
		utc = arrow.utcnow()
		now = utc.format('HH:mm:ss')
		consoleWrite(Fore.WHITE, now)

	elif define_command(tok,filtered_tok, find_synonyms("restart"), ["restart","computer"]):
		consoleWrite(Fore.WHITE, "What's the super user's password?")
		voice = speech()
		print(voice)
		tok, filtered_tok = process_speech(voice)

		if "Amy" in tok:
			consoleWrite(Fore.WHITE, "Restarting computer!")
			subprocess.call('shutdown -r -t 1')
		else:
			consoleWrite(Fore.RED, "Password is incorrect!")

	elif define_command(tok,filtered_tok, find_synonyms("weather"), ["what","weather"]):
		for l in filtered_tok:
			w = Weather(l)
		print(w.location)
		consoleWrite(Fore.WHITE, str(w.temperature))

	elif define_command(tok,filtered_tok, find_synonyms("exit"), ["exit"]):
		consoleWrite(Fore.RED, 'Exit')
		exit(1)

	elif define_command(tok,filtered_tok, find_synonyms("delete"), ["open","delete","file"]):
		consoleWrite(Fore.WHITE, 'Opening delete content log file')
		subprocess.call('notepad D:\Log\delete_content.log')
	
	elif define_command(tok,filtered_tok, find_synonyms("program"), ["open","program","folder"]):
		consoleWrite(Fore.WHITE, 'Opening program folder')
		os.system('explorer {0}'.format(c.readData('Folders','Programs')))


	elif define_command(tok,filtered_tok, find_synonyms("show"), ["open","show","folder"]):
		consoleWrite(Fore.WHITE, 'Opening serie folder')
		os.system('explorer {0}'.format(c.readData('Folders','Series')))

	elif define_command(tok,filtered_tok, find_synonyms("movie"), ["open","movie","folder"]):
		consoleWrite(Fore.WHITE, 'Opening movie folder')
		os.system('explorer {0}'.format(c.readData('Folders','Movies')))

	elif define_command(tok,filtered_tok, find_synonyms("music"), ["open","music","folder"]):
		consoleWrite(Fore.WHITE, 'Opening music folder')
		os.system('explorer {0}'.format(c.readData('Folders','Music')))

	elif define_command(tok,filtered_tok, find_synonyms("picture"), ["open","picture","folder"]):
		consoleWrite(Fore.WHITE, 'Opening picture folder')
		os.system('explorer {0}'.format(c.readData('Folders','Pictures')))

	elif define_command(tok,filtered_tok, find_synonyms("game"), ["open","game","folder"]):
		consoleWrite(Fore.WHITE, 'Opening game folder')
		os.system('explorer {0}'.format(c.readData('Folders','Games')))

	else:
		consoleWrite(Fore.RED, "This commmand doesn't exsist!")
