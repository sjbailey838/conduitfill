from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

# class CableSize(models.Model):
#     size = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.size

# class JacketRating(models.Model):
#     rating = models.CharField(max_length=200)
        
#     def __str__(self):
#         return self.rating

# class Conductors(models.Model):
#     conductors = models.CharField(max_length=200)

#     def __str__(self):
#         return self.conductors

class Cable(models.Model): #standard cable library
    name = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    conductors = models.CharField(max_length=50, null=True)
        
    def __str__(self):
        return self.name

class CableRun(models.Model): #project cables
    cabletag = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    cable = models.ForeignKey(Cable, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cabletag
    
class Conduit(models.Model): #standard conduit library
    name = models.CharField(max_length=50, null=True)
    InnerDimension = models.CharField(max_length=200, null=True)
    OuterDimension = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class ConduitRun(models.Model): #project conduit 
    conduittag = models.CharField(max_length=200)
    conduit = models.ForeignKey(Conduit, on_delete=models.CASCADE)
    cable = models.ManyToManyField(CableRun)

    def __str__(self):
        return self.conduittag
