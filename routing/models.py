from django.db import models
from partner.models import Partner
from client.models import Client, Instance, Smsc

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=100)


    def __str__(self):
        return self.country_name


class Network(models.Model):
    network_name = models.CharField(max_length=100)


    def __str__(self):
        return self.network_name


class Connectors(models.Model):
    connector_name = models.CharField(max_length=100)


    def __str__(self):
        return self.connector_name


class Routers(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    connector = models.ForeignKey(Connectors, on_delete=models.CASCADE)
    connector_range = models.IntegerField()


    def __str__(self):
        return self.partner