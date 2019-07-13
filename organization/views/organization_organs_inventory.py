'''
Created on Jul 12 , 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan
from organ.models import Organ, Person, PersonOrgan
from django.contrib.auth.decorators import login_required
from organ.constants import organ_types, races, blood_types


@login_required
def organization_organs_inventory(request):
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
            organization = UserOrganization.objects.get(user=user).organization

            # Get the all the organs from this.organization
            organs = [organization_organ.organ for organization_organ in OrganizationOrgan.objects.filter(organization=organization)]
            #persons = [person_organ.person for organization_person in PersonOrgan.objects.filter(organization=organization)]

            persons = []
            for organ in organs:
                persons.append(PersonOrgan.objects.get(organ=organ).person)

            context_dict['organs_persons'] = zip(organs, persons)

            #context_dict['organs'] = organs
        except:
            context_dict['error'] = "You are not associated with any organization."

            print('fed')
    else:
        context_dict['authentication_message'] = "User is not authenticated."

    return render(request, 'organization/organization_organs_inventory.html', context_dict)

