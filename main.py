import sys
import shutil
import os

if len(sys.argv) <= 1:
    print("Please provide the location of the settings file!")
    print("Exiting...")
    exit()

synced_folders = []
destination = ""

# Read the settings file
settings_file = sys.argv[1]
print("Loading settings from:", settings_file)

first_line = True
try:
    with open(settings_file) as f:
        for raw_line in f:
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            if first_line:
                destination = line
                print("Destination:", destination)
                first_line = False
            else:
                # Split by the last space if label is present
                if ' ' in line:
                    parts = line.rsplit(' ', 1)
                    source_path = parts[0].strip()
                    target_name = parts[1].strip()
                else:
                    source_path = line
                    target_name = os.path.basename(source_path.strip())

                synced_folders.append((source_path, target_name))
                print(f"Source: {source_path} -> will be copied to: {target_name}")

except Exception as e:
    print(f"Couldn't read the file: {e}")
    print("Exiting...")
    exit()

# Copy folders
for source_path, target_name in synced_folders:
    dest_path = os.path.join(destination, target_name)
    try:
        shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
        print(f"Copied {source_path} -> {dest_path}")
    except Exception as e:
        print(f"Error copying {source_path} -> {dest_path}: {e}")

print("All folders copied!")
print("Exiting...")
