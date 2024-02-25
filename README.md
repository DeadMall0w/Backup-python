# Projet
Voici, mon projet personnel qui a pour but de faire des backups tres simplements et rapidement en python.

# Comment ca fonctionne 
Ce projet utilise des fichiers txt pour sauvegarder des profiles
Voici l'exemple d'un profile. Un profile a pour but d'avoir toutes les données necessaire pour le fonctionnement du programme. Le programme peut fonctionner sans charger de profile, il suffira juste de changer les variables correspondantes dans le script python.

Exemple de fichier config :
> C:/Users/USER_NAME/Documents/to backup
> D:/Users/USER_NAME/Documents/back-up folder
> C:/Users/USER_NAME/Documents/logs
> 1
> 0

La premiere ligne indique le dossier source qui va etre sauvegardé, le second l'emplacement de la sauvegarde et la troisieme la ou sont enregitrer les logs du programme s'il y en a.
La quatrieme ligne indique s'il y a des logs qui sont fait (0 = false, 1 = True)
Et la derniere indique si le programme doit supprimer les fichiers qui sont présent dans le dossier de sauvegarde mais pas présent dans le dossier source.


# Comment l'utiliser 
## Sans fichier config
Il faut avoir python d'insallé sur la machine.
Il faut modifier les variables :
- src_dir : represant le fichier source qui va être sauvegardé.
- sync_dir : l'emplacement de sauvegarde des fichiers.
- logs_dir : l'emplacement ou sont sauvegardé les logs dans le cas où il y en a.
- log : (True ou False) définit le progamme creer des logs.
- delete_file : (True ou False) définit si le programme a droit de supprimer des fichiers dans le cas où ils ne sont pas présent dans le fichier source

## Avec un fichier conig
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
