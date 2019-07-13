'''
Created on Jul 10, 2019

@author: Mahamat Oumar
'''

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan
from organ.models import Organ, Person, PersonOrgan, OrganWatched, OrganRequested

from organization.models import Organization, MedicalProfessionalOrganization, Address, OrganizationAddress


@login_required
def administrator_organ_details(request):
    '''This view get the details of an organ'''
    
    context_dict = {}

    if request.method == 'GET':

        if 'id' in request.GET:
            
            organ = Organ.objects.get(id=request.GET['id'])
            context_dict['organ'] = organ

            context_dict['person'] = PersonOrgan.objects.get(organ=organ).person

            context_dict['address'] = OrganAddress.objects.get(organ=organ).address

            context_dict['organization'] = OrganizationOrgan.objects.get(organ=organ).organization

            try:
                requester = OrganRequested.objects.get(organ=organ).medical_professional
                context_dict['requester'] = requester
                context_dict['requester_organization'] = MedicalProfessionalOrganization.objects.get(medical_professional=requester).organization
            except:
                print('no request')

            context_dict['organ_watchers'] = OrganWatched.objects.filter(organ=organ)


    return render(request, 'administrator/administrator_organ_details.html', context_dict)
