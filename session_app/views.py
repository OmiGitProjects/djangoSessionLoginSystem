from django.shortcuts import render, redirect
from .models import AddCourse, instructor
from .forms import RegisterInstructor, LoginInstructor
from django.contrib import messages

def instructorRegister(request):
    form = RegisterInstructor()

    if request.method == 'POST':
        form = RegisterInstructor(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your are Register')
            return redirect('login')

    context = {'form': form}
    return render(request, 'session_app/instructor_register.html', context)

def instructor_login(request):
    form = LoginInstructor()

    if request.method == 'POST':
        form = LoginInstructor(request.POST)

        instructor_ = instructor.objects.get(name=request.POST['name'])
        if instructor_.password == request.POST['password']:
            request.session['name'] = instructor_.name
            messages.success(request, 'Your are Logged in')
            return redirect('home-page')


    context = {'form': form}
    return render(request, 'session_app/login_instructor.html', context)

def homepage(request):
    name = request.session.get('name')

    context = {'name': name}
    return render(request, 'session_app/homepage.html', context)

def logout(request):
    if 'name' in request.session:
        request.session.flush()

    return redirect('home-page')