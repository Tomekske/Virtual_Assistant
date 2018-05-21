#===============================================================================#
#Title           :blue                                                          #
#Description     :Virtual assitant                                              #
#Author          :joostenstomek@gmail.com                                       #
#Date            :29/04/2018                                                    #
#Version         :1.0.18                                                        #
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
from Modules.Core import core_functions, speech_functions
import Modules.Weather.Weather as Weather
import Modules.ConfigHandler.ConfigHandler as ConfigHandler


argc = len(sys.argv) #check for commandline argumens
c = ConfigHandler.Config('Config/config.ini') #Congif object
if argc > 1:
	if sys.argv[1] == '-c':		
		init(autoreset=True) #reset letter color to default value
		core_functions.consoleWrite(Fore.GREEN, 'Downloading AVbin10-win64')
		os.system('explorer.exe https://github.com/downloads/AVbin/AVbin/AVbin10-win64.exe')
		core_functions.consoleWrite(Fore.GREEN, 'Downloading GIT for commandline')
		os.system('explorer.exe https://git-scm.com/download/win')
		core_functions.consoleWrite(Fore.GREEN, 'Downloading NLTK tools')
		nltk.download()
		exit(1)
	elif sys.argv[1] == '-t':
		if argc == 3:
			if sys.argv[2] == 'blue':
				init(autoreset=True) #reset letter color to default value
				core_functions.consoleWrite(Fore.GREEN,'Testing Blue')
				os.system('python -W ignore Test/test_Blue.py')
				exit(1)
		else:
			init(autoreset=True) #reset letter color to default value
			core_functions.consoleWrite(Fore.GREEN,'Testing ConfigHandler module')
			os.system('python -W ignore Test/test_ConfigHandler.py')

			core_functions.consoleWrite(Fore.GREEN,'Testing ResponseHandler module')
			os.system('python -W ignore Test/test_ResponseHandler.py')

			core_functions.consoleWrite(Fore.GREEN,'Testing Weather module')
			os.system('python -W ignore Test/test_Weather.py')

			core_functions.consoleWrite(Fore.GREEN,'Testing Blue')
			os.system('python -W ignore Test/test_Blue.py')
			exit(1)			

	elif sys.argv[1] == '-u':
		init(autoreset=True) #reset letter color to default value
		core_functions.consoleWrite(Fore.YELLOW, 'Updating modules!')
		os.system('call Download/download_modules_GIT.bat')
		exit(1)
	elif sys.argv[1] == '-l':
		os.system('python Modules/Accent/train_speech.py')
		exit(1)
	elif sys.argv[1] == '-d':
		os.system('python setup.py install')
	

while True:
	init(autoreset=True) #reset letter color to default value
	voice = speech_functions.speech()

	tokenized, filtered_tok = core_functions.process_speech(voice)

	print('Tokenized:', tokenized)
	print('filtered_tok:', filtered_tok)

	if core_functions.define_command(tokenized, ["what","time"]):
		utc = arrow.utcnow()
		now = utc.format('HH:mm:ss')
		ntime = utc.format('HH:mm')
		core_functions.consoleWrite(Fore.WHITE, now)
		speech_functions.tts(ntime)

	elif core_functions.define_command(tokenized, ["set","password"]):
		option = c.checkOption('Password', 'user')

		#check if there is a password
		if not option:
			speech_functions.setPassword() #create new password

		else: #Change old password
			speech_functions.tts('Say old password')
			core_functions.consoleWrite(Fore.WHITE,'Please enter old password')
			voice = speech_functions.speech()
			tok, filtered_tok = core_functions.process_speech(voice)

			if speech_functions.checkPassword(voice):
				speech_functions.tts('Say new password')
				core_functions.consoleWrite(Fore.WHITE,'Please enter new password')
				speech_functions.setPassword()
			else:
				core_functions.consoleWrite(Fore.RED,"Old password is incorrect try again!")
				speech_functions.sound('Sounds/beep_error.mp3')				
   
	elif core_functions.define_command(tokenized,['test','password']):
		core_functions.consoleWrite(Fore.WHITE,'Please say password')
		voice = speech_functions.speech()

		if speech_functions.checkPassword(voice):
			core_functions.consoleWrite(Fore.GREEN,'Password is correct')
		else:
			core_functions.consoleWrite(Fore.RED,'Password is incorrect')

	elif core_functions.define_command(tokenized, ["close","computer"]):
		print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "What's the super user's password?")
		voice = speech_functions.speech()

		if speech_functions.checkPassword(voice):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Closing computer!")
			speech_functions.sound('Sounds/beep_ok.mp3')
			subprocess.call('shutdown -s -t 1')
		else:
			print(Fore.YELLOW + 'Blue: ' + Fore.RED + "Password is incorrect!")
			speech_functions.sound('Sounds/beep_error.mp3')


	elif core_functions.define_command(tokenized, ["restart","computer"]):
		core_functions.consoleWrite(Fore.WHITE, "What's the super user's password?")
		voice = speech_functions.speech()

		if speech_functions.checkPassword(voice):
			core_functions.consoleWrite(Fore.WHITE, "Restarting computer!")
			speech_functions.sound('Sounds/beep_ok.mp3')
			subprocess.call('shutdown -r -t 1')
		else:
			core_functions.consoleWrite(Fore.RED, "Password is incorrect!")
			speech_functions.sound('Sounds/beep_error.mp3')

	elif core_functions.define_command(tokenized, ["what","weather"]):
		for l in filtered_tok:
			w = Weather.Weather(l,'Config/config.ini')
		text = 'The temperature in {0} is {1} degrees'.format(w.location,round(w.temperature))
		core_functions.consoleWrite(Fore.WHITE, text)
		speech_functions.tts(text)


	elif core_functions.define_command(tokenized, ["exit"]):
		core_functions.consoleWrite(Fore.RED, 'Exit')
		speech_functions.sound('Sounds/beep_ok.mp3')
		exit(1)

	elif core_functions.define_command(tokenized, ["open","delete","file"]):
		core_functions.consoleWrite(Fore.WHITE, 'Opening delete content log file')
		speech_functions.sound('Sounds/beep_ok.mp3')
		subprocess.call('notepad D:\Log\delete_content.log')
	
	elif core_functions.define_command(tokenized,['open', 'folder']):
		core_functions.folders(tokenized)

	elif core_functions.define_command(tokenized, ["close","all","folders"]):
		core_functions.consoleWrite(Fore.WHITE, 'All folders are closed')
		speech_functions.sound('Sounds/beep_ok.mp3')
		os.system('cmd /c "taskkill /f /im explorer.exe && start explorer"')

	else:
		core_functions.consoleWrite(Fore.RED, "This commmand doesn't exsist!")
		speech_functions.sound('Sounds/beep_error.mp3')
