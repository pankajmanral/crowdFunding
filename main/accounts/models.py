from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.

genderChoices = [
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]

class Contributor(AbstractUser):
    gender = models.CharField(choices=genderChoices,max_length=1,default='M')
    phone_number = models.CharField(max_length=10,null=False,default='')
    dob = models.DateField(default='',null=False)

    def save(self,*args,**kwargs):
        if kwargs.get('commit') == False:
            self.dob = date.today()
            user = super().save(*args,**kwargs)
        else:
            self.dob = date.today()
            user = super().save(*args,**kwargs)
        return user

STATE_CHOICES = [
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CT', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OR', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'),
    ('UT', 'Uttarakhand'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DL', 'Delhi'),
    ('JK', 'Jammu and Kashmir'),
    ('LA', 'Ladakh'),
    ('LD', 'Lakshadweep'),
    ('PY', 'Puducherry'),
]

class Address(models.Model):
    contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    block_number = models.CharField(max_length=10)
    building = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    land_mark  = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pincode = models.PositiveIntegerField(default=666666,blank=True)
    state = models.CharField(max_length=2,choices=STATE_CHOICES)
    # is_selected = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.contributor} | {self.title} '

# duration_choices = [
#     ('1 Month',1),
#     ('3 Month',3),
#     ('6 Month',6),
#     ('12 Month',12),
#     ('24 Month',24)
# ]

# class Group(models.Model):
#     title = models.CharField(max_length=50)
#     moto = models.CharField(max_length=50)
#     contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
#     description = models.CharField(max_length=100)
#     amount = models.IntegerField()
#     created_at = models.DateField(auto_now_add=True)
#     duration = models.CharField(choices=duration_choices)

# class GroupDetails(models.Model):
#     contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
#     group = models.ForeignKey(Group,on_delete=models.CASCADE)
