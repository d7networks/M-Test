from django.db import models

# Create your models here.
class Client(models.Model):

    partner = models.ForeignKey('partner.Partner', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):

        return self.name