'''
Created on Jul 6, 2019

@author: Mahamat Oumar
'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from medical_professional.models import MedicalProfessional, Organization, MedicalProfessionalOrganization, OrganizationAddress


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

    # Get the username from Get request
    username = request.GET['id']

    # Get the medical professional from database
    medical_professional = MedicalProfessional.objects.get(
        user__username=username)
    context_dict['medical_professional'] = MedicalProfessional.objects.get(
        user__username=username)

    # Get the medical professional's organization from database
    medical_professional_organization = MedicalProfessionalOrganization.objects.get(
        medical_professional=medical_professional)
    context_dict['medical_professional_organization'] = medical_professional_organization

    # Get the organization's address
    organization_address = OrganizationAddress.objects.get(
        organzation=medical_professional.organization)
    context_dict['organization_address'] = organization_address

    return render(request, 'administrator/requested_user_account_detail.html', context_dict)


@login_required
def requested_organization_detail(request):
    '''This view returns an organization detail.'''

    # A dictionary to hold data
    context_dict = {}

    # Get the id from Get request
    id_ = request.GET['id_']

    # Get the  organization from database
    organization = Organization.objects.get(id=int(id_))
    context_dict['organization'] = organization

    # Get the organization's address
    organization_address = OrganizationAddress.objects.get(
        organzation=organization.organization)
    context_dict['organization_address'] = organization_address

    return render(request, 'administrator/requested_user_account_detail.html', context_dict)


@login_required
def approve_request(request):
    '''This view approves a request.'''

    if 'id' in request.GET:
        # Get the medical professional from database
        medical_professional = MedicalProfessional.objects.get(
            user__username=request.GET['id'])
        medical_professional.is_approved = True
        medical_professional.save()
    else:
        # Get the  organization from database
        organization = Organization.objects.get(id=int(request.GET('id_')))
        organization.is_approved = True
        organization.save()

    # Redirect to requested_registration
    return redirect('requested_registration')


@login_required
def decline_request(request):
    '''This view delete a declined request.'''

    if 'id' in request.GET:
        # Get the medical professional from database
        medical_professional = MedicalProfessional.objects.get(
            user__username=request.GET['id'])
        medical_professional.delete()
    else:
        # Get the  organization from database
        organization = Organization.objects.get(id=int(request.GET('id_')))
        organization.delete()

    # Redirect to requested_registration
    return redirect('requested_registration')
