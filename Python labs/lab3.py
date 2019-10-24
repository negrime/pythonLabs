import os
import sys


def removeEmptyDirectories(curPath):
    dir_list = os.listdir(curPath)
    if dir_list:
        for i in dir_list:
            if os.path.isdir(curPath + "\\" + i):
                removeEmptyDirectories(curPath + "\\" + i)
        if not os.listdir(curPath):
            os.rmdir(curPath)
    else:
        os.rmdir(curPath)


try:
    if os.path.exists(sys.argv[1]):
        removeEmptyDirectories(sys.argv[1])
        print("Success!")
    else:
        raise NameError("The directory is does not exist!")
except NameError as e:
    print(e)
except Exception as e:
    print(e)
