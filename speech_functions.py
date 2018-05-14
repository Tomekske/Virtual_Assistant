#===============================================================================#
#Title           :speech_functions                                              #
#Description     :Functions used for speech                                     #
#Author          :joostenstomek@gmail.com                                       #
#Date            :14/05/2018                                                    #
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
from core_functions import *
import os
import ConfigHandler
import sys
import hashlib
from gtts import gTTS
import pyglet
import time
from speech_functions import *



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
		sound('Sounds/beep.mp3')
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
		voice = speech()
		password.append(voice)
		counter += 1

	#Check if all 3 samples are the same
	if password[0] == password[1] == password[2]:
		c.writeData('Password','User',sha224(password[0])) #write hashed password to config file	
		consoleWrite(Fore.GREEN,"Password's succesfully set!")
		sound('Sounds/beep_ok.mp3')
	else:
		consoleWrite(Fore.RED,"Passwords don't match, please try again!")	
		sound('Sounds/beep_error.mp3')



##
## @brief      Function that check if password is correct
## @param      password  The spoken password
## @return     True or False dependin wether password is correct or not
##
def checkPassword(password):
	c = ConfigHandler.Config()

	if sha224(password) == c.readData('Password','user'):
		sound('Sounds/beep_ok.mp3')
		return True
	else:
		sound('Sounds/beep_error.mp3')
		return False



##
## @brief      Function to play sound from a media file
## @param      sound  The file location of the media file
## @return     None
##
def sound(sound):
	file = os.path.isfile(sound) #check if path to media file exists

	if file:
		music = pyglet.media.load(sound)
		music.play()
		time.sleep(music.duration)
	else:
		consoleWrite(Fore.RED,"Mediafile not found!")	



##
## @brief      Function for text to speech
## @param      text  The text you want to translate to speech
## @return     None
##
def tts(text):
	file = gTTS(text = text, lang = 'en')
	filename = 'Sounds/tts.mp3'
	file.save(filename)
	sound(filename)