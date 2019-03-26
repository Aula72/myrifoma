from rest_framework import serializers
from .models import Service, Provider, Company, RatingCompany, RatingProvider
from django.contrib.auth.models import User
from rest_framework.relations import resolve
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='api:services', lookup_field='id')
    class Meta:
        model = Service
        fields = ['id','name', 'service_type']#, 'url']
        # extra_kwargs = {
        #     'url': {'view_name': 'services', 'lookup_field': 'id'},
        #     'services': {'lookup_field': 'id'}
        # }

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='provider-detail',)
    
    class Meta:
        model = Provider
        extra_kwargs = {
            'url': {'view_name': 'api:providers', 'lookup_field': 'id'},
            'services': {'lookup_field': 'id'},
            'company': {'lookup_field': 'id'},
        }
        fields = ( 'id','phone', 'provider_type', 'description', 'service', 'company', 'location', 'url')
        

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail',)
    class Meta:
        model = Company
        fields = ('id','name', 'location', 'phone', 'tin', 'point_reference', 'company_email', 'url')

class RatingProviderSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rating-provider-detail',)
    class Meta:
        model = RatingProvider
        fields = ('id','provider', 'rate', 'url')

class RatingCompanySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rating-company-detail',)
    class Meta:
        model = RatingCompany
        fields = ('id', 'provider', 'rate')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username',)