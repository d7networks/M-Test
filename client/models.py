from django.db import models
from partner.models import Partner

# Create your models here.


class Instance(models.Model):
    instance_name = models.CharField(max_length=100)


    def __str__(self):
        return self.instance_name


class Smsc(models.Model):
    smsc_name = models.CharField(max_length=100)


    def __str__(self):
        return self.smsc_name


class Client(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15)
    default_smsc = models.ForeignKey(Smsc, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_name