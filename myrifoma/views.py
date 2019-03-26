from django.shortcuts import render, get_object_or_404
from myrifoma.models import Individual, Company
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from myrifoma.serializers import (IndividualSerializer, CompanySerializer,
UserSerializer)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from api.models import Provider

def index(request):

    return render(request, 'myrifoma/index.html', {'values':56})

def providers_page(request, service_type):
    # providers = Provider.objects.get()
    pass
def individual(request):
    MAX_OBJECTS = 20
    individuals = Individual.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list(individuals.values(
            "id","created_by__username", "service", "description", "location"
        ))
    }
    return JsonResponse(data)

def individual_details(request, pk):
    individual = get_object_or_404(Individual, pk=pk)
    data = {
        "results":{
            "id": pk,
            "created_by": individual.created_by.username,
            "service": individual.service,
            "description": individual.description,
            "location": individual.location
        }
    }
    return JsonResponse(data)

def company(request):
    MAX_OBJECTS = 20
    companies = Company.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list(companies.values(
            "id", "create_by", "name", "service", "description", "location"
        ))
    }
    return JsonResponse(data)

def company_details(request, pk):
    pass


"""this is now young """
# class IndividualList(APIView):
#     def get(self, request):
#         individuals = Individual.objects.all()[:20]
#         data = IndividualSerializer(individuals, many=True).data
#         return Response(data)

# class IndividualDetails(APIView):
#     def get(self, request, pk):
#         individual = get_object_or_404(Individual, pk=pk)
#         data = IndividualSerializer(individual).data
#         return Response(data)

## these are imporived views
class CreateIndividual(generics.CreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class IndividualList(generics.ListCreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class IndividualDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class CreateCompany(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CreateUser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return  Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
                # in urls.py# ...from .apiviews importPollViewSet, ChoiceList, CreateVote, UserCreate, LoginViewurlpatterns = [path("login/", LoginView.as_view(), name="login"),# ...]Do a POST with a correct username and password, and you will get a response like this.34Chapter 7.  Access Control
