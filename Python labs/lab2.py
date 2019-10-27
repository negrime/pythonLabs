import re


def canOpen(name):
    try:
        open(name)
        return True
    except IOError as e:
        print(e)
        return False


fileName = input("Input file name\n")
while not canOpen(fileName):
    fileName = input("Input file name\n")

file = open(fileName, 'r')

text = file.read()
text = re.sub("[' ']{2,}", ' ', text)
file.close()

file = open(fileName, 'w')
file.writelines(text)
file.close()
