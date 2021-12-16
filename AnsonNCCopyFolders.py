import os
from distutils.dir_util import copy_tree
import timeit


def copyFolder(src, dest, startsWith):
    folderArr = []
    for folder in os.listdir(src):
        folderArr.append(folder)
        folderArr.sort()

    arrLen = len(folderArr)

    for i in range(arrLen):
        srcTemp = src + "\\"+ str(folderArr[i])
        #print(srcTemp)
        for folder in os.listdir(srcTemp):
            if folder.startswith(startsWith):
                source = srcTemp + "\\" + folder
                #print(source)
                copy_tree(source, dest)

                    
def main():
    #start timer
    start = timeit.default_timer()

    #paths
    srcTeePath = "\\\\rodtest\\img\\index\\land\\grantee\\1749-july 1989"
    srcTorPath = "\\\\rodtest\\img\\index\\land\\grantor\\1749-july 1989"
    destTeePath = '\\\\rodtest\img\\index\\1749-1989_land\\tee\\0001\\'
    destTorPath = '\\\\rodtest\img\\index\\1749-1989_land\\tor\\0001\\'

    #copyFolder(srcTeePath, destTeePath, "000") #took 35.4 minutes (4785)
    #copyFolder(srcTorPath, destTorPath, "000") #took40.58 minutes (4841)
    #copying 9626 folders took 75.98 minutes or 1 hour and 15.98 minutes.

    # end timer
    stop = timeit.default_timer()
    print("Copying took " + str(round((stop - start) / 60,2)) + " minutes")


main()
