from django.contrib import admin

from medical_professional.models import Address, MedicalProfessional, MedicalProfessionalAddress, MedicalProfessionalOrganization, MedicalProfessionalPosition, Organization, OrganizationAddress, Position

admin.site.register(MedicalProfessional)
admin.site.register(Organization)
admin.site.register(Address)
admin.site.register(Position)
admin.site.register(MedicalProfessionalOrganization)
admin.site.register(MedicalProfessionalAddress)
admin.site.register(MedicalProfessionalPosition)
admin.site.register(OrganizationAddress)
