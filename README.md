# combineX | Merge all CSVs from Single Directory 

You can download the program here: https://github.com/ByronAllen/combineX. See the green clone or download button. Click and select download ZIP. This will be the easiest route for now. Once you’ve unzipped in your Desktop go to your Terminal (command + space bar) then type Terminal. From there do the following:

cd ~/Desktop/combineX # Moving you into the combineX directory 
mkdir data # This creates a folder called ‘data’, and your CSVs here 
mkdir output # This creates a folder called ‘output’ 
brew install pip # This may break if you do not have brew, but many Macs have it by default 
pip install pandas # The combineX program requires this 
python run.py # Follow the prompts 

All your CSVs have to be the same length and have to have a column that you designate. 


### Detailed Instructions

PREREQ
Command + Space bar + type 'Terminal' 
Execute commands 
	- sudo easy_install pip
	- sudo pip install -U pip
	- sudo pip install pandas

DOWNLOAD combineX
Go to https://github.com/ByronAllen/combineX
Click on the 'Clone or Download' button >> select download zip option
Move zip to Desktop
Unzip

DATA FOLDER
Create new folder (aka project folder) in combineX to store data (e.g. move data folder into combineX)
Remove spaces from the folder name
Create output folder in project folder

RUN PROGRAM
Command + Space bar + type 'Terminal' 
Execute commands 
	- cd ~/Desktop/combineX-master/
 	- python run.py
		- Enter the path to your data folder (path to project folder would be './project')
		- Name the path to the output folder (e.g. './project/output')
		- Create a file name
		- Pick which column to combine
