from django.shortcuts import render
from django.http import JsonResponse

import requests

# Create your views here.
def get_restaurants_list(request):
  url = "https://www.swiggy.com/dapi/restaurants/list/v5"
  params = {
    "lat": "12.9351929",
    "lng": "77.62448069999999",
    "page_type": "DESKTOP_WEB_LISTING"
  }
  response = requests.get(url, params=params)
  return JsonResponse(response.json())


def get_restaurant_data(request, res_id):
  response = requests.get(f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu-true&lat=12.9351929&lng=77.624480699999999&restaurantId={res_id}")

  return JsonResponse(response.json())

