from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from django.contrib.auth.models import User

# class UserManager(BaseUserManager):

#     use_in_migrations = True

#     def create_user(self, email, full_name, phone, password=None):
#         user = self.model(
#             email=self.normalize_email(email),
#             phone=phone,
#             full_name=full_name,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, full_name, phone, password):
#         user = self.create_user(
#             email,
#             password=password,
#             phone=phone,         
#             full_name=full_name,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, full_name, phone, password):
#         user = self.create_user(
#             email,
#             password=password,
#             phone=phone,
#             full_name= "True",
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# class AppUser(AbstractBaseUser):
#     username = None
#     full_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=13,  unique=True)
#     email = models.EmailField(unique=True)
#     date_create = models.DateField(default=datetime.date.today)

#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = [ 'email','full_name' ]
#     objects = UserManager()
#     def __str__(self):              # __unicode__ on Python 2
#         return self.email + ' ' +self.phone 



CHOISE = (
        ('A', 'Electric Installation'),
        ('B','Laundry'),
        ('C','House Cleaning'),
        ('D','Shopping and Delievery'),
        ('E','Handy Work'),
        ('F','Garden Work'),
        ('G','Interior Painting'),
        ('H','Painting'),
        ('I','Catering'),
        ('J','Helping Carry'),
        ('K','Transportation and Delivery'),
        # ('',''),('',''),('',''),('',''),('',''),('',''),
    )

class Individual(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=1, choices=CHOISE)
    description = models.TextField()
    location = models.CharField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.service+ ' '+ self.location
class Company(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    service = models.CharField(max_length=1, choices=CHOISE)
    location = models.CharField(max_length=500)
    description = models.TextField()
    company_contact = models.CharField(max_length=13)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name+' '+self.service+ ' '+ self.location
    
