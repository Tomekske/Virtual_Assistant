#===============================================================================#
#Title           :Response handler                                              #
#Description     :Class to to obtain a JSON response from a server              #
#Author          :joostenstomek@gmail.com                                       #
#Date            :20/04/2018                                                    #
#Version         :1.0.0                                                         #
#Usage           :Python                                                        #
#Python version  :3.6                                                           #
#===============================================================================#



import requests #http request libray
import json
import httplib2



##
## @brief      Class to to obtain a JSON response from a server 
##
class Response():
	##
	## @brief      Constructor of the Response class
	## @param      url The url to the website you want to get a JSON response from    
	##
	def __init__(self, url):
		self.status = self.status(url)
		self.json = self.query(url,self.status)



	##
	## @brief      Function to test if given URL is valid
	## @param      url The URL you want to test
	##
	def status(self,url):
		#Test URL, if it exsist return true else return false
		try:
			h = httplib2.Http()
			resp = h.request(url, 'HEAD') 
			return True
		except:
			return False



	##
	## @brief      request to the server
	## @param      url The URL you want to fetch data from
	## @param      status The status code which is tested in te status function
	## @return     JSON response or error message
	##  
	def query(self,url,status):
		#if URL exsist get data from the server and return it. Else return error string
		if status == True:
			raw = requests.get(url)
			decodeRaw = raw.content.decode("utf-8") #get content from webpage and decode bytes,replace "" with `` and convert them to a string
			jsonData = json.loads(decodeRaw) #convert JSON string to a JSON object
			return jsonData
		return 'RAW_QUERY_ERROR'

	def removeOption(self, section, option):
		print(section, option)
