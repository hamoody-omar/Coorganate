'''
Created on Jul 9 , 2019

@author: Mahamat Oumar
'''


from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
from organ.models import Organ
from medical_professional.models import MedicalProfessional


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    domain_url = models.CharField(max_length=200)
    support_email = models.CharField(max_length=100)
    work_phone_number1 = models.CharField(max_length=12)
    work_phone_number2 = models.CharField(max_length=12, default='')
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return "id: "+str(self.id)+", name: "+self.name+", domain_url: "+self.domain_url+", support_email: "+self.support_email+", work_phone_number1: "+self.work_phone_number1+", work_phone_number2: "+self.work_phone_number2+", date_added: "+str(self.date_added)+", is_approved: "+str(self.is_approved)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50, default="United States")
    #date_added = models.DateTimeField(default=datetime.now, blank=True)

    #def __str__(self):
    #    return "id: "+str(self.id)+", street_address: "+self.street_address+", city: "+self.city+", zip_code: "+self.zip_code+", country: "+self.country


class UserOrganization(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="the related organization", db_index=True)

    #def __str__(self):
    #   return "id: "+str(self.id)+", medical_professional: "+self.medical_professional+", organization: "+self.organization


class OrganizationAddress(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="the related address", db_index=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="the related organization", db_index=True)


class OrganizationOrgan(models.Model):
    id = models.AutoField(primary_key=True)
    organ = models.ForeignKey(
        Organ, on_delete=models.CASCADE, verbose_name="the related organ", db_index=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="the related organization", db_index=True)

class MedicalProfessionalOrganization(models.Model):
    id = models.AutoField(primary_key=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medical professional", db_index=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="the related organization", db_index=True)

    #def __str__(self):
    #    return "id: "+str(self.id)+", medical_professional: "+self.medical_professional+", organization: "+self.organization


class MedicalProfessionalAddress(models.Model):
    id = models.AutoField(primary_key=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medical professional", db_index=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="the related address", db_index=True)

    # def __str__(self):
    # +", medical_professional: "+self.medical_professional+", address: "+self.address
    # return "id: "+str(self.id)


class OrganAddress(models.Model):
    id = models.AutoField(primary_key=True)
    organ = models.ForeignKey(
        Organ, on_delete=models.CASCADE, verbose_name="the related medical organ", db_index=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="the related address", db_index=True)
