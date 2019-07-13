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
from administrator.forms import OrganizationUserRegisterForm


@login_required
def requested_registration(request):
    '''This view returns all registration requests, user account and organization registration, that are not approved yet.'''

    # A dictionary to hold data
    context_dict = {}

    # Get user accounts that are not approved yet
    unapproved_medical_professionals = MedicalProfessional.objects.filter(
        is_approved=False)
    context_dict['unapproved_medical_professionals'] = unapproved_medical_professionals

    # Get organization registrations that are not approved yet
    unapproved_organizations = Organization.objects.filter(is_approved=False)
    context_dict['unapproved_organizations'] = unapproved_organizations

    return render(request, 'administrator/requested_registration.html', context_dict)


@login_required
def requested_user_account_detail(request):
    '''This view returns a user account detail.'''

    # A dictionary to hold data
    context_dict = {}

    try:
        # Get the username from Get request
        username = request.GET['id']

        # Get the medical professional from database
        medical_professional = MedicalProfessional.objects.get(
            user__username=username)
        context_dict['medical_professional'] = MedicalProfessional.objects.get(
            user__username=username)

        # Get the medical professional's organization from database
        organization = MedicalProfessionalOrganization.objects.get(
            medical_professional=medical_professional).organization
        context_dict['organization'] = organization

        # Get the organization's address
        context_dict['organization_address'] = OrganizationAddress.objects.get(
            organization=organization).address
    except:
        context_dict['error_message'] = 'Ops! Something went wrong.'
        return redirect('/requested_registration')

    return render(request, 'administrator/requested_user_account_detail.html', context_dict)


@login_required
def requested_organization_detail(request):
    '''This view returns an organization detail.'''

    # A dictionary to hold data
    context_dict = {}
    try:
        # Get the id from Get request
        id_ = request.GET['id_']

        # Get the  organization from database
        organization = Organization.objects.get(id=int(id_))
        context_dict['organization'] = organization

        # Get the organization's address
        context_dict['organization_address'] = OrganizationAddress.objects.get(
            organization=organization).address

        context_dict['user_form'] = OrganizationUserRegisterForm()
    except:
        context_dict['error_message'] = 'Ops! Something went wrong.'
        return redirect('/requested_registration')

    return render(request, 'administrator/requested_organization_detail.html', context_dict)


@login_required
def approve_request(request):
    '''This view approves a request.'''

    context_dict = {}
    if 'id' in request.GET:
        # Get the medical professional from database
        medical_professional = MedicalProfessional.objects.get(
            user__username=request.GET['id'])
        medical_professional.is_approved = True
        medical_professional.save()
        
        # Add user to medical professional group 
        Group.objects.get(name='MedicalProfessionals').user_set.add(medical_professional.user)
   
    elif request.method == 'POST':
        try:

            user_form = OrganizationUserRegisterForm(request.POST)

            if user_form.is_valid():
                user_form.save()

                # Get user and associate with medical professional
                username = user_form.cleaned_data.get('username')
                user = User.objects.get(username=username)

                print('user is created')
                
                # Get the organization from database
                organization = Organization.objects.get(id=int(request.POST['id_']))
                organization.is_approved = True
                organization.save()

                print("approved")

                user_organization = UserOrganization()
                user_organization.organization = organization
                user_organization.user = user
                user_organization.save()

                # Add user to organization admin group 
                Group.objects.get(name='OrganizationAdmins').user_set.add(user)

                print("everything is set")
            else:
                redirect('/approve_request')
            
        except:
            print('Something went wrong')
            context_dict['error_message'] = 'Ops! Something went wrong.'
    # Redirect to requested_registration
    return redirect('/requested_registration')


@login_required
def decline_request(request):
    '''This view delete a declined request.'''

    if 'id' in request.GET:
        # Get the medical professional from database
        medical_professional = MedicalProfessional.objects.get(
            user__username=request.GET['id'])
        medical_professional.delete()
    elif 'id_' in request.GET:
        # Get the  organization from database
        organization = Organization.objects.get(id=int(request.GET('id_')))
        organization.delete()

    # Redirect to requested_registration
    return redirect('/requested_registration')
