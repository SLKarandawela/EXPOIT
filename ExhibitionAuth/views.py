from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ExhibitionAuth.models import *


# Create your views here.
# home page
def exhibition_home_page(request):
    return render(request, 'exhibit_auth/index.html')


# login view
def user_login_feature(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        user_password = request.POST.get('userPassword')
        auth_user = authenticate(request, username=user_name, password=user_password)

        if auth_user is not None:
            request.session['id'] = auth_user.id
            login(request, auth_user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'EXHIBITOR':
                # messages.success(request, 'Welcome Back' + ' ' + str(request.user.username))
                return redirect('create_exhibition')

            if group == 'VISITOR':
                # messages.success(request, 'Welcome Back' + ' ' + str(request.user.username))
                return redirect('all_exhibitions')

            if request.user.is_staff:
                # messages.success(request, 'Welcome Back' + ' ' + str(request.user.username))
                print(user_name)
                print(user_password)
                return redirect('admin-dashboard-display')

            messages.success(request, 'Welcome Back')

        else:
            messages.error(request, 'username or password is incorrect')
    return render(request, 'exhibit_auth/sign_in.html')


# exhibitor register view
def exhibitor_register_view(request):
    if request.method == 'POST':
        ex_username = request.POST.get('exhibitor_username').strip()
        ex_password = request.POST.get('exhibitor_password')
        ex_mail = request.POST.get('exhibitor_password')
        company = request.POST.get('exhibitor_company')
        company_address = request.POST.get('exhibitor_address')
        company_contact = request.POST.get('exhibitor_contact_number')

        print(company, company_address, company_contact)


        if User.objects.all().exists():
            last_system_user = User.objects.last()
            last_sys_id = last_system_user.id

        else:
            last_sys_id = 0

        exhibitor_user = User.objects.create_user(
            id=last_sys_id + 1,
            username=ex_username,
            email=ex_mail
        )

        exhibitor_user.set_password(ex_password)

        print("This is test username", exhibitor_user.username)


        try:
            if Group.objects.filter(name='EXHIBITOR').exists():
                exhibitor_group = None
                print('ok')
            else:
                print('not ok')
                new_exhibitor_group = Group(name='EXHIBITOR')
                new_exhibitor_group.save()
        except:
            print('error')

        exo_group = Group.objects.get(name='EXHIBITOR')
        exhibitor_user.groups.add(exo_group)
        exhibitor_user.save()

        new_exhibitor = Exhibitor(
            exhibitor_user=exhibitor_user,
            exhibitor_company_name=company,
            exhibitor_address=company_address,
            exhibitor_mobile_number=company_contact
        )

        new_exhibitor.save()

        # return redirect()

    return render(request, 'exhibit_auth/exhibitor_signup.html')


# visitor register view
def visitor_register_view(request):
    return render(request, 'exhibit_auth/visitor_signup.html')
