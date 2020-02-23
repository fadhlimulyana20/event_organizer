from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profession = models.CharField(max_length=50, blank=True, null=True)
    institute = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(auto_now_add=False, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image_profile = models.ImageField(upload_to='images/profile/', default='images/profile/default/icons8-user-100.png')
    address = models.OneToOneField('Address', on_delete=models.CASCADE, null=True, blank=True)
    
    

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    
    def get_profession_code(self):
        if self.profession.lower() == 'dokter':
            code_profession = 'DR'
        elif self.profession.lower() == 'perawat':
            code_profession = 'PR'
        elif self.profession.lower() == 'bidan':
            code_profession = 'BD'
        else:
            code_profession = 'OT'
        
        return code_profession
    
class Address(models.Model):
    name = models.CharField(default="untitled location", blank=False, null=False, max_length=120)
    street = models.CharField(default="untitled street", blank=False, null=False, max_length=300)
    sub_district = models.CharField(default="untitled sub district", blank=False, null=False, max_length=120)
    city = models.CharField(default="untitled city", blank=False, null=False, max_length=120)
    province_or_state = models.CharField(default="untitled province", blank=False, null=False, max_length=120)
    country = models.CharField(default="untitled country", blank=False, null=False, max_length=120)
    postal_code = models.DecimalField(decimal_places=0, max_digits=5)

    def __str__(self):
        return self.name