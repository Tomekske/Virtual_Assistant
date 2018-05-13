#===============================================================================#
#Title           :blue                                                          #
#Description     :Virtual assitant                                              #
#Author          :joostenstomek@gmail.com                                       #
#Date            :29/04/2018                                                    #
#Version         :1.0.14                                                        #
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
import hashlib

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
		return voice.lower()
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		return "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
		print("Could not request resulsts from Google Speech Recognition service; {0}".format(e))
		return "Could not request results from Google Speech Recognition service; {0}".format(e)



##
## @brief      Sets the password for the superuser's commands
## @return     None
##
def setPassword():
	counter = 0
	password = []

	#Repeat conforming password 3 times
	while counter <= 2:
		consoleWrite(Fore.WHITE,'{0}. confirm password:'.format(counter + 1))
		password.append(voice)
		counter += 1

	#Check if all 3 samples are the same
	if password[0] == password[1] == password[2]:
		c.writeData('Password','User',sha224(password[0])) #write hashed password to config file	
		consoleWrite(Fore.GREEN,"Password's succesfully set!")
	else:
		consoleWrite(Fore.RED,"Passwords don't match, please try again!")	



##
## @brief      Function that check if password is correct
## @param      password  The spoken password
## @return     True or False dependin wether password is correct or not
##
def checkPassword(password):
	c = ConfigHandler.Config()

	if sha224(password) == c.readData('Password','user'):
		return True
	else:
		return False



#===============================================================================#
#                                                                               #
#                              Main program                                     #
#                                                                               #
#===============================================================================#



argc = len(sys.argv) #check for commandline argumens
c = ConfigHandler.Config() #Congif object

if argc > 1:
	if sys.argv[1] == '-c':		
		init(autoreset=True) #reset letter color to default value
		consoleWrite(Fore.YELLOW, 'Installing modules!')
		os.system('call download_modules.bat')
		nltk.download()
		exit(1)
	elif sys.argv[1] == '-t':
		if argc == 3:
			if sys.argv[2] == 'blue':
				init(autoreset=True) #reset letter color to default value
				consoleWrite(Fore.GREEN,'Testing Blue')
				os.system('python -W ignore test_Blue.py')
				exit(1)
		else:
			init(autoreset=True) #reset letter color to default value
			consoleWrite(Fore.GREEN,'Testing ConfigHandler module')
			os.system('python -W ignore test_ConfigHandler.py')

			consoleWrite(Fore.GREEN,'Testing ResponseHandler module')
			os.system('python -W ignore test_ResponseHandler.py')

			consoleWrite(Fore.GREEN,'Testing Weather module')
			os.system('python -W ignore test_Weather.py')

			consoleWrite(Fore.GREEN,'Testing Blue')
			os.system('python -W ignore test_Blue.py')
			exit(1)			

	elif sys.argv[1] == '-u':
		init(autoreset=True) #reset letter color to default value
		consoleWrite(Fore.YELLOW, 'Updating modules!')
		os.system('call download_modules.bat')
		exit(1)
	elif sys.argv[1] == '-l':
		os.system('python train_speech.py')
		exit(1)



while True:
	init(autoreset=True) #reset letter color to default value
	voice = speech()

	tokenized, filtered_tok = process_speech(voice)

	print('Tokenized:', tokenized)
	print('filtered_tok:', filtered_tok)

	if define_command(tokenized, ["what","time"]):
		utc = arrow.utcnow()
		now = utc.format('HH:mm:ss')
		consoleWrite(Fore.WHITE, now)

	elif define_command(tokenized, ["set","password"]):
		option = c.checkOption('Password', 'user')

		#check if there is a password
		if not option:
			setPassword() #create new password
		else: #Change old password
			consoleWrite(Fore.WHITE,'Please enter old password')
			voice = speech()
			tok, filtered_tok = process_speech(voice)

			if checkPassword(filtered_tok[0]):
				consoleWrite(Fore.WHITE,'Please enter new password')
				setPassword()
			else:
				consoleWrite(Fore.RED,"Old password is incorrect try again!")

	elif define_command(tokenized, ["close","computer"]):
		print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "What's the super user's password?")
		voice = speech()

		if checkPassword(voice):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Closing computer!")
			subprocess.call('shutdown -s -t 1')
		else:
			print(Fore.YELLOW + 'Blue: ' + Fore.RED + "Password is incorrect!")

	elif define_command(tokenized, ["restart","computer"]):
		consoleWrite(Fore.WHITE, "What's the super user's password?")
		voice = speech()

		if checkPassword(voice):
			consoleWrite(Fore.WHITE, "Restarting computer!")
			subprocess.call('shutdown -r -t 1')
		else:
			consoleWrite(Fore.RED, "Password is incorrect!")

	elif define_command(tokenized, ["what","weather"]):
		for l in filtered_tok:
			w = Weather(l)
		print(w.location)
		consoleWrite(Fore.WHITE, str(w.temperature))

	elif define_command(tokenized, ["exit"]):
		consoleWrite(Fore.RED, 'Exit')
		exit(1)

	elif define_command(tokenized, ["open","delete","file"]):
		consoleWrite(Fore.WHITE, 'Opening delete content log file')
		subprocess.call('notepad D:\Log\delete_content.log')
	
	elif define_command(tokenized, ["open","program","folder"]):
		consoleWrite(Fore.WHITE, 'Opening program folder')
		os.system('explorer {0}'.format(c.readData('Folders','Programs')))

	elif define_command(tokenized, ["open","show","folder"]):
		consoleWrite(Fore.WHITE, 'Opening serie folder')
		os.system('explorer {0}'.format(c.readData('Folders','Series')))

	elif define_command(tokenized, ["open","movie","folder"]):
		consoleWrite(Fore.WHITE, 'Opening movie folder')
		os.system('explorer {0}'.format(c.readData('Folders','Movies')))

	elif define_command(tokenized, ["open","music","folder"]):
		consoleWrite(Fore.WHITE, 'Opening music folder')
		os.system('explorer {0}'.format(c.readData('Folders','Music')))

	elif define_command(tokenized, ["open","picture","folder"]):
		consoleWrite(Fore.WHITE, 'Opening picture folder')
		os.system('explorer {0}'.format(c.readData('Folders','Pictures')))

	elif define_command(tokenized, ["open","game","folder"]):
		consoleWrite(Fore.WHITE, 'Opening game folder')
		os.system('explorer {0}'.format(c.readData('Folders','Games')))

	elif define_command(tokenized, ["close","all","folders"]):
		consoleWrite(Fore.WHITE, 'All folders are closed')
		os.system('cmd /c "taskkill /f /im explorer.exe && start explorer"')

	else:
		consoleWrite(Fore.RED, "This commmand doesn't exsist!")
