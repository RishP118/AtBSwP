
import shelve, pyperclip, sys, os
from pathlib import Path
mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	 if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		 pyperclip.copy(mcbShelf[sys.argv[1]])
	elif sys.argv[1].lower()== 'delete':
                for keys in list(mcbShelf.keys()):
                        del mcbShelf[keys]
elif len(sys.argv)==3 and sys.argv[1].lower()== 'delete':
        del mcbShelf[sys.argv[2]]

mcbShelf.close()
