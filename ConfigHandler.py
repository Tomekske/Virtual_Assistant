#===============================================================================#
#Title           :Response handler                                              #
#Description     :Class to interface easily with config files                   #
#Author          :joostenstomek@gmail.com                                       #
#Date            :20/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import configparser
import os



##
## @brief      Class to interface easily with config files
##
class Config():
	##
    ## @brief      Constructor of the Config class
    ## @param      section Section from the config file    
    ## @param      option Option associated with section
    ## @param      file_location the location of the config file [default = config.ini]  
    ##
	def __init__(self, section, option, file_location = 'config.ini'):
		self.exsist = self.fileExistence(file_location)
		self.file = self.fileObject(file_location)
		self.option = self.optionExistence(section, option)
		self.content = self.readContent(section, option)



	##
    ## @brief      Check if the file exsist
    ##	
	def fileExistence(self, file_location):
		return os.path.isfile(file_location)



	##
    ## @brief      Create a file object
    ##	
	def fileObject(self, file_location):
		#if the config file exsist create a file object, else return False
		if self.exsist:
			file = configparser.ConfigParser()
			file.read(file_location)
			return file
		return False

      

	##
    ## @brief      Check if the option associated with a given section exsist
    ##	
	def optionExistence(self, section, option):
		#Only check option exsistence if the config file exsists, else return False
		if self.file:
			return self.file.has_option(section,option)
		return False



	##
    ## @brief      Read the content from the config file
    ##		
	def readContent(self, section, option):
		#Only read the content from the config file when the option is valid and if the file-object exsists, else return error message
		if self.option and self.file:
			return self.file[section][option]
		return 'ERROR_CONTENT'