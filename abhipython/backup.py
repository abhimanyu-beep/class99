import os
import shutil
source=input("Enter the source folder name")
destination=input("Enter the destination folder name")
source=source+"/"
destination=destination+"/"
listoffile=os.listdir(source)
for file in listoffile:
    shutil.move((source+file),destination)
