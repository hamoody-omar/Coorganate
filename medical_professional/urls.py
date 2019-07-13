from django.urls import path, include

from .views.medical_professional_organs_list import medical_professional_organs_list
from .views.medical_professional_directory import medical_professional_directory
from .views.medical_professional_complete_account_setup import medical_professional_complete_account_setup
from .views.medical_professional_organ_details import medical_professional_organ_details
from .views.medical_professional_organization_directory import medical_professional_organization_directory
from .views.medical_professional_organization_details import medical_professional_organization_details

urlpatterns = [
    path('medical_professional_organs_list', medical_professional_organs_list,
        name='medical_professional_organs_list'),
    path('medical_professional_directory', medical_professional_directory,
        name='medical_professional_directory'),
    path('medical_professional_complete_account_setup', medical_professional_complete_account_setup,
        name='medical_professional_complete_account_setup'),
    path('medical_professional_organ_details', medical_professional_organ_details,
        name='medical_professional_organ_details'),
    path('medical_professional_organization_directory', medical_professional_organization_directory,
        name='medical_professional_organization_directory'),
    path('medical_professional_organization_details', medical_professional_organization_details,
        name='medical_professional_organization_details'),
]
