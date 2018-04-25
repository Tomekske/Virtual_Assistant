#===============================================================================#
#Title           :Unit test ConfigHandler                                       #
#Description     :Unit test to test Config class                                #
#Author          :joostenstomek@gmail.com                                       #
#Date            :20/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import unittest
from ConfigHandler import Config



##
## @brief      Class for test core functions.
##
class TestConfigHandler(unittest.TestCase):
	##
	## @brief      method to setup some basic stuff
	##	
	def setUp(self):
		#Variables with config file names
		self.file_valid = 'config.ini'
		self.file_invalid = 'configfdfsf.ini'

		#Created Conif() objects
		self.f_valid = Config(self.file_valid) #valid object, file name does exsist
		self.f_invalid = Config(self.file_invalid) #invalid object, file name doesn't exsist



	##
	## @brief      method to test if file exsist
	##	
	def test_fileExistence(self):
		self.assertTrue(self.f_valid.exsist) #file exsist
		self.assertFalse(self.f_invalid.exsist) #file does not exsist



	##
	## @brief      method to test if the file-objext exsist
	##	
	def test_fileObject(self):
		self.assertTrue(self.f_valid.file) #file object exsist
		self.assertFalse(self.f_invalid.file) #file objext does not exsist



	##
	## @brief      method to test if the output of the content is valid or invalid
	##		
	def test_readContent(self):
		self.assertEqual(self.f_valid.readData('Default','Default'), 'Test') #Querry is invalid
		self.assertEqual(self.f_invalid.readData('Default','Defagfult'),'ERROR_DATA') #Querry is invalid



	##
	## @brief      Method to test if section exsists or not
	##
	def test_section(self):
		self.assertTrue(self.f_valid.checkSection('Default')) #sections exsists
		self.assertFalse(self.f_valid.checkSection('Deffsdault')) #section does not exsist



if __name__ == '__main__':
	unittest.main()