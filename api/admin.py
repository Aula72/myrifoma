from django.contrib import admin
from .models import Service, Company, RatingCompany, RatingProvider, Provider

admin.site.register(Service)
admin.site.register(Company)
admin.site.register(Provider)
admin.site.register(RatingProvider)
admin.site.register(RatingCompany)
# Register your models here.
