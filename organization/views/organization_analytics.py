'''
Created on Jul 11, 2019

@author: Mahamat Oumar
'''

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan
from organ.models import Organ, Person, PersonOrgan, OrganWatched, OrganRequested
from organ.constants import organ_types, blood_types
from organ.utils import get_filtered_organs

from organization.models import Organization, MedicalProfessionalOrganization, Address, OrganizationAddress
from organ.models import Organ


@login_required
def organization_analytics(request):
    '''This view get the all the organs' analytics.'''
    
    context_dict = {}
    context_dict['organs'] = Organ.objects.all()


    return render(request, 'organization/organization_analytics.html', context_dict)
