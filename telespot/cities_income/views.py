from django.shortcuts import render
from .models import ActualProfit, Cities, PlanProfit
from .forms import CityForm


def cities_income(request):
    cities = Cities.objects.prefetch_related('plan_profit', 'actual_profit').all()
    form = CityForm(request.GET or None)
    if form.is_valid():
        city_name = form.cleaned_data['city_name']
        cities = city_name
    context = {
        'cities': cities,
        'forms': form
    }
    return render(request, 'cities_income.html', context)
