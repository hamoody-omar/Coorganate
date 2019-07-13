from django.db import models
from datetime import datetime
from PIL import Image
from medical_professional.models import MedicalProfessional


class Organ(models.Model):
    id = models.AutoField(primary_key=True)
    organ_type = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, default='')
    comment = models.CharField(max_length=10000, default='')
    #date_added = models.DateTimeField(default=datetime.now, blank=True)
    #date_extracted = models.DateTimeField()
    expiration_date = models.CharField(max_length=200)
    is_expired = models.BooleanField(default=False)
    organ_image = models.ImageField(
        default='organ_default.jpg', upload_to='organ_pics')

    #def __str__(self):
    #    return "id: "+str(self.id)+", organ_type: "+self.organ_type+", description: "+self.description+", comment: "+self.comment+", date_added: "+str(self.date_added)+", date_exactred: "+str(self.date_exactred)+", expiration_date: "+str(self.expiration_date)+", is_expired: "+str(self.is_expired)


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    race = models.CharField(max_length=50, default='unknown')
    blood_type = models.CharField(max_length=50, default='unknown')
    weight = models.IntegerField(default=0)  # lb
    height = models.IntegerField(default=0)
    is_alive = models.BooleanField(default=True)
    # 0=don’t know, 1=patient, 2=donor, 3=patient+donnor
    who = models.IntegerField(default=0)
    comment = models.CharField(max_length=10000, default='')

    #def __str__(self):
     #   return "id: "+str(self.id)+", first_name: "+self.first_name+", last_name: "+self.last_name+", age: "+str(self.age)+", race: "+self.race+", blood_type: "+self.blood_type+", weight: "+str(self.weight)+", height: "+str(self.height)+", is_alive: "+str(self.is_alive)+", who: "+str(self.who)


class PersonOrgan(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name="the related person", db_index=True)
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE,
                              verbose_name="the related medical Organ", db_index=True)
    
    
class Illness(models.Model):
    id = models.AutoField(primary_key=True)
    illness_name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, default='')
    comment = models.CharField(max_length=10000, default='')
    urgency = models.IntegerField(default=3)  # scale 1-10

    def __str__(self):
        return "id: "+str(self.id)+", illness_name: "+self.illness_name+", description: "+self.description+", comment: "+self.comment+", urgency: "+str(self.urgency)


class PersonIllness(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name="the related person", db_index=True)
    illness = models.ForeignKey(
        Illness, on_delete=models.CASCADE, verbose_name="the related illness", db_index=True)

    def __str__(self):
        # +", person: "+self.person+", illness: "+self.illness
        return "id: "+str(self.id)


class OrganReleased(models.Model):
    id = models.AutoField(primary_key=True)
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE,
                              verbose_name="the related medical Organ", db_index=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medial professional", db_index=True)

    def __str__(self):
        # +", organ: "+self.organ+", medical_professional: "+self.medical_professional
        return "id: "+str(self.id)


class OrganWatched(models.Model):
    id = models.AutoField(primary_key=True)
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE,
                              verbose_name="the related medical Organ", db_index=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medial professional", db_index=True)

    def __str__(self):
        # +", organ: "+self.organ+", medical_professional: "+self.medical_professional
        return "id: "+str(self.id)


class OrganRequested(models.Model):
    id = models.AutoField(primary_key=True)
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE,
                              verbose_name="the related medical Organ", db_index=True)
    medical_professional = models.ForeignKey(
        MedicalProfessional, on_delete=models.CASCADE, verbose_name="the related medial professional", db_index=True)

    def __str__(self):
        # +", organ: "+self.organ+", medical_professional: "+self.medical_professional
        return "id: "+str(self.id)

