from django.db import models



class Service(models.Model):
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
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=1, choices=CHOISE, blank=True)
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    tin = models.CharField(max_length = 15, verbose_name='Tax Identification Number')
    point_reference = models.CharField(max_length = 10)
    company_email = models.EmailField()
    
    def __str__(self):
        return self.name
class Provider(models.Model):
    CHOOSE = (('I', 'individual'), ('C', 'company'))
    service = models.ManyToManyField(Service, related_name='service')
    company = models.ForeignKey(Company, blank=True, null = True, on_delete=models.CASCADE, related_name='company')
    provider_type = models.CharField(max_length = 1, choices=CHOOSE)
    description = models.TextField(blank=True)
    location = models.CharField(max_length = 100, blank = True)
    phone = models.CharField(max_length = 100)
    def __str__(self):
        return self.phone

class RatingProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    #user
    rate = models.IntegerField()
    def __str__(self):
        return str(self.rate)

class RatingCompany(models.Model):
    provider = models.ForeignKey(Company, on_delete=models.CASCADE)
    #user
    rate = models.IntegerField()
    def __str__(self):
        return str(self.rate)
