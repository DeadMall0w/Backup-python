import sys
import shutil
import os
# total arguments
if(len(sys.argv) <= 1):
    print("Please give the location of the settings file !")
    print("Exiting...")
    exit()

syncedFolders = []
destination = ""

# Arguments passed
settings_file = sys.argv[1]
print("Loading file : ", settings_file)

f_firstLine = 1
try:
    # Open the file and read its content.
    with open(settings_file) as f:
        content = f.readlines()

    # Display the file's content line by line.
    for line in content:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        if f_firstLine == 1:
            f_firstLine = 0
            destination = line
            print("destination :" + destination)
        else:
            syncedFolders.append(line)
            print("source : " + line)

except:
    print("Could't read file !")
    print("exiting...")
    exit()

for folder in syncedFolders:
    print("Copying folder : " + folder)
    folder_name = os.path.basename(folder.strip())  # nom du dossier source
    dest_path = os.path.join(destination, folder_name)

    try:
        shutil.copytree(folder.strip(), dest_path, dirs_exist_ok=True)
        print(f"Copied {folder} -> {dest_path}")
    except Exception as e:
        print(f"Error copying {folder}: {e}")



print("All folder copied ! ")
print("Exiting...")