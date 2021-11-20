# CL_template
A script for generating a cover letter pdf for any recipient.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project uses both a Bash, Python, and Latex to generate a pdf of a letter. The Python script, make_letter.py, prompts the user for the recipient of their 
letter, and writes the contents of the letter to my_letter.tex which is imported into a generalized template cover_letter_template.tex. The bash script, build.sh,
calls the Python script and compiles the contents of cover_letter_template.tex into a pdf.

## Technologies
Project is created with:
* Bash version 5.1.0(1)
* Python version 3.9
* Tex Live version 2020
	
## Setup
To run this project, complete the following steps. 
### Install Dependancies
These instructions have been tested on Fedora Workstation 34.
1. Install Tex Live full.
```
$ yum install texlive-scheme-full
```
2. Install Python 3.9
```
$ sudo dnf install python3.9
```
### Complete and Run the Bash Script
1. Change the string on line 10 on make_letter.py to the file path of my_letter.tex.
2. Enagle executable permission on make_letter.py and build.sh.
```
chmod +x build.sh make_letter.py
```
3. Build the letter pdf by changing to the directory CL_template. Then run the following command. The following command with prompt for the
name of your desired letter recipient.
```
./build.sh
```
