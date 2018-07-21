from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from .models import Document


def index(request):

    return render(request, 'local/home.html')

def contact(request):
    return render(request, 'local/contact.html')

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'local/uploaded.html')
        #return render(request, 'local/upload.html', {
        #    'uploaded_file_url': uploaded_file_url
        #})
    return HttpResponse('File not uploaded!')
