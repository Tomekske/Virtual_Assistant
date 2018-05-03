# Project #
### Title ###
	Virtual assistant
### Created by ###
	Joostens Tomek
### Description ###
	Voice controlled virtual assistant

# Setting up #
### 1. Download modules ###
	python blue.py -s
### 2. If downloading is finnished press any key to continue
### 3. Download all collections
### 4. When finnished exit the window

# Test if everything works fine #
### Option 1: Enter the following command in commandline ###
	test_blue.bat
### Option 2: Dubbel click on the test_blue.bat script ###

# Optionally: train words so recognizion will better understand your accent
### Run the following command
	python train_speech.py
### Option 1: Train a new word
#### 1. Enter the word you want to train
#### 2. Enter the amount of times you want to repeat the word

### Option 2: Train an exsisting word
#### 1. Enter the word you want to re-train
#### 2. Enter the amount of times you want to repeat the word

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
### 4. Exit script
	blue exit
### 5. Weather 
	blue what weather is it in {'city' or 'country'}
### 6. Open specific folder, currently only show, music, pictures and movie supported
	blue open {folder name}
### 7. Close all open folders
	blue close all folders
### 8. Shutdown computer
	blue shut-down computer, next say the super user's password {Amy}
### 9. Restart computer
	blue restart computer, next say the super user's password {Amy}