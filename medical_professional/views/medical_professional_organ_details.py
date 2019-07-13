'''
Created on Jul 10, 2019

@author: Mahamat Oumar
'''

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan
from organ.models import Organ, Person, PersonOrgan, OrganRequested

from organization.models import Organization, MedicalProfessionalOrganization, Address, OrganizationAddress


@login_required
def medical_professional_organ_details(request):
    '''This view get the details of an organ'''
    
    context_dict = {}

    if request.method == 'GET':

        if 'id' in request.GET:
            
            organ = Organ.objects.get(id=request.GET['id'])
            context_dict['organ'] = organ

            context_dict['person'] = PersonOrgan.objects.get(organ=organ).person

            context_dict['address'] = OrganAddress.objects.get(organ=organ).address

            if not OrganRequested.objects.filter(organ=organ):
                    context_dict['not_requested'] = True


    return render(request, 'medical_professional/medical_professional_organ_details.html', context_dict)
