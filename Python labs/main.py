def is_digit( string):
    try:
        int(string)
        return True
    except BaseException:
        return False


result = None
isFirst = True
isAlone = False

line = input("Input numbers sequence. For input finish \".\"\n")

while line != '.' or not isAlone:
    if not isAlone and line == '.':
        line = input("Input at least one number")
        continue
    else:
        isAlone = True
    if is_digit(line):
        num = int(line)
        if num < 0:
            if isFirst:
                isFirst = False
                result = num
            if num > result:
                result = num
    else:
        print("Wrong value! Please input only digits!")
    line = input()

print("Sequence does not have any negative numbers") if not result else print(result)
