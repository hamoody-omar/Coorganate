from django.urls import path, include
from .views.redirect_login_to_home import redirect_login_to_home
from .views.registration_type import registration_type, medical_professional_registration, organization_registration, request_review_message
from .views.requested_registration import requested_registration, requested_user_account_detail,requested_organization_detail, approve_request, decline_request
from .views.administrator_organs_list import administrator_organs_list
from .views.administrator_organ_details import administrator_organ_details

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
     path('home', redirect_login_to_home, name='home'),
     path('registration_type', registration_type, name='registration_type'),
     path('medical_professional_registration', medical_professional_registration,
         name='medical_professional_registration'),
     path('organization_registration', organization_registration,
         name='organization_registration'),
     path('request_review_message', request_review_message,
         name='request_review_message'),
     path('requested_registration', requested_registration,
         name='requested_registration'),
     path('requested_user_account_detail', requested_user_account_detail,
         name='requested_user_account_detail'),
     path('requested_organization_detail', requested_organization_detail,
         name='requested_organization_detail'),
     path('approve_request', approve_request,
         name='approve_request'),
     path('decline_request', decline_request,
         name='decline_request'),
     path('administrator_organs_list', administrator_organs_list,
        name='administrator_organs_list'),
     path('administrator_organ_details', administrator_organ_details,
        name='administrator_organ_details'),

]

urlpatterns += staticfiles_urlpatterns()
