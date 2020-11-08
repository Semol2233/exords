from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

class profileinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pictures',blank=True)

    def __str__(self):
        return self.user.username




class location_model(models.Model):
    Location =  models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('lsoc')

    def __str__(self):
        return self.loc


class Post_Asn(models.Model):
    VLAN = models.IntegerField()
    DESCRIPTION = models.TextField()
    LOCATION = models.ForeignKey(location_model, on_delete=models.CASCADE ,blank=True, null=True ,related_name='books')
    
    def __str__(self):
        return self.VLAN

    def get_absolute_url(self):
        return reverse('homes')