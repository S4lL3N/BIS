import os
from distutils.dir_util import copy_tree
import timeit
from PIL import Image
"""
Author:Shae Allen
Version: 1.0.0
date:12/15/21
Discription: 
    This script is for the Anson NC server restructure. They wanted to change the web
lookup for grantors and grantees from 1749-1989 to make it more user friendly. Requested that the
folder structure be based on names. The script needs the source folder path and the destination folder
path, then will copy folders, subfolders, and files from source to destination, Merge corperations and
civilians folders, rename the subfolders, rename the (images) files and rotate images that are in the
wrong orientation.   
"""

def copyFolder(src, dest, startsWith, logFile):
    start = timeit.default_timer()
    folderArr = []
    for folder in os.listdir(src):
        folderArr.append(folder)
        folderArr.sort()

    arrLen = len(folderArr)

    for i in range(arrLen):
        srcTemp = src + "\\"+ str(folderArr[i])
        for folder in os.listdir(srcTemp):
            if folder.startswith(startsWith):
                source = srcTemp + "\\" + folder
                copy_tree(source, dest)
    stop = timeit.default_timer()
    time = str(round((stop - start) / 60,2))
    print("Done copying " + str(arrLen) + " folders in " + time + " minutes.")
    logFile.write("Done copying " + str(arrLen) + " folders in " + time + " minutes.")
    
def renameSubfolders(path, logFile):
    start = timeit.default_timer()
    count = 0
    duplicates = 0
    for folder in os.listdir(path):
        count += 1
        orginalName = str(folder)
        temp = orginalName.split(" ")
        temp.pop(0)
        newName = " ".join(temp)
        original = path + "\\" + orginalName
        new = path + "\\" + newName
        try:
            os.rename(original, new)
        except FileExistsError:
            duplicates += 1
            print("\nError Duplicate Folder Found: " + str(folder))
            logFile.write("\nError Duplicate Folder Found: " + str(folder))
            new = path + "\\" + newName + "1"
            os.rename(original, new)
    stop = timeit.default_timer()
    time = str(round((stop - start) / 60,2))
    print("\nDone renaming "+ str(count) + " folders in " + time + " minutes, " + str(duplicates) + " Duplicates Found.")
    logFile.write("\n\n\nDone renaming "+ str(count) + " folders in " + time + " minutes, " + str(duplicates) + " Duplicates Found.") 
         
def renameImages(path, logFile):
    start = timeit.default_timer()
    totalImages = 0
    #array of subfolders
    subfolders = os.listdir(path)
    for folder in subfolders:
        #array of files in directory
        files = os.listdir(path+"\\"+str(folder))
        #starting number for new file name
        count = 1
        #prefix for new file name
        prefix = "00000"
        for file in files:
            totalImages += 1
            if count > 9:
                prefix = "0000"
            if count > 99:
                prefix = "000"
            if count > 999:
                prefix = "00"
            if count > 9999:
                prefix = "0"

            original = path + "\\" + str(folder) + "\\" + str(file)
            new = path + "\\" + str(folder) + "\\" + prefix + str(count) + ".tif"
            os.rename(original, new)
            count += 1
    stop = timeit.default_timer()
    time = str(round((stop - start) / 60,2))
    print("Done renaming "+ str(totalImages) +" files in " + time + " minutes.")
    logFile.write("\nDone renaming "+ str(totalImages) +" files in " + time + " minutes.")

def rotateImage(path, logFile):
    start = timeit.default_timer()
    count = 0
    subfolders = os.listdir(path)
    for folder in subfolders:
        #array of files in directory
        files = os.listdir(path+"\\"+str(folder))
        for file in files:
            pathToFile = path + "\\" + str(folder) + "\\" + str(file)
            img = Image.open(pathToFile)
            width, height = img.size
            if (height > width):
                count += 1
                rotated = img.transpose(Image.ROTATE_270)
                rotated.save(pathToFile)
                print("Rotated # " + str(count) +": " + str(pathToFile))
                logFile.write("Rotated: " + str(pathToFile))
    stop = timeit.default_timer()
    time = str(round((stop - start) / 60,2))
    print("Done rotating "+ str(count) +" images in " + time + " minutes.")
    logFile.write("\nDone rotating "+ str(count) +" images in " + time + " minutes.")
    
def main():
    #start timer
    start = timeit.default_timer()

    #log file
    logfile = open("AnsonNCRestructureLog.txt","w+")

    #paths
    srcTeePath = "\\\\rodtest\\img\\index\\land\\grantee\\1749-july 1989"
    srcTorPath = "\\\\rodtest\\img\\index\\land\\grantor\\1749-july 1989"
    destTeePath = '\\\\rodtest\\img\\index\\1749-1989_land\\tee\\0001\\'
    destTorPath = '\\\\rodtest\\img\\index\\1749-1989_land\\tor\\0001\\' 

    fileStartWith = "000"

    copyFolder(srcTeePath, destTeePath, fileStartWith, logfile) 
    # Notes -- Copying 4785 folders in 35.4 minutes.
    copyFolder(srcTorPath, destTorPath, fileStartWith, logfile) 
    # Notes -- Copying 4841 folders in 40.58 minutes.
    # Notes -- Total copying 9626 folders in 75.98 minutes.(Both tee & tor)
    renameSubfolders(destTeePath, logfile)
    # Notes -- renamed 4785 folders in 1.0 minutes, 5 Duplicates Found.
    renameSubfolders(destTorPath, logfile)
    # Notes -- renamed 4841 folders in 1.09 minutes, 12 Duplicates Found.
    renameImages(destTeePath, logfile)
    # Notes -- renamed 13391 files in 3.81 minutes.
    renameImages(destTorPath, logfile)
    # Notes -- renamed 14169 files in 3.56 minutes.
    rotateImage(destTeePath, logfile)
    # Notes -- rotated 1 images in 7.63 minutes.
    rotateImage(destTorPath, logfile)
    # Notes -- rotated 47 images in 8.71 minutes.

    # end timer
    stop = timeit.default_timer()
    print("\nScript ran in " + str(round((stop - start) / 60,2)) + " minutes")
    logfile.write("\n\n\nScript ran in " + str(round((stop - start) / 60,2)) + " minutes")

    logfile.close()

if __name__ == "__main__":
    main()
