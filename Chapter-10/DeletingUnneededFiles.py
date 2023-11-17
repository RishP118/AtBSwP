import os, re, shutil
from pathlib import Path
for folderName,subfolders,filenames in os.walk(os.getcwd()):
    for filename in filenames:
        a= os.path.getsize(os.path.join(folderName,filename))
        if a>1048576:
            print("The size of ",filename, "is ",a//1048576,"MB")
