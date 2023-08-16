from django.urls import path
from .views import cities_income

app_name = 'cities_income'

urlpatterns = [
    path('', cities_income, name='cities_income')
]
