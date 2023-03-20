from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def members(request):
    return HttpResponse("hello")

def home(request):
    return render(request,'todos/index.html',{ 'name' : 'karthic'})

def test(request):
    return render(request, 'todos/test.html')

def main(request):
    return render(request, 'todos/main.html')