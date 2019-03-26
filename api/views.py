from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse

def services(request):
    if request.method=='GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data = JSONParser().parse(request.POST)
        serial = ServiceSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        else:
            return JsonResponse(serial.errors, status=400)
def services_details(request, id):
    #instance = get_object_or_404(Service, id=id)
    try:
        instance=Service.objects.get(id=id)
    except Service.DoesNotExit:
        return JsonResponse({'error':'The service you requested does not exits'}, status=404)
    if request.method=='GET':
        serializer = ServiceSerializer(instance)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data = JSONParser().parse(request.PUT)
        serial = ServiceSerializer(instance,data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=200)
        else:
            return JsonResponse(serial.errors, status=400)
    elif request.method=='DELETE':
        instance.delete()
        return HttpResponse(status=204)

def providers(request):
    if request.method=='GET':
        service = Provider.objects.all()
        serializer = ProviderSerializer(Provider, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data = JSONParser().parse(request.POST)
        serial = ProviderSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        else:
            return JsonResponse(serial.errors, status=400)
# class ServiceView(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer      

# class ProviderView(viewsets.ModelViewSet):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer

# class CompanyView(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class RatingCompanyView(viewsets.ModelViewSet):
#     queryset = RatingCompany.objects.all()
#     serializer_class = RatingCompanySerializer

# class RatingProviderView(viewsets.ModelViewSet):
#     queryset = RatingProvider.objects.all()
#     serializer_class = RatingProviderSerializer

# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer