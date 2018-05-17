#===============================================================================#
#Title           :Unit test Weather                                             #
#Description     :Unit test to test Weather class                               #
#Author          :joostenstomek@gmail.com                                       #
#Date            :23/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import unittest
from Weather import Weather



##
## @brief      Class for test Weather class
##
class TestWeather(unittest.TestCase):
	##
	## @brief      setUp function to set up two weather objects
	##
	def setUp(self):
		self.weather_valid = Weather('Brussels','Config/config.ini') #valid object
		self.weather_invalid = Weather('Brussegfdgls','Config/config.ini') #Invalid object



	##
	## @brief      Method to test wether a location exsists or not
	##
	def test_location(self):
		self.assertTrue(self.weather_valid.location_exsists) #location exsists
		self.assertFalse(self.weather_invalid.location_exsists) #location doens't exsists



	##
	## @brief      Method to test to test data
	##
	def test_weather(self):
		self.assertNotEqual(self.weather_valid.temperature, 'CITY_ERROR') #Data is valid
		self.assertEqual(self.weather_invalid.temperature, 'CITY_ERROR') #Data is invalid
		
		self.assertNotEqual(self.weather_valid.description, 'CITY_ERROR') #Data is valid
		self.assertEqual(self.weather_invalid.description, 'CITY_ERROR') #Data is invalid


	
if __name__ == '__main__':
	unittest.main()