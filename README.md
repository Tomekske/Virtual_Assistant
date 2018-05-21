# Project
### Title
	Virtual assistant
### Created by
	Joostens Tomek
### Description
	Voice controlled virtual assistant
### Version
	1.0.18

# Setup
### 1. Setup
	python setup.py install
### 2. Configure
	python blue.py -c
### 3. Install the AVbin-10-win64.exe in the browser
### 4. Install github if necessary
### 5. Download all NLTK collections
### 6. When finnished exit the window


# Test
	python blue.py -t


# Optionally: train words so recognizion will better understand your accent
### Run the following command
	python blue.py -l
### Option 1: Train a new word
#### 1. Enter the word you want to train
#### 2. Enter the amount of times you want to repeat the word

### Option 2: Train an exsisting word
#### 1. Enter the word you want to re-train
#### 2. Enter the amount of times you want to repeat the word

### Option 3: Synonyms
#### 1. Enter new synonym
#### 2. Add synonym to exsisting word


# Updating modules
	python blue.py -u

# Config file
### Change the absolute path for the next folders Serie, Music, Pictures and Movie supported


# Run virtual assistant
	python blue.py


# Commands
### 1. Every speech command starts with the assistant's name 'blue'
### 2. Time
	blue what time is it
### 3. Exit script
	blue exit
### 4. Set password
	blue set password
### 5. Test if password is correct
	blue test password
### 6. Weather 
	blue what weather is it in {'city' or 'country'}
### 7. Open specific folder, currently only show, music, pictures and movie supported
	blue open {folder name}
### 8. Close all open folders
	blue close all folders
### 9. Shutdown computer
	blue shut-down computer, next say the super user's password {Amy}
### 10. Restart computer
	blue restart computer, next say the super user's password {Amy}