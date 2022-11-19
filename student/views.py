from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def homepage(request):
    data = Student.objects.all();
    return render(request, 'student/homepage.html', {'data':data})

def add_student(request):
    if request.method == "POST":
        roll = request.POST['roll']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']

        data = Student(roll=roll, fname=fname, lname=lname, email=email, phone=phone)
        data.save()

        return redirect('/')
    
    return render(request, 'student/addstd.html')

def delete_student(request, roll):
    record = Student.objects.get(pk=roll)
    record.delete()
    return redirect('/')


def update_student(request, roll):
    record = Student.objects.get(pk=roll)
    return render(request, 'student/updatestd.html', {'data': record})

def do_updated_changes(request, roll):
    roll = request.POST['roll']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']

    record = Student.objects.get(pk=roll)
    
    record.roll = roll
    record.fname = fname
    record.lname = lname
    record.email = email
    record.phone = phone

    record.save()

    return redirect('/')

    
