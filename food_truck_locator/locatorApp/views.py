from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from .models import FoodTruckInfo

from django.db.models import F

import math

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    context = {
        "food_trucks": FoodTruckInfo.objects.all()
    }
    return render(request,"locatorApp/index.html", context)


'''
Function to generate a list of n nearest food trucks. Ideally, I would have placed
this in a separate package and imported it.
'''
def compute_nearest(latitude, longitude, n):

    lati = float(latitude)
    longi = float(longitude)

    truck_mapping = {}
    all_trucks = FoodTruckInfo.objects.all()

    if n > len(all_trucks):
        n == len(all_trucks)

    for truck in all_trucks:
        x_squared = pow(truck.longitude - longi,2)
        y_squared = pow(truck.latitude - lati,2)
        distance = math.sqrt(x_squared+y_squared)
        truck_mapping[truck.locationId] = distance
    
    # sort by distance: return tuples mapping location ids to distances
    sorted_trucks = sorted(truck_mapping.items(), key=lambda item: item[1])[:n]

    loc_ids = []
    for element in sorted_trucks:
        loc_ids.append(element[0])
    
    return loc_ids

# Return nearest 5 food trucks from user input on index page
def nearest_form(request):

    latitude = float(request.POST.get("latitude")) 
    longitude = float(request.POST.get("longitude"))

    loc_ids = compute_nearest(latitude, longitude, 5)

    # compute distance squared to display food trucks ordered by distance
    nearest_trucks = FoodTruckInfo.objects.filter(locationId__in=loc_ids).annotate(
    distance=pow((latitude - F('latitude')),2) + pow((longitude - F('longitude')),2))

    context = {
        "food_trucks": nearest_trucks.order_by('distance')
    }
    
    return render(request,"locatorApp/nearest.html", context)

# Return nearest by typing in url
def nearest(request, latitude, longitude, n):

    loc_ids = compute_nearest(latitude, longitude, n)

    # compute distance squared to display food trucks ordered by distance
    nearest_trucks = FoodTruckInfo.objects.filter(locationId__in=loc_ids).annotate(
    distance=pow((latitude - F('latitude')),2) + pow((longitude - F('longitude')),2))

    context = {
        "food_trucks": nearest_trucks.order_by('distance')
    }
    
    return render(request,"locatorApp/nearest.html", context)

'''
Simple api allowing endpoints to return nearest n restaurants for a given set of 
coordinates in JSON format. Would have used Django REST api library, but I really 
don't want users doing anything more than GET requests (NO POST, DELETE, etc., since 
the food truck data should not be updated by users)
'''
def nearest_api(request, latitude, longitude, n):
    
    loc_ids = compute_nearest(latitude, longitude, n)

    # compute distance squared to display orderd by distance
    nearest_trucks = FoodTruckInfo.objects.filter(locationId__in=loc_ids).annotate(
    distance=pow((latitude - F('latitude')),2) + pow((longitude - F('longitude')),2))
    
    data = {"results": list(nearest_trucks.order_by('distance').values("name","address","foodItems","distance"))}
    
    return JsonResponse(data)


