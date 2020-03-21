from django.shortcuts import render
from  django.http import HttpResponse
from app1.models import Topic, People,Date
def ola(request):
    ord=Date.objects.order_by('date')
    return render(request,'html.html',{"cho":ord})

# Create your views here.
