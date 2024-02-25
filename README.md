# Project
Here is my personal project aimed at making backups very simply and quickly in Python.

# How it works
This project uses txt files to save profiles. Here is an example of a profile. A profile aims to have all the necessary data for the program to function. The program can work without loading a profile, it will just be necessary to change the corresponding variables in the Python script.

Example of config file:
> C:/Users/USER_NAME/Documents/to backup
> D:/Users/USER_NAME/Documents/back-up folder
> C:/Users/USER_NAME/Documents/logs
> 1
> 0

The first line indicates the source folder that will be backed up, the second one indicates the backup location, and the third one indicates where the program logs are saved if there are any. The fourth line indicates whether logs are being made (0 = false, 1 = true), and the last one indicates if the program should delete files that are present in the backup folder but not in the source folder.


# How to use it
## Without a config file
You need to have Python installed on the machine.
You need to modify the variables:
- src_dir: represents the source file to be backed up.
- sync_dir: the location to backup files.
- logs_dir: the location where logs are saved in case there are any.
- log: (True or False) defines whether the program creates logs.
- delete_file: (True or False) defines if the program has the right to delete files if they are not present in the source file.ce

## With a config fileg
1) Have Python installed on the machine.
2) Create a text file named after the config you want: e.g., "config1.txt".
3) Modify the config file:
4) To run this program with the config file, open the Windows or Linux terminal.
5) Execute the program with the name of the config as an argument, e.g., "python main.py config1".



# Limitations
For optimization purposes, to check if a file has been modified, it checks the date of the last modification. This can cause problems if the files in the backup folder have been modified after those present in the source folder. This program has only been tested on Linux and Windows. This program may contain errors or bugs; if you notice any, please report them.

# License 
You are free to use or modify the program as you wish.
