#===============================================================================#
#Title           :train_speech                                                  #
#Description     :train specific words for their pronunciation                  #
#Author          :joostenstomek@gmail.com                                       #
#Date            :29/04/2018                                                    #
#Version         :1.0.1                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import ConfigHandler
import core_functions as cf
import speech_recognition as sr
from colorama import Fore, Back, Style, init
import re
from collections import namedtuple



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
	options = c.getOptions('Command')
	options.sort() #sort option by alphabet

	print('\r\n')
	drawLine('#','=','#',29)
	print('# Commands already registered #')
	drawLine('#','-','#',29)


	newMenu = namedtuple('newMenu', ['hash1','word','hash2'])
	new_menu = []

	#get enteries from tuple
	for entry in new_menu:
	    index = str(getattr(entry,'index')).ljust(1)
	    point = getattr(entry,'point').ljust(3)
	    descr = getattr(entry,'description').ljust(15)
	    print('{0}{1}{2}'.format(index,point,descr))

	#append option to menu
	for o in options:
		new_menu.append(newMenu('#',o, '#'))

	#get enteries from tuple	
	for entry in new_menu:
	    index = str(getattr(entry,'hash1')).ljust(2)
	    point = getattr(entry,'word').ljust(28)
	    descr = getattr(entry,'hash2').ljust(1)
	    print('{0}{1}{2}'.format(index,point,descr))

	drawLine('#','=','#',29)


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
	options = c.getOptions('Command')
	options.sort()
	counter = 0
	print('\r\n')
	drawLine('#','=','#',29)
	print('# Commands already registered #')
	drawLine('#','-','#',29)



	oldMenu = namedtuple('oldMenu', ['hash1','number','point','word','hash2'])
	old_menu = []



	for o in options:
		old_menu.append(oldMenu('#',counter+1,'.',o, '#'))
		counter += 1

	for entry in old_menu:
	    hash1 = str(getattr(entry,'hash1')).ljust(2)
	    number = str(getattr(entry,'number')).ljust(1)
	    point = str(getattr(entry,'point')).ljust(2)
	    word = getattr(entry,'word').ljust(25)
	    hash2 = getattr(entry,'hash2').ljust(1)
	    print('{0}{1}{2}{3}{4}'.format(hash1,number,point,word,hash2))


	drawLine('#','-','#',29)

	word = input('What word would you like to re-train: ')
	option = options[int(word) - 1]

	old = c.readData('Command',option)
	formated = re.split(r'[,]+|,', old) #split on ',' and space
	file.removeOption('Command', option) #remove option from config file

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
	c.writeData('Command',option,s) #write data to the config file	



##
## @brief      Function to display the synonym menu
## @param      file  The config file you wan to write data to
## @return     None
##
def synonyms_menu(file):
	print('\r\n')
	mainMenu = namedtuple('mainMenu', ['index','point','description'])
	main_menu = []
	main_menu.append(mainMenu(1,'.', 'New symomym'))
	main_menu.append(mainMenu(2,'.', 'Add to exsisting word'))
	main_menu.append(mainMenu(3,'.', 'Exit'))
	for entry in main_menu:
		index = str(getattr(entry,'index')).ljust(1)
		point = getattr(entry,'point').ljust(3)
		descr = getattr(entry,'description').ljust(15)
		print('{0}{1}{2}'.format(index,point,descr))


	choice = input('Choose: ')
	if choice == '1':
		options = c.getOptions('Command')
		options.sort()

		print('\r\n')
		drawLine('#','=','#',29)
		print('# Commands already registered #')
		drawLine('#','-','#',29)


		newMenu = namedtuple('newMenu', ['hash1','word','hash2'])
		new_menu = []
		for entry in new_menu:
			index = str(getattr(entry,'index')).ljust(1)
			point = getattr(entry,'point').ljust(3)
			descr = getattr(entry,'description').ljust(15)
			print('{0}{1}{2}'.format(index,point,descr))

		for o in options:
			new_menu.append(newMenu('#',o, '#'))

		for entry in new_menu:
			index = str(getattr(entry,'hash1')).ljust(2)
			point = getattr(entry,'word').ljust(28)
			descr = getattr(entry,'hash2').ljust(1)
			print('{0}{1}{2}'.format(index,point,descr))

		drawLine('#','=','#',29)


		x = input('Search for synonyms: ')

		syn = cf.find_synonyms(x)
		print(syn)
		s = listToString(set(syn)) #convert list to string
		c.writeData('Command',x,s) #write data to the config file

	elif choice == '2':
		options = c.getOptions('Command')
		options.sort()
		counter = 0
		print('\r\n')
		drawLine('#','=','#',29)
		print('# Commands already registered #')
		drawLine('#','-','#',29)

		oldMenu = namedtuple('oldMenu', ['hash1','number','point','word','hash2'])
		old_menu = []

		for o in options:
			old_menu.append(oldMenu('#',counter+1,'.',o, '#'))
			counter += 1

		for entry in old_menu:
			hash1 = str(getattr(entry,'hash1')).ljust(2)
			number = str(getattr(entry,'number')).ljust(1)
			point = str(getattr(entry,'point')).ljust(2)
			word = getattr(entry,'word').ljust(25)
			hash2 = getattr(entry,'hash2').ljust(1)
			print('{0}{1}{2}{3}{4}'.format(hash1,number,point,word,hash2))


		drawLine('#','-','#',29)

		word = input('What word would you like to re-train: ')
		option = options[int(word) - 1]

		old = c.readData('Command',option)
		formated = re.split(r'[,]+|,', old) #split on ',' and space
		file.removeOption('Command', option) #remove option from config file
		s = ""
		syn = cf.find_synonyms(options[int(word) - 1])

		for s in syn:
			formated.append(s)

		s = listToString(set(formated)) #convert list to string
		c.writeData('Command',options[int(word) - 1],s) #write data to the config file
	elif choice == '3':
		exit(1)



##
## @brief      Draws a line.in console
## @param      start   The start symbol
## @param      symbol  The symbol you want to use
## @param      stop    The stop symbol
## @param      amount  The amount of times you want to repeat the symbol
## @return     None
##
def drawLine(start,symbol,stop,amount):
	line = start
	for i in range(0,amount):
		line += symbol
	line += stop
	print(line)



init(autoreset=True) #reset letter color to default value
c = ConfigHandler.Config('trained_speech.ini')
mainMenu = namedtuple('mainMenu', ['index','point','description'])
main_menu = []

main_menu.append(mainMenu(1,'.', 'New word'))
main_menu.append(mainMenu(2,'.', 'Old word'))
main_menu.append(mainMenu(3,'.', 'Synonyms'))
main_menu.append(mainMenu(4,'.', 'Exit'))

for entry in main_menu:
    index = str(getattr(entry,'index')).ljust(1)
    point = getattr(entry,'point').ljust(3)
    descr = getattr(entry,'description').ljust(15)
    print('{0}{1}{2}'.format(index,point,descr))


choice = input('Choose: ')
if choice == '1':
	new_menu(c)
elif choice == '2':
	old_menu(c)
elif choice == '3':
	synonyms_menu(c)
elif choice == '4':
	exit(1)
else:
	print('Wrong option')