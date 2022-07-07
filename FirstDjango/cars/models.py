from django.db import models

# Create your models here.
class cars(models.Model):
    carname = models.CharField(blank=False, max_length=100)
    model = models.IntegerField()
    year = models.IntegerField()
    hp = models.IntegerField()
    new = models.BooleanField()