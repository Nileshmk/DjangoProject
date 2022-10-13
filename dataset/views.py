from django.http import HttpResponse
from django.shortcuts import render,redirect
from dataset.forms import upload
# Create your views here.
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
    return render(request,'display.html',{'form':form})

def handle_uploaded_file(f,fileName):
    with open('static/' + fileName+'.csv','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)