from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Doctor
from .models import Patient


def About(request):
    return render(request, 'about.html')


def Home(request):
    return render(request, 'home.html')


def Contact(request):
    return render(request, 'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    d = 0
    p = 0
    for i in doctors:
        d += 1
    for i in patient:
        p += 1

    d1 = {'d': d, 'p': p}
    return render(request, 'index.html',  d1)


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user is not None:
            try:
                if user.is_staff:
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except Exception as e:
                error = "yes"
        else:
            error = "yes"

        return render(request, 'login.html', {'error': error})

    return render(request, 'login.html', {'error': error})


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('admin_login')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()

    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')

    error = ""
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']

        try:
            # Ensure these field names match your model
            Doctor.objects.create(name=n, mobile=m, special=sp)
            messages.success(request, 'Record saved successfully!')
            return redirect('view_doctor')
        except Exception as e:
            print(e)
            messages.error(request, 'Failed to add doctor. Please try again.')
            error = 'yes'

    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()

    d = {'doc': doc}
    return render(request, 'view_patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    if not request.user.is_staff:
        return redirect('login')

    error = ""
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        c = request.POST['mobile']
        a = request.POST['address']

        try:

            Patient.objects.create(name=n, gender=g, mobile=c, address=a)
            messages.success(request, 'Record saved successfully!')
            return redirect('view_patient')
        except Exception as e:
            print(e)
            messages.error(request, 'Failed to add doctor. Please try again.')
            error = 'yes'

    d = {'error': error}
    return render(request, 'add_patient.html', d)



