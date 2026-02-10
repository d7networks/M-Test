from django.db import models

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Network(models.Model):

    country = models.ForeignKey('network.Country', on_delete=models.PROTECT)
    name = models.CharField(max_length=256)
    number_matching = models.CharField(max_length=256)

    def __str__(self):

        return f'{self.country.name} - {self.name}'
    

class Connector(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):

        return self.name