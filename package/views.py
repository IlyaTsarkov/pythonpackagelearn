from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import NewPackage
from .models import Package


# Create your views here.
def home(request):
    return render(request, 'package/home.html')


def personal_cabinet(request):
    packages = Package.objects.filter(user=request.user).order_by('-title')
    if request.method == 'POST':
        return redirect('personal_cabinet')
    else:
        return render(request, 'package/personal_cabinet.html', {'packages': packages})


def currentpackage(request, package_pk):
    package = get_object_or_404(Package, pk=package_pk, user=request.user)
    if request.method == 'POST':
        return redirect('editpackage')
    else:
        return render(request, 'package/view_package.html', {'package': package})


def editpackage(request, package_pk):
    package = get_object_or_404(Package, pk=package_pk, user=request.user)
    form = NewPackage(instance=package)
    if request.method == 'GET':
        return render(request, 'package/edit_package.html', {'package': package, 'form': form})
    else:
        try:
            form = NewPackage(request.POST, instance=package)
            form.save()
            return redirect('personal_cabinet')
        except ValueError:
            return render(request, 'package/edit_package.html', {'form': form, 'package': package,
                                                                 'error': 'Недопустимая '
                                                                          'длина '
                                                                          'названия'})


def deletepackage(request, package_pk):
    package = get_object_or_404(Package, pk=package_pk, user=request.user)
    if request.method == 'POST':
        package.delete()
        return redirect('personal_cabinet')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'package/signupuser.html', {'registerform': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('personal_cabinet')
            except IntegrityError:
                return render(request, 'package/signupuser.html',
                              {'registerform': UserCreationForm(), 'error': 'Данное имя уже используется'})
        else:
            return render(request, 'package/signupuser.html',
                          {'registerform': UserCreationForm(), 'error': 'Пароли не совпадают'})


def loginuser(request):
    if request.method == "GET":
        return render(request, 'package/loginuser.html', {'authenticationform': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'package/loginuser.html', {'authenticationform': AuthenticationForm(),
                                                              'error': 'Пользователь с такими данными не найден. '
                                                                       'Проверьте правильность введенных данных.'})
        else:
            login(request, user)
            return redirect('personal_cabinet')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def createnewpackage(request):
    if request.method == "GET":
        return render(request, 'package/createnewpackage.html', {'NewPackage': NewPackage})
    else:
        try:
            form = NewPackage(request.POST)
            newpackage = form.save(commit=False)
            newpackage.user = request.user
            newpackage.save()
            return redirect('personal_cabinet')
        except ValueError:
            return render(request, 'package/createnewpackage.html', {'NewPackage': NewPackage, 'error': 'Недопустимая '
                                                                                                        'длина '
                                                                                                        'названия'})
