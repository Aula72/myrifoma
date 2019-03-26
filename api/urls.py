from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter 
# router = DefaultRouter()
# router.register('services', my_services, basename='services')
# router.register('providers', ProviderView)
# router.register('companies', CompanyView)
# router.register('company-ratings', RatingCompanyView)
# router.register('provider-ratings', RatingProviderView)
# router.register('user', UserView)
app_name = "Api"
urlpatterns = [
    # path('', include(router.urls), name='item-list'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('api/', include('api.urls', namespace="ApiKey")),
    path('services/', services, name="services"),
    path('services/<int:id>/', services_details, name="services-details"),
    path('providers/', providers, name="providers"),
]
