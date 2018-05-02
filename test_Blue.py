#===============================================================================#
#Title           :test_blue                                                     #
#Description     :Unit test to test virtual assistant code                      #
#Author          :joostenstomek@gmail.com                                       #
#Date            :16/04/2018                                                    #
#Version         :1.0.3                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
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
		self.speech = "blue what time is it"
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
	## @brief     Method to get and test if certain words are synonyms
	##
	def test_Synonyms(self):
		self.assertIn('meter',self.synonyms)
		self.assertNotIn('weather',core_functions.find_synonyms('time'))



	##
	## @brief     Method to determintate wether speech command is valid or invallid
	##
	def test_command(self):
		print('\r\nTokenized:', self.tokenized)
		print('Filtered:', self.filtered)
		print('Synonyms:', self.synonyms,"\r\n\r\n")


		self.assertTrue(core_functions.define_command(self.tokenized, self.filtered, self.synonyms, ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue what is the weather in Brussels")[0],core_functions.process_speech("blue what is the weather in Brussels")[1], core_functions.find_synonyms('weather'), ['what','weather']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("new what time is it")[0],core_functions.process_speech("new what time is it")[1], core_functions.find_synonyms('time'), ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("new what's time is it")[0],core_functions.process_speech("new what's time is it")[1],core_functions.find_synonyms('time'), ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue open music folder")[0],core_functions.process_speech("blue open music folder")[1],core_functions.find_synonyms('music'), ['open','music','folder']))

		self.assertFalse(core_functions.define_command(core_functions.process_speech("open music folder")[0],core_functions.process_speech("open music folder")[1], core_functions.find_synonyms('weather'), ['blue','what','weather']))
		self.assertFalse(core_functions.define_command(core_functions.process_speech("fdsf what time is it")[0],core_functions.process_speech("fdsf what time is it")[1], core_functions.find_synonyms('weather'), ['blue','what','time']))
		self.assertFalse(core_functions.define_command(core_functions.process_speech("what time is it")[0],core_functions.process_speech("what time is it")[1], core_functions.find_synonyms('weather'), ['what','time']))
		self.assertFalse(core_functions.define_command(core_functions.process_speech("new what time is it")[0],core_functions.process_speech("new what time is it")[1], core_functions.find_synonyms('weather'), ['what','time']))



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