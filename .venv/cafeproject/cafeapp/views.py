from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from .models import booking,Staff,up
from django.contrib import messages
from cafeproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def hello (request):
    return HttpResponse("Hello Cyril")
def temp (request):
    return render(request, 'first.html')
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')



def bookin(request):
    if request.method == 'POST':
        bk = booking(
            name=request.POST.get("nam"),
            email=request.POST.get("mail"),
            phone=request.POST.get("phon"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            seating=request.POST.get("seating"),
            people=request.POST.get("people"),
            occasion=request.POST.get("occasion"),
            message=request.POST.get("message")
        )
        bk.save()

        subject = 'Reservation Confirmation'
        message = (
            f'Dear {bk.name},\n\n'
            f'Your Reservation has been successfully booked.\n\n'
            f'Occasion: {bk.occasion} on {bk.date}.\n\n'
            'Thank you for choosing Platia Restaurant\n'
            'Best Regards,\nPlatia Restaurant'
        )
        send_mail(subject, message, EMAIL_HOST_USER, [bk.email], fail_silently=False)

    return render(request, 'booking.html')

def viewdata(request):
    if request.method =='POST':
        b=booking.objects.get(id=request.POST.get("cid"))
        b.email=request.POST.get("email")
        b.save()
    data=booking.objects.all()
    return render(request, 'view.html',{'d':data})

def signup(request):
    if request.method == 'POST':
        sign = up(
            username=request.POST.get("uname"),
            email=request.POST.get("mail"),
            password=request.POST.get("pass")
        )
        sign.save()
    return render(request, 'signup.html')


def staff(request):
    if request.method == 'POST':
        reg = Staff(
            name=request.POST.get("nam"),
            email=request.POST.get("mail"),
            password=request.POST.get("pass"),
            phone=request.POST.get("phon"),
            role=request.POST.get("role"),
            shift=request.POST.get("shift")
        )
        reg.save()
    return render(request, 'staff/staffreg.html')


def login(request):
    if request.method == 'POST':
        utype = request.POST.get('utype')
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if utype == 'Staff':
            user = Staff.objects.filter(name=uname).first()

            if user:
                if pwd == user.password:
                    request.session['sid'] = user.name
                    return redirect('viewdata')
                else:
                    return HttpResponse("Incorrect password")
            else:
                return redirect('staffreg')

        elif utype == 'User':
            user = up.objects.filter(username=uname).first()

            if user:
                if pwd == user.password:
                    request.session['sid'] = user.username
                    return redirect('book')
                else:
                    return HttpResponse("Incorrect password")
            else:
                return redirect('signup')

    return render(request, 'login.html')