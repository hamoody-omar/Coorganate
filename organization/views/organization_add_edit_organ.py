'''
Created on Jul 9 , 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from organization.models import Organization, Address, OrganAddress, UserOrganization, OrganizationOrgan
from organ.models import Organ, Person, PersonOrgan
from organ.constants import organ_types, races, blood_types
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def organization_add_edit_organ(request):
    '''This view adds an organ under this.organization'''

    context_dict = {}

     # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username

        if request.method == 'POST':
            #try:
                # Get organzition

                #print(x)
                organization = UserOrganization.objects.get(user=user).organization

                organ = Organ()
                organ.organ_type = request.POST['organ_type']
                #date_extracted = datetime.strptime(request.POST['date_extracted'], "%B %d, %Y")
                #organ.date_extracted = date_extracted
                #expiration_date = datetime.strptime(request.POST['expiration_date'],  "%B %d, %Y")
                organ.expiration_date = request.POST['expiration_date']
                #organ.expiration_date = expiration_date
                #if expiration_date > datetime.now
                
                if 'is_expired' in request.POST:
                    organ.is_expired = True
                if 'comment' in request.POST:
                    organ.comment = request.POST['comment']
                if 'description' in request.POST:
                    organ.description = request.POST['description']
                if 'organ_image' in request.POST:
                    organ.organ_image = organ_image
                
                organ.save()

                person = Person()
                #person.first_name = request.POST['first_name']
                #person.last_name = request.POST['last_name']
                person.age = int(request.POST['age'])
                
                if 'race' in request.POST:
                    person.race = request.POST['race']
                if 'blood_type' in request.POST:
                    person.blood_type = request.POST['blood_type']
                if 'weight' in request.POST:
                    person.weight = int(request.POST['weight'])
                if 'height' in request.POST:
                    person.height = int(request.POST['height'])
                if 'is_alive' in request.POST:
                    person.is_alive = True
                else:
                    person.is_alive = False
                if 'comment' in request.POST:
                    person.comment = request.POST['comment']
                
                person.who = 2
                
                person.save()

                address = Address()
                address.street_address = request.POST['street_address']
                address.city = request.POST['city']
                address.zip_code = request.POST['zip_code']
                address.state = request.POST['state']

                address.save()

                # Relate organ to person
                person_organ = PersonOrgan()
                person_organ.person = person
                person_organ.organ = organ
                person_organ.save()

                # Relate organ to organization
                organization_organ = OrganizationOrgan()
                organization_organ.organization = organization
                organization_organ.organ = organ
                organization_organ.save()

                # Relate organ to address
                organ_address = OrganAddress()
                organ_address.address = address
                organ_address.organ = organ
                organ_address.save()


                print("added")
                
                return redirect('/organization_organs_inventory')

            #except:
                print('something went wrong')
                context_dict['error'] = "Ops! Something went wrong."

        else:

            if 'id' in request.GET:

                organ = Organ.objects.get(id=int(request.GET['id']))

                context_dict['organ'] = organ
                context_dict['address'] = OrganAddress.objects.get(organ=organ)
                context_dict['person'] = PersonOrgan.objects.get(organ=organ)

        context_dict['races'] = races()
        context_dict['organ_types'] = organ_types()
        context_dict['blood_types'] = blood_types()

    else:
        context_dict['authentication_message'] = "User is not authenticated."

    return render(request, 'organization/organization_add_edit_organ.html', context_dict)
