from django.urls import path, include

from .views.organization_organs_inventory import organization_organs_inventory
from .views.organization_add_edit_organ import organization_add_edit_organ
from .views.organization_directory import organization_directory
from .views.organization_organ_details import organization_organ_details
from .views.organization_organs_list import organization_organs_list
from .views.organization_analytics import organization_analytics
from .views.organization_organization_details import organization_organization_details

urlpatterns = [

    path('organization_organs_inventory', organization_organs_inventory,
        name='organization_organs_inventory'),
    path('organization_add_edit_organ', organization_add_edit_organ,
        name='organization_add_edit_organ'),
    path('organization_directory', organization_directory,
        name='organization_directory'),
    path('organization_organ_details', organization_organ_details,
        name='organization_organ_details'),
    path('organization_organs_list', organization_organs_list,
        name='organization_organs_list'),
    path('organization_analytics', organization_analytics,
        name='organization_analytics'),
    path('organization_organization_details', organization_organization_details,
        name='organization_organization_details'),
]

