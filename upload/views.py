from django.shortcuts import render
from dataset.forms import upload as up
import os
# Create your views here.
def getFilesNames():
    filesNames = []
    for file in os.listdir(".\static"):
        if file.endswith(".csv"):
            filesNames.append(file)
    return filesNames

def upload(request):
    form = up()
    context = {"data": getFilesNames(),'form':form}
    return render(request, 'upload.html',context)