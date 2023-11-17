import os, re, shutil
p=int("Source folder: ")
s=os.path.join(p,'newfolder')
ext=input("Enter file extension: ")
try:
	for foldername,subfolders,filenames in os.walk(p):
		for filename in filenames:
			if filename.endswith(ext):
				t=os.path.exists(s)
                		if t==True:
                    			shutil.copy( os.path.join(foldername,filename),s)
                		else:
                    			os.makedirs(s)
                    			shutil.copy( os.path.join(foldername,filename),s)
