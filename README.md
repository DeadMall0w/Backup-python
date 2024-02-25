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
1) Avoir python d'installé sur la machine.
2) Creer un fichier texte portant le nom de la config que vous voulez : ex "config1.txt"
3) Modifier le fichier config :


4) Pour executer ce programme avec le fichier config, ouvrez le terminale windows, ou linux.
5) Executer le programme avec comme un argument le nom de la config ex : "python main.py config1"



# Limitation
Par souci d'optimisation, pour regarder si un fichier a été modifié, il regarde la date de la derniere modification. Ce qui peut causer des problemes si les fichiers dans le dossier de back-up ont été modifié apres ceux présent dans le dossier source.
Ce programme a été uniquement testé sur linux et windows.
Ce programme comporte peux etre des erreurs ou des bugs, si vous en voyez n'hesitez pas a le signaler.


# Licence 
Vous êtes libre d'utiliser ou modifier le programme comme vous le voulez.
