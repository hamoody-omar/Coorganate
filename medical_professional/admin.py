from django.contrib import admin

from medical_professional.models import MedicalProfessional,   MedicalProfessionalPosition, Position
from organization.models import Address, MedicalProfessionalAddress, MedicalProfessionalOrganization, OrganizationAddress, Organization, UserOrganization, OrganizationOrgan
from organ.models import Organ

admin.site.register(MedicalProfessional)
admin.site.register(Organization)
admin.site.register(Address)
admin.site.register(Position)
admin.site.register(MedicalProfessionalOrganization)
admin.site.register(MedicalProfessionalAddress)
admin.site.register(MedicalProfessionalPosition)
admin.site.register(OrganizationAddress)
admin.site.register(UserOrganization)
admin.site.register(Organ)
admin.site.register(OrganizationOrgan)
