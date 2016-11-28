from __future__ import unicode_literals

from django.db import models

class Specialist(models.Model):
    name         = models.CharField(max_length=100)
    specialty    = models.CharField(max_length=100)
    amater       = models.CharField(max_length=100)
    pcertificate = models.CharField(max_length=100)
    scertificate = models.CharField(max_length=100)
    mgroup       = models.CharField(max_length=100)
    pnumber1     = models.CharField(max_length=13)
    pnumber2     = models.CharField(max_length=13)
    
class Patient(models.Model):
    name       = models.CharField(max_length=100)
    sex        = models.CharField(max_length=1)
    bday       = models.DateTimeField()
    pnumber    = models.CharField(max_length=13)
    email      = models.EmailField(max_length=100)
    specialist = models.ForeignKey(Specialist)
    
class Alergy(models.Model):
    name        = models.CharField(max_lenght=100)
    description = models.TextField()
    patient     = models.ForeighKey(Patient, on_delete=models.CASCADE)

class History(models.Model):
    date        = models.DateTimeField()
    weight      = models.DecimalField(max_digits=5, decimal_places=2)
    height      = models.DecimalField(max_digits=3, decimal_places=2)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    patient     = models.ForeighKey(Patient, on_delete=models.CASCADE)
    
class Prescription(models.Model):
    date        = models.DateTimeField()
    description = models.TextField()
    patient     = models.ForeighKey(Patient, on_delete=models.CASCADE)
    
class Report(models.Model):
    date        = models.DateTimeField()
    description = models.TextField()
    treport     = models.CharField(max_lenght=20)
    patient     = models.ForeighKey(Patient, on_delete=models.CASCADE)

class Picture(models.Model):
    img      = CharField(max_length=255)
    comments = models.TextField()
    report   = models.ForeighKey(Report, on_delete=models.CASCADE)
