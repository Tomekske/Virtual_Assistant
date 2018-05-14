#===============================================================================#
#Title           :core_functions                                                #
#Description     :Functions used in blue.py                                     #
#Author          :joostenstomek@gmail.com                                       #
#Date            :25/04/2018                                                    #
#Version         :1.0.3                                                         #
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
import configparser
import requests #http request libray
import json
import ConfigHandler
import ResponseHandler
import re
import hashlib
import os
from speech_functions import *



##
## @brief      Function to find synonyms for a word
## @param      word  Word you want to find a synonym for
## @return     A list of all synonyms for that word
##
def find_synonyms(word):	
	synonyms = []

	#loop over all the synonyms of a certain word
	for syn in wordnet.synsets(word):

		#loop over all lemmas in synonyms
		for l in syn.lemmas(): #lemmas are base words
			synonyms.append(l.name()) #add synonym to synonyms list
	return set(synonyms)



##
## @brief      Function to process the string received from speech
## @param      voice  String that was converted from speech
## @return     A tokenized list and a filtered tokenized list without stopwords
##
def process_speech(voice):
	filtered_tok = []

	tokenized = word_tokenize(voice) #tokenize speech string
	sw = set(stopwords.words("english")) #get all 'english'stopwords from dictionary

	#loop over tokenized elements
	for w in tokenized:

		#if token is not in the stopword list append it to filtered_tok list
		if w not in sw:
			filtered_tok.append(w)
	return tokenized,filtered_tok



##
## @brief      Function to define the command sequence
## @param      tokenized  Tokenized speech list
## @param      command     The command you want to perform a list
## @return     True if all  elements in the list are true, else it'll returns false
##
def define_command(tokenized, command):
	config = ConfigHandler.Config('trained_speech.ini')

	check_commands = []
	blue = False
	counter = 0

	for t in tokenized:
		#check if blue is in tokenized or if a token if in accent list
		if (t in config.readData('Command', 'blue')) or ('blue' in tokenized):
			blue = True
	#if blue is in command excecute this block of code
	if blue:
		#loop over every command in command list
		for c in command:
			check_commands.append(False) #make sure all elemets in the boolean list are false
			accent_string = config.readData('Command', c) #get accent string from config file according to command
			#check if accent is in the file, split string into tokens and store them in a list
			if accent_string != 'ERROR_DATA':
				accent_list = accent_string.split(',') #split on ',' and space
				#loop over every token in tokenized list
				for t in tokenized:
					#if command = token or if token is in accent list append true
					if (c == t) or (t in accent_list):
						check_commands[counter] = True
			#if accent string is invallid excecute following code
			else:
				#check if command is in tokenized
				if c in tokenized:
					check_commands[counter] = True
			counter += 1 #inrease counter
	#if blue is not in command then return false
	else:
		return False

	#check if all elements are true in the list
	if all(check_commands):
		return True
	else:
		return False



##
## @brief      Function to write to console 
## @param      color  The color
## @param      text   The text
## @return     { description_of_the_return_value }
##
def consoleWrite(color, text):
	print(Fore.YELLOW + 'Blue: ' + color + text)


##
## @brief      Function to simplify hashing function (sha224)
## @param      word  The word you want to hash
## @return     Return hashed word
##
def sha224(word):
	return hashlib.sha224(str.encode(word)).hexdigest()



##
## @brief      To open folders in windows explorer
## @param      tokenized  The tokenized speech
## @return     None
##
def folders(tokenized):
	c = ConfigHandler.Config()

	for t in tokenized:
		directory = c.readData('Folders',t) #check if option exists
		path = os.path.isdir(directory) #check if directory exists

		#if directory exists open the folder
		if directory != 'ERROR_DATA' and path:
			consoleWrite(Fore.WHITE, 'Opening {0} folder'.format(t.lower()))
			os.system('explorer {0}'.format(directory)) #Open folder in windows explorer 
			sound('Sounds/beep_ok.mp3')