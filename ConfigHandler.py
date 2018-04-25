#===============================================================================#
#Title           :Config handler                                                #
#Description     :Class to interface easily with config files                   #
#Author          :joostenstomek@gmail.com                                       #
#Date            :24/04/2018                                                    #
#Version         :1.0.1                                                         #
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
	## @param      file_location the location of the config file [default = config.ini]  
	##
	def __init__(self, file_location = 'config.ini'):
		self.location = file_location
		self.exsist = self.fileExistence(file_location)
		self.file = self.fileObject(file_location)



	##
	## @brief      Check if the file exsist
	## @return     Return True or false wether file exsists
	##	
	def fileExistence(self, file_location):
		return os.path.isfile(file_location)



	##
	## @brief      Create a file object
	## @return     Return file object or False
	##	
	def fileObject(self, file_location):
		#if the config file exsist create a file object, else return False
		if self.exsist:
			file = configparser.ConfigParser()
			file.read(file_location)
			return file
		return False

      

	##
	## @brief      Read the data from the config file
	## @return     Return boolean 
	##		
	def readData(self, section, option):
		#Only read the data from the config file when the option is valid and if the file-object exsists, else return error message
		try:
			return self.file[section][option]
		except:
			return 'ERROR_DATA'



	##
	## @brief      Method to check wether a section exsists or not
	## @param      section  The section you want to test
	## @return     Return boolean 
	##
	def checkSection(self, section):
		if section in self.file.sections():
			return True
		else:
			return False



	##
	## @brief      Writes a data to config file
	## @param      section  The new or exsisting section
	## @param      option   The option of a section
	## @param      data     The data you want to write to the file
	## @return     Boolean wehter 
	##
	def writeData(self, section, option, data):
		print(self.file.sections())
		check = self.checkSection(section)

		save = open(self.location,'w')
		
		if not check:
			self.file.add_section(section) #Add section
			self.file.set(section, option, data) #Add option according to section
			self.file.write(save) #Write data to to the [section][option]
			save.close() #close file
		else:
			self.file.set(section, option, data) #Add option according to section
			self.file.write(save) #Write data to to the [section][option]
			save.close() #close file