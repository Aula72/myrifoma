from rest_framework import serializers
from myrifoma.models import Individual, Company
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual  
        url = serializers.HyperlinkedRelatedField(many=True, view_name='our_app:individual-details', read_only=True)      
        fields = ['id', 'service', 'description', 'location', 'created_by', 'create_at']
        extra_kwargs = {
            'url': {'view_name':'list-individuals'},
        }
        #fields = '__all__'
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'service', 'description', 'location', 'company_contact', 'create_by', 'create_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password':{'write_only':True}}
        def create(self, validated_data):
            user = User(
                email = validated_data['email'],
                username = validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user