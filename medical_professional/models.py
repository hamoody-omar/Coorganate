from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime


class MedicalProfessional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User Attrbutes:
    # username varchar(30)
    # first_name varchar(30)
    # last_name varchar(30)
    # email varchar
    # password hash of password string
    # groups Many-to-Many relationship to Group
    # user_permissions Many-to-Many relationship to Permission
    # is_staff Boolean
    # is_active Boolean
    # is_superuser Boolean
    # last_login DateTime of last log in
    # date_joined DateTime of creation
    license_ID = models.CharField(max_length=100)
    cellphone_number = models.CharField(max_length=12)
    work_phone_number = models.CharField(max_length=12, default='')
    profile_image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} MedicalProfessional'

    def save_image(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


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


class MedicalProfessionalOrganization(models.Model):
    id = models.AutoField(primary_key=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medical professional", db_index=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="the related organization", db_index=True)

    def __str__(self):
        return "id: "+str(self.id)+", medical_professional: "+self.medical_professional+", organization: "+self.organization


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50, default="United States")
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "id: "+str(self.id)+", street_address: "+self.street_address+", city: "+self.city+", zip_code: "+self.zip_code+", country: "+self.country


class OrganizationAddress(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="the related Address", db_index=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name="the related organization", db_index=True)

    # def __str__(self):
    # +", organization: "+self.organization+", address: "+self.address
    # return "id: "+str(self.id)


class MedicalProfessionalAddress(models.Model):
    id = models.AutoField(primary_key=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medical professional", db_index=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="the related address", db_index=True)

    # def __str__(self):
    # +", medical_professional: "+self.medical_professional+", address: "+self.address
    # return "id: "+str(self.id)


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10000, default='')

    def __str__(self):
        return "id: "+str(self.id)+", position_name: "+self.position_name+", role: "+self.role


class MedicalProfessionalPosition(models.Model):
    id = models.AutoField(primary_key=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medical professional", db_index=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name="the related position", db_index=True)

    def __str__(self):
        # +", medical_professional: "+self.medical_professional+", position: "+self.position
        return "id: "+str(self.id)
