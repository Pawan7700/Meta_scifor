from django.shortcuts import render
from django.http import HttpResponse
from HomeApp.models import Book_Table

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        person = request.POST.get('person')

        if name !='' and email !='' and number !='' and date !='' and person !='':

            data = Book_Table(Name=name,Email=email,Number=number,Date=date,Person=person)
            data.save()
    return render(request, 'book_table.html')

def order(request):
    return render(request, 'order.html')

