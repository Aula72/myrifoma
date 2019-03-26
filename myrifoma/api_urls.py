from django.urls import path
from .views import (individual, company, company_details,
 individual_details, IndividualDetails, IndividualList, CreateIndividual, 
 CompanyDetails, CreateCompany, CompanyList, CreateUser, UserList, UserDetails, LoginView)
app_name = 'our_api'
urlpatterns = [
    # path('individuals/', individual, name = 'list-individuals'),
    # path('individuals/<int:pk>/', individual_details, name="individual-details"),
    path('individual-new/', CreateIndividual.as_view(), name="new-individual"),
    path('individuals/', IndividualList.as_view(), name = 'list-individuals'),
    path('individuals/<int:pk>/', IndividualDetails.as_view(), name="individual-details"),
    path('company-new/', CreateCompany.as_view(), name='new-companies'),
    path('companies/', CompanyList.as_view(), name='list-companies'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
    path('users/', UserList.as_view(), name="user-list"),
    path('user/<int:pk>/', UserDetails.as_view(), name='user-details'),
    # path('login/', LoginView.as_view(), name="login"),
    path('register/', CreateUser.as_view(), name="create-user"),
]