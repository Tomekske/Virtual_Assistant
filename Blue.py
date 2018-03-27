import speech_recognition as sr
from colorama import Fore, Back, Style, init
import arrow
import subprocess
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords


while True:
	init(autoreset=True)
	# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print(Fore.YELLOW + "Say something:")
	    audio = r.listen(source)

	# Speech recognition using Google Speech Recognition
	try:
		voice = r.recognize_google(audio)
		print(voice)

		tok = word_tokenize(voice)
		print('Tokenized:',tok)

		sw = set(stopwords.words("english"))

		filtered_tok = []

		for w in tok:
			if w not in sw:
				filtered_tok.append(w)
		print('Filtered:',filtered_tok)

		

	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))