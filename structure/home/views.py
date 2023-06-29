from django.shortcuts import render, HttpResponse
#from . models import Subcontact
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is home")
def about(request):
    #print("we are in viws")
    return render(request, 'about.html')
    #return HttpResponse("this is about")
def services(request):
    return render(request, 'services.html')

   # return HttpResponse("this is services")
def contact(request):
    '''
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        '''
    return render(request, 'contacts.html')
    #return HttpResponse("this is contact")
def buy(request):
     return render(request, 'buy.html')
'''
def subcontact(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    desc = request.POST.get("desc")
    subcontact = Subcontact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    subcontact.save()
    return render(request, 'contacts.html')
'''