# importing the necessary libraries
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import subprocess


def initial(request):
    if request.method == 'GET':
        return render(request, 'initial.html')

    if request.method == 'POST':
        text = request.POST["text"]
        x1 = request.POST["x1"]
        y1 = request.POST["y1"]
        x2 = request.POST["x2"]
        y2 = request.POST["y2"]
        x3 = request.POST["x3"]
        y3 = request.POST["y3"]
        print(text, " ", x1, "\n")
        print(text, " ", y1, "\n")

        dict = {
            'text': text,
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'x3': x3,
            'y3': y3
        }
        #p = subprocess.Popen("C:\\Users\\ainam\\Desktop\\UPF 3R\\TALLER MUSICAL\\hello\\dist\\main.exe")
        p = subprocess.Popen(["notepad.exe", "documento.txt"])
    return render(request, 'initial.html', dict)
