from django.http import HttpResponse
from django.shortcuts import render,redirect
from dataset.forms import upload
from upload.views import getFilesNames

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def csvData(request):
    form = upload()
    if request.method == "POST":
        form = upload(request.POST,request.FILES)
        print('Postrequest')
        if form.is_valid():
            print('true')
            handle_uploaded_file(request.FILES['file'],request.POST['name'])
            return Response(status=200,data={'success':True})
        else:
            print('false')
            form = upload()
            return Response(status=403,data={'success':False})
    elif request.method == "GET":
        return Response(status=200,data = {'data':getFilesNames()})

def formsubmission(request):
    form = upload()
    if request.method == "POST":
        form = upload(request.POST,request.FILES)
        if form.is_valid():
            print('true')
            handle_uploaded_file(request.FILES['file'],request.POST['name'])
            return redirect('/upload')
        else:
            print('false')
            form = upload()
            return redirect('/upload')
    if request.method == "GET":
        return render(request,'display.html',{'form':form})

def handle_uploaded_file(f,fileName):
    with open('static/' + fileName+'.csv','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)