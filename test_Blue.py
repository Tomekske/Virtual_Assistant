#===============================================================================#
#Title           :test_blue                                                     #
#Description     :Unit test to test virtual assistant code                      #
#Author          :joostenstomek@gmail.com                                       #
#Date            :16/04/2018                                                    #
#Version         :1.0.6                                                         #
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
	def test_synonyms(self):
		self.assertIn('meter',self.synonyms)
		self.assertNotIn('weather',core_functions.find_synonyms('time'))



	##
	## @brief     Method to determintate wether speech command is valid or invallid
	##
	def test_command(self):
		#testing regular commands
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue what time is it")[0], ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue open music folder")[0], ['open','music','folder']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue reboot computer")[0], ['reboot','computer']))

		#testing synonyms
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue what clock is it")[0], ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue open music folders")[0], ['open','music','folder']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue reboot pc ")[0], ['reboot','computer']))
		
		#testing accent
		self.assertTrue(core_functions.define_command(core_functions.process_speech("new what clock is it")[0], ['what','time']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("new open music folders")[0], ['open','music','folder']))
		self.assertTrue(core_functions.define_command(core_functions.process_speech("blue reboots computers")[0], ['reboot','computer']))

		#testing incorrect cases
		self.assertFalse(core_functions.define_command(core_functions.process_speech("green what time is it")[0], ['what','time']))
		self.assertFalse(core_functions.define_command(core_functions.process_speech("blue open picture desk")[0], ['open','music','folder']))
		self.assertFalse(core_functions.define_command(core_functions.process_speech("new shutdown computers")[0], ['reboot','computer']))



	##
	## @brief     Method to test sha244 function
	##
	def test_sha224(self):
		self.assertEqual(core_functions.sha224('Hello'), '4149da18aa8bfc2b1e382c6c26556d01a92c261b6436dad5e3be3fcc')
		self.assertNotEqual(core_functions.sha224('World'), '4149da18aa8bfc2b1e382c6c26556d01a92c261b6436dad5e3be3fcc')



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