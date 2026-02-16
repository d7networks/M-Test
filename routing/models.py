from django.db import models
from partner.models import Partner
from client.models import Client
from django.conf import settings

class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


class Network(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


class Connectors(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


class Routing(models.Model):
    partner = models.ForeignKey(Partner,on_delete=models.SET_NULL,null=True,blank=True)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True)
    network = models.ForeignKey(Network,on_delete=models.SET_NULL,null=True,blank=True)

    @property
    def get_percentage(self):
        return self.routingconnector_set.values('connector__name', 'percentage').first()

class RoutingConnector(models.Model):
    route = models.ForeignKey(Routing,on_delete=models.CASCADE)
    connector = models.ForeignKey(Connectors,on_delete=models.SET_NULL,null=True,blank=True)
    percentage = models.IntegerField()
    
    def __str__(self):
        return self.name