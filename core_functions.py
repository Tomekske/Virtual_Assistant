#===============================================================================#
#Title           :core_functions                                                #
#Description     :Functions used in blue.py                                     #
#Author          :joostenstomek@gmail.com                                       #
#Date            :25/04/2018                                                    #
#Version         :1.0.0                                                         #
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
## @brief      Function to determinate whether the speech is a start command or not
## @param      filtered  Pass the filetered token list
## @return     A boolean whether the speech is a start command or not
##
def start_command(filtered):

	#check if command 'blue' is in filtered list
	if ("blue" in filtered):
			return True
	return False



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
## @param      unfiltered  Unfiltered token list
## @param      filtered    Filtered token list
## @param      synonyms    predefined list of synonyms
## @param      command     The command you want to perform a list
## @return     True if all  elements in the list are true, else it'll returns false
##
def define_command(unfiltered, filtered, synonyms, command):

	#list of question words
	exception_list = [	"what",
						"can",
						"who", 
						"where", 
						"when", 
						"why", 
						"which",
						"all",
						"how"]
	new_Command = []
	check_commands = []
	counter = 0
	blue = False

	#Check if blue is in the speech string
	if ('blue' in filtered):
		blue = True

	#loop over command list
	if blue:
		for c in command:
			check_commands.append(False) #make sure all elemets in the boolean list are false
			#if command is in question loop over unfiltered tokens add it to check_commands
			if c in exception_list:
				for u in unfiltered:
					#Check if unfiltered token is in questionlist and command token is in unfiltered list
					if (u in exception_list) and (c in unfiltered):
						check_commands[counter] = True #set check_command command postion to true
			else:
				#loop over filtered items
				for f in filtered:
					#Check if filtered token is in synonyms and command token is in filtered list
					if (f in synonyms) and (c in filtered):
						check_commands[counter] = True #set check_command command postion to true
			counter += 1 #inrease counter
	else:
		return False
		#check if all elements are true in the list
	if all(check_commands):
		return True
	else:
		return False



def consoleWrite(color, text):
	print(Fore.YELLOW + 'Blue: ' + color + text) 
