#===============================================================================#
#Title           :blue                                                          #
#Description     :Virtual assitant                                              #
#Author          :joostenstomek@gmail.com                                       #
#Date            :29/04/2018                                                    #
#Version         :1.0.17                                                        #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import sys,os,time,subprocess,hashlib
import speech_recognition as sr
from colorama import Fore, Back, Style, init
import arrow
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from gtts import gTTS
import pyglet
from Modules.speech_functions import *
from Modules.core_functions import *
from Weather import Weather 
import ConfigHandler


argc = len(sys.argv) #check for commandline argumens
c = ConfigHandler.Config('Config/config.ini') #Congif object

if argc > 1:
	if sys.argv[1] == '-c':		
		init(autoreset=True) #reset letter color to default value
		consoleWrite(Fore.GREEN, 'Downloading AVbin10-win64')
		os.system('explorer.exe https://github.com/downloads/AVbin/AVbin/AVbin10-win64.exe')
		consoleWrite(Fore.GREEN, 'Downloading GIT for commandline')
		os.system('explorer.exe https://git-scm.com/download/win')
		nltk.download()
		exit(1)
	elif sys.argv[1] == '-t':
		if argc == 3:
			if sys.argv[2] == 'blue':
				init(autoreset=True) #reset letter color to default value
				consoleWrite(Fore.GREEN,'Testing Blue')
				os.system('python -W ignore Test/test_ConfigHandler.py')
				exit(1)
		else:
			init(autoreset=True) #reset letter color to default value
			consoleWrite(Fore.GREEN,'Testing ConfigHandler module')
			os.system('python -W ignore Test/test_ConfigHandler.py')

			consoleWrite(Fore.GREEN,'Testing ResponseHandler module')
			os.system('python -W ignore Test/test_ResponseHandler.py')

			consoleWrite(Fore.GREEN,'Testing Weather module')
			os.system('python -W ignore Test/test_Weather.py')

			consoleWrite(Fore.GREEN,'Testing Blue')
			os.system('python -W ignore Test/test_Blue.py')
			exit(1)			

	elif sys.argv[1] == '-u':
		init(autoreset=True) #reset letter color to default value
		consoleWrite(Fore.YELLOW, 'Updating modules!')
		os.system('call Download/download_modules_GIT.bat')
		exit(1)
	elif sys.argv[1] == '-l':
		os.system('python Modules/train_speech.py')
		exit(1)
	elif sys.argv[1] == '-d':
		os.system('python setup.py install')
	


while True:
	init(autoreset=True) #reset letter color to default value
	voice = speech()

	tokenized, filtered_tok = process_speech(voice)

	print('Tokenized:', tokenized)
	print('filtered_tok:', filtered_tok)

	if define_command(tokenized, ["what","time"]):
		utc = arrow.utcnow()
		now = utc.format('HH:mm:ss')
		ntime = utc.format('HH:mm')
		consoleWrite(Fore.WHITE, now)
		tts(ntime)

	elif define_command(tokenized, ["set","password"]):
		option = c.checkOption('Password', 'user')

		#check if there is a password
		if not option:
			setPassword() #create new password

		else: #Change old password
			consoleWrite(Fore.WHITE,'Please enter old password')
			voice = speech()
			tok, filtered_tok = process_speech(voice)

			if checkPassword(voice):
				consoleWrite(Fore.WHITE,'Please enter new password')
				tts('Enter new password')
				setPassword()
			else:
				consoleWrite(Fore.RED,"Old password is incorrect try again!")
				sound('Sounds/beep_error.mp3')				
   
	elif define_command(tokenized,['test','password']):
		consoleWrite(Fore.WHITE,'Please say password')
		voice = speech()

		if checkPassword(voice):
			consoleWrite(Fore.GREEN,'Password is correct')
		else:
			consoleWrite(Fore.RED,'Password is incorrect')

	elif define_command(tokenized, ["close","computer"]):
		print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "What's the super user's password?")
		voice = speech()

		if checkPassword(voice):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Closing computer!")
			sound('Sounds/beep_ok.mp3')
			subprocess.call('shutdown -s -t 1')
		else:
			print(Fore.YELLOW + 'Blue: ' + Fore.RED + "Password is incorrect!")
			sound('Sounds/beep_error.mp3')


	elif define_command(tokenized, ["restart","computer"]):
		consoleWrite(Fore.WHITE, "What's the super user's password?")
		voice = speech()

		if checkPassword(voice):
			consoleWrite(Fore.WHITE, "Restarting computer!")
			sound('Sounds/beep_ok.mp3')
			subprocess.call('shutdown -r -t 1')
		else:
			consoleWrite(Fore.RED, "Password is incorrect!")
			sound('Sounds/beep_error.mp3')

	elif define_command(tokenized, ["what","weather"]):
		for l in filtered_tok:
			w = Weather(l,'Config/config.ini')
		text = 'The temperature in {0} is {1} degrees'.format(w.location,round(w.temperature))
		consoleWrite(Fore.WHITE, text)
		tts(text)


	elif define_command(tokenized, ["exit"]):
		consoleWrite(Fore.RED, 'Exit')
		sound('Sounds/beep_ok.mp3')
		exit(1)

	elif define_command(tokenized, ["open","delete","file"]):
		consoleWrite(Fore.WHITE, 'Opening delete content log file')
		sound('Sounds/beep_ok.mp3')
		subprocess.call('notepad D:\Log\delete_content.log')
	
	elif define_command(tokenized,['open', 'folder']):
		folders(tokenized)

	elif define_command(tokenized, ["close","all","folders"]):
		consoleWrite(Fore.WHITE, 'All folders are closed')
		sound('Sounds/beep_ok.mp3')
		os.system('cmd /c "taskkill /f /im explorer.exe && start explorer"')

	else:
		consoleWrite(Fore.RED, "This commmand doesn't exsist!")
		sound('Sounds/beep_error.mp3')
