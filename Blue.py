import speech_recognition as sr
from colorama import Fore, Back, Style, init
import arrow
import subprocess
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


def speech():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print(Fore.YELLOW + "Say something:")
		audio = r.listen(source)	

	try:
		voice = r.recognize_google(audio)
		return voice
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		return "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
		print("Could not request resulsts from Google Speech Recognition service; {0}".format(e))
		return "Could not request results from Google Speech Recognition service; {0}".format(e)

def find_synonyms(word):	
	synonyms = []

	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
	print(set(synonyms))
	return set(synonyms)

def start_command(filtered):
	if ("blue" in filtered):
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + "Can I do somthing for you ?")
			return True
	return False

def process_speech(voice):
	tok = word_tokenize(voice)
	print('Tokenized:',tok)

	sw = set(stopwords.words("english"))

	filtered_tok = []

	for w in tok:
		if w not in sw:
			filtered_tok.append(w)

	return tok,filtered_tok



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
		print(blue)
		print("hieeer")

		tok, filtered_tok = process_speech(voice)

		if ('time' in filtered_tok) and ('time' in sTime):
			utc = arrow.utcnow()
			now = utc.format('HH:mm:ss')
			print(Fore.YELLOW + 'Blue: ' + Fore.WHITE + now) 
		else:
			print(Fore.YELLOW + 'Blue: ' + Fore.RED + "This commmand doesn't exsist!") 

		blue = False