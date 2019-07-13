'''
Created on Jul 12, 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from organization.models import OrganizationAddress


@login_required
def medical_professional_organization_directory(request):
    '''This view gets all the available organizations.'''

    context_dict = {}

    # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username

        context_dict['organizations_addresses'] = OrganizationAddress.objects.all()

    return render(request, 'medical_professional/medical_professional_organization_directory.html', context_dict)
