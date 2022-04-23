from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def display_bank(request):
    return render(request, 'bank.html')