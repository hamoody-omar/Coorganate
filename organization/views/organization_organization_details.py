'''
Created on Jul 12 , 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan, MedicalProfessionalOrganization, OrganizationAddress
from organ.models import Organ, Person, PersonOrgan
from django.contrib.auth.decorators import login_required
from organ.constants import organ_types, races, blood_types


@login_required
def organization_organization_details(request):
    '''This view gets all this.organization's organs.'''

    context_dict = {}

    # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username

        print(user)

            
        try:
            # Get organzition
            organization = Organization.objects.get(id=request.GET['id'])
            
            context_dict['organization'] = organization
            context_dict['address'] = OrganizationAddress.objects.get(organization=organization).address

            context_dict['med_pros_organizations'] = MedicalProfessionalOrganization.objects.filter(organization=organization)

        except:
            context_dict['error'] = "You are not associated with any organization."

            print('fed')
    else:
        context_dict['authentication_message'] = "User is not authenticated."

    return render(request, 'organization/organization_organization_details.html', context_dict)

