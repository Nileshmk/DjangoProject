import os
from webbrowser import get

def getFilesNames():
    filesNames = []
    for file in os.listdir(".\static"):
        if file.endswith(".csv"):
            filesNames.append(file)
    return filesNames
print(getFilesNames())