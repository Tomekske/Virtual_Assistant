pip install configparser
pip install SpeechRecognition
pip install PyAudio
pip install colorama
pip install arrow
pip install nltk
pip install numpy
pip install requests
pip install httplib2
git clone https://github.com/Tomekske/Module_Weather
git clone https://github.com/Tomekske/Module_ConfigHandler
git clone https://github.com/Tomekske/Module_ResponseHandler

cd Module_Weather
move Weather.py ../Weather.py
move test_Weather.py ../test_Weather.py
cd ..
RD /S /Q Module_Weather

cd Module_ConfigHandler
move ConfigHandler.py ../ConfigHandler.py
move test_ConfigHandler.py ../test_ConfigHandler.py
cd ..
RD /S /Q Module_ConfigHandler

cd Module_ResponseHandler
move ResponseHandler.py ../ResponseHandler.py
move test_ResponseHandler.py ../test_ResponseHandler.py
cd ..
RD /S /Q Module_ResponseHandler

