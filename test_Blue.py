#===============================================================================#
#Title           :test_blue														#
#Description     :Unittest to test virtual assistant code						#
#Author          :joostenstomek@gmail.com										#
#Date            :16/04/2018													#
#Version         :1.0.0															#
#Usage           :Python														#
#Python version  :3.6															#
#===============================================================================#



import unittest
import core_functions



##
## @brief      Class for test core functions.
##
class TestCoreFunctions(unittest.TestCase):

	##
	## @brief     Method to setup basic functionality for code reusability, get called in every test case
	##
	def setUp(self):
		self.speech = "what time is it"
		self.tokenized = core_functions.process_speech(self.speech)[0] #String to tokens
		self.filtered = core_functions.process_speech(self.speech)[1] #Filtered tokens without stopwords

		self.synonyms = core_functions.find_synonyms('time') #Get synonyms for 'time'



	##
	## @brief     Method to test if speech is correctly converted to tokenized and filtered
	##
	def test_processSpeech(self):		
		#Tokenized
		self.checkItemsInList(['what','time','it'], self.tokenized)
		self.checkItemsInList(['what','weather','in', 'Brussels'],core_functions.process_speech("what is the weather like in Brussels")[0])

		#Filtered
		self.checkItemsInList(['time'], self.filtered)
		self.checkItemsInList(['weather','Brussels'],core_functions.process_speech("what is the weather like in Brussels")[1])
		
		self.checkItemsNotInList(['weather'], self.filtered)
		self.checkItemsNotInList(['time','Antwerp'],core_functions.process_speech("what is the weather like in Brussels")[1])



	##
	## @brief     Method to check if the start command is 'blue' (name of assistant)
	##
	def test_startCommand(self):
		self.assertTrue(core_functions.start_command('blue'))
		self.assertFalse(core_functions.start_command('green'))



	##
	## @brief     Method to get and test if certain words are synonyms
	##
	def test_Synonyms(self):
		self.assertIn('meter',self.synonyms)
		self.assertNotIn('weather',core_functions.find_synonyms('time'))



	##
	## @brief     Method to determintate wether speech command is valid or invallid
	##
	def test_command(self):
		self.assertTrue(core_functions.define_command(self.tokenized, self.filtered, self.synonyms, ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("what is the weather like in Brussels")[0],core_functions.process_speech("what is the weather like in Brussels")[1], core_functions.find_synonyms('weather'), ['what','weather']))
	

	##
	## @brief     Helper method to check if multiple items are in the list
	##	
	def checkItemsInList(self,items,speech):
		for i in items:
			self.assertIn(i,speech) 



	##
	## @brief     Helper method to check if multiple items aren't in the list
	##	
	def checkItemsNotInList(self,items,speech):
		for i in items:
			self.assertNotIn(i,speech) 
		


if __name__ == '__main__':
	unittest.main()