

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from medical_professional.forms import AddressForm

def medical_professional_complete_account_setup(request):

	# if request.method == 'POST':

 #        # Get forms
 #        user_form = UserRegisterForm(request.POST)
 #        address_form = AddressForm(request.POST)

 #        # Validate forms
 #        if user_form.is_valid() and address_form.is_valid():
 #            user_form.save()

 #            # Get user and associate with medical professional
 #            username = user_form.cleaned_data.get('username')
 #            user = User.objects.get(username=username)

 #            license_ID = med_pro_form.cleaned_data.get('license_ID')
 #            cellphone_number = med_pro_form.cleaned_data.get(
 #                'cellphone_number')
 #            work_phone_number = med_pro_form.cleaned_data.get(
 #                'work_phone_number')

 #            med_pro = MedicalProfessional()
 #            med_pro.user = user
 #            med_pro.license_ID = license_ID
 #            med_pro.cellphone_number = cellphone_number
 #            med_pro.work_phone_number = work_phone_number
 #            med_pro.save()

 #            # Associate medical professional with their organziation
 #            organization = Organization.objects.get(
 #                 id=int(request.POST['organization']))
 #            med_pro_organization = MedicalProfessionalOrganization()
 #            med_pro_organization.medical_professional = med_pro
 #            med_pro_organization.organization = organization
 #            med_pro_organization.save()

 #            messages.success(
 #                request, f'Thank you for your request. We will review your form and get back to you as soon as possible.')
 #            return redirect('/request_review_message')

 #    messages.success(
 #        request, f'Something was wrong. Make sure your password is not too similar to your username.')
 #    context_dict = {}
 #    # Get the forms and render the medical professional registration form
 #    context_dict['user_form'] = UserRegisterForm()
 #    context_dict['med_pro_form'] = MedicalProfessionalForm(request.POST)
 #    context_dict['Organization'] = Organization.objects.filter(
 #        is_approved=True)

 #    return render(request, 'administrator/medical_professional_registration.html', context_dict)

    context_dict = {}

    # Check whether user is already authenticated
    if request.user.is_authenticated:
        user = request.user
        context_dict['user'] = user
        context_dict["username"] = user.username


    return render(request, 'medical_professional/medical_professional_complete_account_setup.html', context_dict)
