'''
Created on Jul 6, 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group, Permission

def redirect_login_to_home(request):
    '''This view checks whether an admin or another user logs in and redirects them to the appropriete page.'''

    context_dict = {}

    # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username

        new_group, created = Group.objects.get_or_create(name='SuperAdmins')
        new_group, created = Group.objects.get_or_create(name='OrganizationAdmins')
        new_group, created = Group.objects.get_or_create(name='MedicalProfessionals')

        if user.username == 'admin':
            Group.objects.get(name='SuperAdmins').user_set.add(user)

        if user.groups.filter(name='SuperAdmins').exists():
            context_dict["is_super_admin"] = True
            return redirect('/requested_registration')
        elif user.groups.filter(name='OrganizationAdmins').exists():
            context_dict["is_organization_admin"] = True
            return redirect('/organization_organs_inventory')
        elif user.groups.filter(name='MedicalProfessionals').exists():
            context_dict["is_med_pro"] = True
            return redirect('/medical_professional_organs_list')
        else:
            context_dict['error_message'] = 'Your account has not been approved yet.'
            messages.success(
                request, f'Thank you for your request. We will review your form and get back to you as soon as possible.')
            redirect('/login/')

    return render(request, 'login.html', context_dict)
