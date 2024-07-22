from django.shortcuts import render
from django.http import JsonResponse
import os
import json

# Create your views here.
def load_json_data(file_name) :
  file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)

  with open(file_path, 'r') as json_file:
    return json.load(json_file)

def getMCQ(request, name):
  data = load_json_data(f"{name}.json")
  return JsonResponse(data, safe=False)