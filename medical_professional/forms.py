from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from medical_professional.models import MedicalProfessional
from organization.models import Organization, Address

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

class OrganizationUserRegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class MedicalProfessionalForm(forms.ModelForm):

    class Meta:
        model = MedicalProfessional
        fields = ['license_ID', 'cellphone_number', 'work_phone_number']


class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['name', 'domain_url', 'support_email',
                  'work_phone_number1', 'work_phone_number2']


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['street_address', 'city', 'zip_code', 'state']
