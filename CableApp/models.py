from django.db import models

# Create your models here.
class Cable(models.Model): #standard cable library
    name = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    conductors = models.CharField(max_length=50, null=True)
    OuterDim = models.FloatField(max_length=50, null=True)
        
    def __str__(self):
        return self.name

class CableRun(models.Model): #project cables
    cabletag       = models.CharField(max_length=200)
    length         = models.CharField(max_length=200)
    cable          = models.ForeignKey(Cable, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cabletag
    
class Conduit(models.Model): #standard conduit library
    name           = models.CharField(max_length=50, null=True)
    InnerDimension = models.FloatField(max_length=200, null=True)
    OuterDimension = models.FloatField(max_length=200, null=True)
    Area           = models.FloatField(max_length=200, null=True)

    def calculate_area(innerdimension):
        result = 3.14*innerdimension**2
        return result

    def __str__(self):
        return self.name
    
class ConduitRun(models.Model): #project conduit 
    conduittag = models.CharField(max_length=200)
    conduit = models.ForeignKey(Conduit, on_delete=models.CASCADE)
    cable = models.ManyToManyField(CableRun)

    def calculate_fill():
        return fill

    def __str__(self):
        return self.conduittag