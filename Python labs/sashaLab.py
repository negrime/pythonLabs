import sys
import os
import shutil
from datetime import datetime, timedelta

firstDir = sys.argv[1]
secondDir = sys.argv[2]
try:
    os.mkdir(os.path.join(secondDir, "Last Day"))
    os.mkdir(os.path.join(secondDir, "Last Week"))
    os.mkdir(os.path.join(secondDir, "Last Month"))
except OSError:
    print("Ошибка!")

now = datetime.now()

for fileName in os.listdir(firstDir):
    yesterday = now - timedelta(days=1)
    thisWeek = now - timedelta(weeks=1)
    first = now.replace(day=1)
    thisMonth = first - timedelta(days=1)
    thisMonth = thisMonth.replace(day=now.day)
    creationTime = datetime.fromtimestamp(os.path.getmtime(os.path.join(firstDir, fileName)))
    if creationTime > yesterday:
        shutil.copy(os.path.join(firstDir, fileName), os.path.join(secondDir, "Last Day"))
    elif creationTime > thisWeek:
        shutil.copy(os.path.join(firstDir, fileName), os.path.join(secondDir, "Last Week"))
    elif creationTime > thisMonth:
        shutil.copy(os.path.join(firstDir, fileName), os.path.join(secondDir, "Last Month"))

print("Успех!")

