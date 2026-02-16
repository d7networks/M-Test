from django.db import models
from partner.models import Partner
from django.conf import settings


class Instance(models.Model):
    instance_name = models.CharField(max_length=255)

    def __str__(self):
        return self.instance_name

class SMSC(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100,null=True,blank=True)
    port = models.IntegerField()
    username = models.CharField(max_length=100,null=True,blank=True)
    key = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    partner = models.ForeignKey(Partner,on_delete=models.SET_NULL,null=True,blank=True)
    instance = models.ForeignKey(Instance,on_delete=models.SET_NULL,null=True,blank=True)
    method = models.ForeignKey(SMSC,on_delete=models.SET_NULL,null=True,blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    # email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15)
    # account_type = models.CharField(max_length=50, choices=AccountType.choices, null=True, blank=True)
    # company_url = models.URLField(null=True, blank=True)
    # address = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.client_name

