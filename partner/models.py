from django.db import models


class AccountType(models.TextChoices):
    PREPAID = 'Prepaid', 'Prepaid'
    POSTPAID = 'Postpaid', 'Postpaid'



class Partner(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    account_type = models.CharField(max_length=50, choices=AccountType.choices, null=True, blank=True)
    company_url = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.company_name