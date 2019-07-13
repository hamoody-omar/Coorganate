'''
Created on Jul 8, 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def medical_professional_directory(request):
    '''This view gets all the available organizations.'''

    context_dict = {}

    # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username


    return render(request, 'medical_professional/medical_professional_directory.html', context_dict)
