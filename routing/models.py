from django.db import models

# Create your models here.
class Routing(models.Model):

    network = models.ForeignKey('network.Network', on_delete=models.PROTECT)
    connector = models.ForeignKey('network.Connector', on_delete=models.PROTECT)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    ratio = models.PositiveIntegerField()
    conf_added = models.BooleanField(default=False)

    def __str__(self):

        return f'{self.network} - {self.connector}'