#===============================================================================#
#Title           :train_speech                                                  #
#Description     :train specific words for their pronunciation                  #
#Author          :joostenstomek@gmail.com                                       #
#Date            :29/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import ConfigHandler
import core_functions
import speech_recognition as sr
from colorama import Fore, Back, Style, init
import re



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



##
## @brief      Convert a list to a formatted string
## @param      lst   The list you want to convert to a string
## @return     Formatted string (word1,word2,word3)
##
def listToString(lst):
	l_string = ''

	#loop over all the elements in the list
	for l in lst:
		l_string += '{0},'.format(l) #add each word in a string
	l_string = l_string[:-1] #remove comma at the end of the string
	return l_string



##
## @brief      Function to display the add new word menu
## @param      file  The config file you wan to write data to
## @return     None
##
def new_menu(file):
	word = input('What word would you like to train: ')
	repeat = input('Repeat: ')
	counter = 0
	words = []
	s = ""

	#Repeat loop x-times
	while counter <= (int(repeat) - 1):
		print('Round:', counter + 1)
		ns = speech()
		print('You said:', ns)
		words.append(ns) #append word to a list
		counter += 1

	s = listToString(set(words)) #convert list to string
	c.writeData('Command',word,s) #write data to the config file



##
## @brief      Function to display the edit old word menu
## @param      file  The config file you wan to write data to
## @return     None
##
def old_menu(file):
	word = input('What word would you like to re-train: ')
	old = c.readData('Command',word)
	formated = re.split(r'[,]+|,', old) #split on ',' and space
	file.removeOption('Command', word) #remove option from config file

	repeat = input('Repeat: ')
	counter = 0
	words = []
	s = ""

	#Repeat loop x-times	
	while counter <= (int(repeat) - 1):
		print('Round:', counter + 1)
		ns = speech()
		print('You said:', ns)
		formated.append(ns)
		counter += 1

	s = listToString(set(formated)) #convert list to string
	c.writeData('Command',word,s) #write data to the config file	

init(autoreset=True) #reset letter color to default value
c = ConfigHandler.Config('trained_speech.ini')

#Menu structure
print('New word: 1\r\nOld word: 2')
choice = input('Choose: ')
if choice == '1':
	new_menu(c)
elif choice == '2':
	old_menu(c)
else:
	print('Wrong option')