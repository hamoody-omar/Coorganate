'''
Created on Jul 7, 2019

@author: Mahamat Oumar
'''

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

        print("user form ", user_form.is_valid())
        print("med form ", med_pro_form.is_valid())

        # Validate forms
        if user_form.is_valid() and med_pro_form.is_valid():
            user_form.save()

            # Get user and associate with medical professional
            username = user_form.cleaned_data.get('username')
            user = User.objects.get(username=username)

            license_ID = med_pro_form.cleaned_data.get('license_ID')
            cellphone_number = med_pro_form.cleaned_data.get(
                'cellphone_number')
            work_phone_number = med_pro_form.cleaned_data.get(
                'work_phone_number')

            med_pro = MedicalProfessional()
            med_pro.user = user
            med_pro.license_ID = license_ID
            med_pro.cellphone_number = cellphone_number
            med_pro.work_phone_number = work_phone_number
            med_pro.save()

            # Associate medical professional with their organziation
            # organization = Organization.objects.get(
            #     id=int(request.POST['organization']))
            # med_pro_organization = MedicalProfessionalOrganization()
            # med_pro_organization.medical_professional = med_pro
            # med_pro_organization.organization = organization
            # med_pro_organization.save()

            messages.success(
                request, f'Thank you for your request. We will review your form and get back to you as soon as possible.')
            return redirect('/request_review_message')

    messages.success(
        request, f'Something was wrong. Make sure your password is not too similar to your username.')
    context_dict = {}
    # Get the forms and render the medical professional registration form
    context_dict['user_form'] = UserRegisterForm()
    context_dict['med_pro_form'] = MedicalProfessionalForm(request.POST)
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

            return redirect('/request_review_message')
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
