'''
Created on Jul 6, 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render


def redirect_login_to_home(request):
    '''This view checks whether an admin or another user logs in and redirects them to the appropriete page.'''

    context_dict = {}

    print("testss")

    # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username

        if user.groups.filter(name='SuperAdmins').exists():
            context_dict["is_admin"] = True
            return render(request, 'administrator/home.html', context_dict)
        else:
            context_dict["is_med_pro"] = True
            return render(request, 'medical_professional/home.html', context_dict)

    return render(request, 'login.html', context_dict)
