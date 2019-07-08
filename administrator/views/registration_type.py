'''
Created on Jul 7, 2019

@author: Mahamat Oumar
'''

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from administrator.forms import UserRegisterForm, MedicalProfessionalForm, OrganizationForm, AddressForm
from medical_professional.models import Organization, MedicalProfessional, MedicalProfessionalOrganization, Address, OrganizationAddress


def registration_type(request):
    '''This view provides the different registration types'''

    return render(request, 'administrator/registration_type.html', {})


def medical_professional_registration(request):
    '''This view allows medical professionals to request a registration'''

    if request.method == 'POST':
        print("heere")

        # Get forms
        user_form = UserRegisterForm(request.POST)
        med_pro_form = MedicalProfessionalForm(request.POST)

        # Validate forms
        if user_form.is_valid() and med_pro_form.is_valid():
            user_form.save()
            med_pro_form.save()
            print("validated")

            # Get medical professional and associate it with their organziation
            # username = user_form.cleaned_data.get('username')
            # med_pro = MedicalProfessional.objects.get(
            #     user__username=username)
            # organization = Organization.objects.get(
            #     id=int(request.POST['organization']))
            # med_pro_organization = MedicalProfessionalOrganization()
            # med_pro_organization.medical_professional = med_pro
            # med_pro_organization.organization = organization
            # med_pro_organization.save()

            messages.success(
                request, f'Thank you for your request. We will review your form and get back to you as soon as possible.')
            return redirect('/request_review_message/')

    context_dict = {}
    # Get the forms and render the medical professional registration form
    context_dict['user_form'] = UserRegisterForm()
    context_dict['med_pro_form'] = MedicalProfessionalForm()
    # context_dict['Organization'] = Organization.objects.filter(
    #    is_approved=True)

    return render(request, 'administrator/medical_professional_registration.html', context_dict)


def organization_registration(request):
    '''This view allows organizations to request a registration'''

    if request.method == 'POST':

        # Get forms
        organization_form = OrganizationForm(request.POST)
        address_form = AddressForm(request.POST)

        # Validate forms
        if organization_form.is_valid() and address_form.is_valid():
            organization_form.save()
            address_form.save()

            # Get organization and associate it with their address
            support_email = organization_form.cleaned_data.get('support_email')
            organization = Organization.objects.get(
                support_email=support_email)

            street_address = address_form.cleaned_data.get('street_address')

            address = Address.objects.get(
                street_address=street_address)
            organization_address = OrganizationAddress()
            organization_address.address = address
            organization_address.organization = organization
            organization_address.save()

            messages.success(
                request, f'Thank you for your request. We will review your form and get back to you as soon as possible.')

            return redirect('/request_review_message/')
    else:

        # Get the forms and render the organization registration form
        context_dict = {}
        context_dict['organization_form'] = OrganizationForm()
        context_dict['address_form'] = AddressForm()

    return render(request, 'administrator/organization_registration.html', context_dict)


def request_review_message(request):
    '''This view render request review message'''

    context_dict = {}
    context_dict['message'] = 'Thank you for your request. We will review your form and get back to you as soon as possible.'

    return render(request, 'administrator/request_review_message.html', context_dict)
