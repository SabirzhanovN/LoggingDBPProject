from django.contrib import auth
from django.shortcuts import render, redirect
from .models import User
from django.db import connection
from shopApp.models import LoggingMoves


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                new_user = User.objects.create_user(
                    username=username,
                    password=password2
                )

                query1 = connection.queries[-1]['sql']
                new_user.save()
                query2 = connection.queries[-1]['sql']

                new_log = LoggingMoves.objects.create(
                    ip_address=request.META.get('REMOTE_ADDR'),
                    author='Admin',
                    method='CREATE',
                    sql_query=f'{query1};\n{query2};',
                    path=request.get_full_path(),
                    verdict='SUCCESS',
                    email=''
                )
                new_log.save()

                return redirect('login')
        else:
            return redirect('register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )
        query1 = connection.queries[-1]['sql']

        if user is not None:
            auth.login(request, user)
            query2 = connection.queries[-1]['sql']

            new_log = LoggingMoves.objects.create(
                ip_address=request.META.get('REMOTE_ADDR'),
                author='Admin',
                method='UPDATE',
                sql_query=f'{query1};\n{query2};',
                path=request.get_full_path(),
                verdict='SUCCESS',
                email=request.user.email
            )

            new_log.save()

            return redirect('dashboard')
        else:
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    user = request.user.username
    email = request.user.email

    auth.logout(request)
    query = connection.queries[-1]['sql']

    new_log = LoggingMoves.objects.create(
        ip_address=request.META.get('REMOTE_ADDR'),
        author=user,
        method='DELETE',
        sql_query=f'{query};',
        path=request.get_full_path(),
        verdict='SUCCESS',
        email=email
    )

    new_log.save()
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def delete_account(request, id):
    auth.logout(request)
    query1 = connection.queries[-1]['sql']

    user = User.objects.get(id=id)
    username = user.username
    email = user.email
    query2 = connection.queries[-1]['sql']

    user.delete()
    query3 = connection.queries[-2]['sql']
    query4 = connection.queries[-1]['sql']

    new_log = LoggingMoves.objects.create(
        ip_address=request.META.get('REMOTE_ADDR'),
        author=username,
        method='DELETE',
        sql_query=f'{query1};\n{query2};\n{query3};\n{query4};',
        path=request.get_full_path(),
        verdict='SUCCESS',
        email=email
    )
    new_log.save()

    return redirect('login')


def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = request.user

        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        user.save()
        query = connection.queries[-1]['sql']

        new_log = LoggingMoves.objects.create(
            ip_address=request.META.get('REMOTE_ADDR'),
            author=user.username,
            method='UPDATE',
            sql_query=f'{query};',
            path=request.get_full_path(),
            verdict='SUCCESS',
            email=user.email
        )
        new_log.save()
        return redirect('dashboard')

    return render(request, 'accounts/edit_profile.html')