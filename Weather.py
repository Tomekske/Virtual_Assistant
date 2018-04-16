#===============================================================================#
#Title           :Weather module                                                #
#Description     :Class to interface with the openweathermap API                #
#Author          :joostenstomek@gmail.com                                       #
#Date            :09/04/2018                                                    #
#Version         :1.0                                                           #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import requests #http request libray
import configparser #parse data from a config file
import json



##
## @brief      Class to fetch weather data from the openweathermap API
##
class Weather(object):
    ##
    ## @brief      Constructor of the Weather class
    ## @param      location The location or country which you want to fetch weather data from    
    ## @param      file_location The config file location, default value is 'config.ini'    
    ##
    def __init__(self, location, file_location ="config.ini"):
        self.API = self.API(file_location)
        self.location = location 
        self.rawQuerry = self.querry()

        #check if there isn't an error in rawQuerry
        if not self.rawQuerry == "RAW_QUERRY_ERROR":
            self.temperature = self.rawQuerry['main']['temp']
            self.min_temperature = self.rawQuerry['main']['temp_min']
            self.max_temperature = self.rawQuerry['main']['temp_max']
            self.humidity = self.rawQuerry['main']['humidity']
            self.pressure = self.rawQuerry['main']['pressure']
            self.description = self.rawQuerry['weather'][0]['main']
            self.detailed = self.rawQuerry['weather'][0]['description']
        else:
            self.temperature = "Error"
            self.min_temperature = "Error"
            self.max_temperature = "Error"
            self.humidity = "Error"
            self.pressure = "Error"
            self.description = "Error"
            self.detailed = "Error"            



    ##
    ## @brief      Get the API key from a config file 
    ## @param      file_location  The config file location
    ## @return     API key or error message
    ##
    def API(self,file_location):
        config = configparser.ConfigParser() #creates an object of the configparser class
        try:
            config.read(file_location) #reads config file content
            api = config['Openweathermap']['API'] #Get the value of a section from the config file
            return api
        except:
            return "API_KEY_ERROR"



    ##
    ## @brief      request to openweathermap server
    ## @return     JSON response or error message
    ##
    def querry(self):
            
        #check if API is not a error
        if not self.API == "API_KEY_ERROR":
            try:
                request = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric".format(self.location,self.API) #API URL
                raw = requests.get(request)
                decodeRaw = raw.content.decode("utf-8") #get content from webpage and decode bytes,replace "" with `` and convert them to a string
                jsonData = json.loads(decodeRaw) #convert JSON string to a JSON object
                return jsonData
            except:
                return "RAW_QUERRY_ERROR"
        else:
            return "RAW_QUERRY_ERROR"