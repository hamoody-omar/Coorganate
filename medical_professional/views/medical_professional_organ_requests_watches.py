'''
Created on Jul 6, 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from medical_professional.models import MedicalProfessional
from organization.models import  Organization, MedicalProfessionalOrganization, OrganizationAddress, UserOrganization
from organ.models import Organ, Person, PersonOrgan, OrganRequested, OrganWatched


@login_required
def medical_professional_organ_requests_watches(request):
    ''''''

    # A dictionary to hold data
    context_dict = {}

    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username

        context_dict['med_pro_requests'] = OrganRequested.objects.filter(
            medical_professional__user=user)
        context_dict['med_pro_watches'] = OrganWatched.objects.filter(
            medical_professional__user=user)

    return render(request, 'medical_professional/medical_professional_organ_requests_watches.html', context_dict)
