from django.shortcuts import render

# Create your views here.
files = [
    "Data file 01",
    "Data file 02",
    "Data file 03",
    "Data file 04",
    "Data file 05",
]
def upload(request):
    context = {"data": files}
    return render(request, 'upload.html',context)