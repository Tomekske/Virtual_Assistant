#===============================================================================#
#Title           :Weather module                                                #
#Description     :Class to interface with the openweathermap API                #
#Author          :joostenstomek@gmail.com                                       #
#Date            :09/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import requests #http request libray
import configparser #parse data from a config file
import json
from ResponseHandler import Response
from ConfigHandler import Config


##
## @brief      Class to fetch weather data from the openweathermap API
##
class Weather(Config,Response):
    ##
    ## @brief      Constructor of the Weather class
    ## @param      location The location or country which you want to fetch weather data from    
    ## @param      file_location The config file location, default value is 'config.ini'    
    ##
    def __init__(self, location, file_location ="config.ini"):
        Config.__init__(self,'Openweathermap','API', file_location)
        self.api = self.content
        self.location = location
        self.url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(location,self.api)
        Response.__init__(self,self.url)
        self.query = self.json
        self.location_exsists = self.check_city(self.query)
        
        if self.location_exsists:
            self.temperature = self.query['main']['temp']
            self.temperature = self.query['main']['temp']
            self.min_temperature = self.query['main']['temp_min']
            self.humidity = self.query['main']['humidity']
            self.pressure = self.query['main']['pressure']
            self.description = self.query['weather'][0]['main']
            self.detailed = self.query['weather'][0]['description']
        else:
            self.temperature = 'CITY_ERROR'
            self.temperature = "CITY_ERROR"
            self.min_temperature = "CITY_ERROR"
            self.max_temperature = "CITY_ERROR"
            self.humidity = "CITY_ERROR"
            self.pressure = "CITY_ERROR"
            self.description = "CITY_ERROR"
            self.detailed = "CITY_ERROR"  



    ##
    ## @brief      Method to check a city's exsists
    ## @param      query  The raw query
    ## @return     if the city exsists return true else false
    ##
    def check_city(self, query):
        if (query['cod'] == '404') and (query['message'] == 'city not found'):
            return False
        return True