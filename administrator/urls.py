from django.urls import path, include
from .views.redirect_login_to_home import redirect_login_to_home
from .views.registration_type import registration_type, medical_professional_registration, organization_registration, request_review_message

urlpatterns = [
    path('home', redirect_login_to_home, name='home'),
    path('registration_type', registration_type, name='registration_type'),
    path('medical_professional_registration', medical_professional_registration,
         name='medical_professional_registration'),
    path('organization_registration', organization_registration,
         name='organization_registration'),
    path('request_review_message', request_review_message,
         name='request_review_message'),

]
