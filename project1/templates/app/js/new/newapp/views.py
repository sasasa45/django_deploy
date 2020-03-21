from django.shortcuts import render
# from newapp.models import Person
from newapp.forms import Users
# Create your views here.
def show_person(request):
    person=Users()

    if request.method=="POST":

        person=Users(request.POST)
        if person.is_valid():
            # print("name "+person.cleaned_data["name"])
            # person.save()
            print("aaaa")
    print('bbbb')
    return render(request,"html.html",{'person':person})
