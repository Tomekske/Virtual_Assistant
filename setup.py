from setuptools import setup

setup(
	name='Virtual assistant',
	author='Tomek Joostens',
	author_email='joostenstomek@gmail.com',
	url='https://github.com/Tomekske/Virtual_Assistant',
	version='1.0.18',
	py_modules=['blue'],
	install_requires=['requests',
					  'httplib2',
					  'SpeechRecognition',
					  'PyAudio',
					  'colorama',
					  'arrow',
					  'nltk',
					  'numpy',
					  'pyglet',
					  'gtts'],
	packages=['Modules/',
			  'Modules/Accent/',
			  'Modules/ConfigHandler/',
			  'Modules/ResponseHandler/',
			  'Modules/Core/',
			  'Modules/Weather/']
)