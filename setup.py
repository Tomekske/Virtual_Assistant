from setuptools import setup

setup(
	name='Virtual assistant',
	author='Tomek Joostens',
	author_email='joostenstomek@gmail.com',
	url='https://github.com/Tomekske/Virtual_Assistant',
	version='1.0.17',
	py_modules=['blue'],
	install_requires=['requests','httplib2'],
	packages=['Modules']
)