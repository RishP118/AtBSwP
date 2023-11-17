## 1. What is the difference between shutil.copy() and shutil.copytree()?

shutil.copy(): This will copy a single file from one path to another folder.

shutil.copytree(): This will copy an entire folder from one path to another folder.

## 2. What function is used to rename files?

shutil.move()

## 3. What is the difference between the delete functions in the send2trash and shutil modules?

delete of send2trash: This will help you to not permanently delete the file but sends it to the recycle bin.

delete of shutil: This will permanently delete the file.

## 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

zipfile.ZipFile()
