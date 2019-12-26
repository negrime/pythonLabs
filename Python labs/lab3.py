import os
import sys


def removeEmptyDirectories(curPath):
    dir_list = os.listdir(curPath)
    if dir_list:
        for i in dir_list:
            dir = os.path.join(curPath, i)
            if os.path.isdir(dir):
                removeEmptyDirectories(dir)
        if not os.listdir(curPath):
            os.rmdir(curPath)
    else:
        os.rmdir(curPath)


try:
    if os.path.exists(sys.argv[1]):
        removeEmptyDirectories(sys.argv[1])
        print("Success!")
    else:
        raise NameError("The directory  does not exist!")
except NameError as e:
    print(e)
except Exception as e:
    print(e)
