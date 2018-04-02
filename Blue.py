import speech_recognition as sr
from colorama import Fore, Back, Style, init
import arrow
import subprocess
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer



##
## @brief      Function to start recording speech
## @return     Speech as a string
##
def speech():
	r = sr.Recognizer() #make an object

	#use microphone as source
	with sr.Microphone() as source:
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

	print(set(synonyms))
	return set(synonyms)



##
## @brief      Function to determinate whether the speech is a start command or not
## @param      filtered  Pass the filetered token list
## @return     A boolean whether the speech is a start command or not
##
def start_command(filtered):

	#check if command 'blue' is in filtered list
	if ("blue" in filtered):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Can I do somthing for you ?")
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
	print('Tokenized:',tok)

	stopwords = set(stopwords.words("english")) #get all 'english'stopwords from dictionary

	#loop over tokenized elements
	for w in tokenized:

		#if token is not in the stopword list append it to filtered_tok list
		if w not in stopwords:
			filtered_tok.append(w)

	print('filtered_tok:',filtered_tok)

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
	question_list = [	"what",
						"can",
						"who", 
						"where", 
						"when", 
						"why", 
						"which", 
						"how"]
	new_Command = []
	check_commands = []
	counter = 0

	#loop over command list
	for c in command:
		chech_commands.append(False) #make sure all elemets in the boolean list are false

		#if command is in question loop over unfiltered tokens add it to check_commands
		if c in question_list:
			for u in unfiltered:

				#Check if unfiltered token is in questionlist and command token is in unfiltered list
				if (u in question_list) and (c in unfiltered):
					check_commands[counter] = True #set check_command command postion to true

		else:

			#loop over filtered items
			for f in filtered:

				#Check if filtered token is in synonyms and command token is in filtered list
				if (f in synonyms) and (c in filtered):
					check_commands[counter] = True #set check_command command postion to true
		counter += 1 #inrease counter

		#check if all elements are true in the list
		if all(check_commands):
			return True
		else:
			return False
	return False



sTime = find_synonyms("time")
sRestart = find_synonyms("restart")
sShutdown = find_synonyms("shut")
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
		voice = speech()

		tok, filtered_tok = process_speech(voice)

		if define_command(tok,filtered_tok, sTime, ["what","time"]):
			utc = arrow.utcnow()
			now = utc.format('HH:mm:ss')
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + now) 
		else:
			print(Fore.YELLOW + 'Blue: ' + Fore.RED + "This commmand doesn't exsist!") 

		blue = False