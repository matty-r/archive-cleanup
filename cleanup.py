import os
import subprocess
from pathlib import Path

foldersWithRARs = subprocess.run('find -iname *.rar -execdir pwd \;', shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout.splitlines()
for folderPath in foldersWithRARs:
    rarPath = folderPath+"/*.rar"
    listContentsCommand = 'unrar lb "'+rarPath+'"'
    rarContents = subprocess.run(listContentsCommand, shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout.splitlines()
    shortestContentPath = ""
    for contentPath in rarContents:
        if len(contentPath) < len(shortestContentPath) or len(shortestContentPath) == 0:
            shortestContentPath = "/"+contentPath
    
    if len(shortestContentPath) > 0:
        fullContentPath = folderPath+shortestContentPath
        if os.path.exists(fullContentPath):
            deleteContentCommand = 'rm -rf "'+fullContentPath+'"'
            print(deleteContentCommand)
            # uncomment to actually delete it
            subprocess.run(deleteContentCommand, shell=True, stdout=subprocess.PIPE)
            if not os.path.exists(fullContentPath):
                print("deleted successfully!")
            else:
                print("not deleted")