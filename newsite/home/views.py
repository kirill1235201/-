from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'papka/main.html'  )
def about(request):
    return render(request,'papka/about.html')
def contact(request):
    return render(request,'papka/contact.html')
def random(request):
    return render(request,'papka/random.html')