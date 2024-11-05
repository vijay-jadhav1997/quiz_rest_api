from django.shortcuts import render
from django.http import JsonResponse

import os
import json
from requests

# Create your views here.
def load_json_data(file_name) :
  file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)

  with open(file_path, 'r') as json_file:
    return json.load(json_file)

def get_mcq(request, name):
  data = load_json_data(f"{name}.json")
  return JsonResponse(data, safe=False)


def get_restaurants_list(request):
  response = requests.get("https://www.swiggy.com/dapi/restaurants/list/v5?lat=12.9351929&lng=77.62448069999999&page_type=DESKTOP_WEB_LISTING")

  return JsonResponse(response.json())


def get_restaurant_data(request, res_id):
  response = requests.get("https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu-true&lat=12.9351929&lng=77.624480699999999&restaurantId=" + res_id)

  return JsonResponse(response.json())
