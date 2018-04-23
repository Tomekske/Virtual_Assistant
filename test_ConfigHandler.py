#===============================================================================#
#Title           :Unit test ResponseHandler                                     #
#Description     :Unit test to test Response class                              #
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
		self.f_valid = Config('Default', 'Default', self.file_valid) #valid object, file name does exsist
		self.f_invalid = Config('Default', 'Default', self.file_invalid) #invalid object, file name doesn't exsist



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
	## @brief      method to the config file option associated with a section
	##	
	def test_option(self):
		#created invalid objects
		f_invalid_2 = Config('Default', 'fdsfsdf', self.file_valid)
		f_invalid_3 = Config('fdgs', 'Default', self.file_invalid)
		f_invalid_4 = Config('fdgs', 'dfdsf', self.file_invalid)


		self.assertTrue(self.f_valid.option) #option exsists
		self.assertFalse(f_invalid_2.option) #option doesn't exsists
		self.assertFalse(f_invalid_3.option) #option doesn't exsists
		self.assertFalse(f_invalid_4.option) #option doesn't exsists



	##
	## @brief      method to test if the output of the content is valid or invalid
	##		
	def test_readContent(self):
		self.assertEqual(self.f_valid.content, 'Test') #Querry is invalid
		self.assertEqual(self.f_invalid.content, 'ERROR_CONTENT') #Querry is invalid



if __name__ == '__main__':
	unittest.main()