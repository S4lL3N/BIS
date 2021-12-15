import shutil
import os
from PIL import Image
import timeit

'''
Author: Shae Allen
Date: 12/14/21
version: 1.0.0

Script Discription:
Anson county request to restructure the file system.
script takes folder and source and destination paths, copys files
and renames to our naming convention. along with rotating
any file that is in the wrong orintation. 
'''
#start timer
start = timeit.default_timer()

#source and dest folder / paths
dir = r"C:\Users\Shae.Allen\Desktop\Testing"
sourceFolderPath = "C:\\Users\\Shae.Allen\\Desktop\\Testing\\"
destFolderPath = "C:\\Users\\Shae.Allen\\Desktop\\TestingDone\\"

print("\n\nCopying files... \n\nSource Folder = " + sourceFolderPath + "\nDestination Folder = " + destFolderPath)

#starting number for file name
count = 1

#prefix for file name
prefix = "00000"

#loop through all files in folder.
#copy and rename file.
for filename in os.listdir(dir):
    if filename.endswith(".tif") or filename.endswith(".png"): 
        src = sourceFolderPath + str(filename)
        # for rotated images
        # if the image is rotated vert, it rotates back to hori.
        img = Image.open(src)
        width, height = img.size
        if (height > width):
            rotated = img.transpose(Image.ROTATE_270)
            rotated.save(sourceFolderPath + str(filename))

        if count > 9:
            prefix = "0000"
        if count > 99:
            prefix = "000"
        if count > 999:
            prefix = "00"
        if count > 9999:
            prefix = "0"

        dest = destFolderPath + prefix + str(count) + ".tif"

        shutil.copy(src, dest)
        count += 1
        continue
    else:
        continue
    
# end timer
stop = timeit.default_timer()
print("\n\nCopyied over " + str(count) + " files in " + str(round(stop - start, 2)) + " seconds\n\n")
