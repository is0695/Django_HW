from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    file_csv = settings.BUS_STATION_CSV
    with open(file_csv, 'r', encoding='utf-8') as f:
        stations = []
        data = csv.DictReader(f)
        for i in data:
            stations.append(i)
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(stations, 10)
        page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
