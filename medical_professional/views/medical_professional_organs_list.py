'''
Created on Jul 12, 2019

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

@login_required
def medical_professional_organs_list(request):
    '''This view gets all the available organs.'''

    context_dict = {}

    if request.method == 'POST':
        filter =  request.POST['organs_filter'].split('---')
        if filter[0]=='request_status':
            context_dict['organs_range'] = get_filtered_organs('request_status' ,filter[1])
            context_dict['curent_filter'] = filter[1]
        elif filter[0]=='organ_type':
            context_dict['organs_range'] = get_filtered_organs('organ_type' ,filter[1])
            context_dict['curent_filter'] = filter[1]
        elif filter[0]=='blood_type':
            context_dict['organs_range'] = get_filtered_organs('blood_type' ,filter[1])
            context_dict['curent_filter'] = filter[1]
        else:
            context_dict['curent_filter'] = "All"
            context_dict['organs_range'] = get_filtered_organs('all' ,'all')
    else:
        
        context_dict['curent_filter'] = "notrequested"
        context_dict['organs_range'] = get_filtered_organs('request_status' ,'notrequested')

    context_dict['organ_types'] = organ_types
    context_dict['blood_types'] = blood_types

    return render(request, 'medical_professional/medical_professional_organs_list.html', context_dict)
