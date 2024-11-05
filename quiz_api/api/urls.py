from django.urls import path
from . import views


urlpatterns = [
  path('<str:name>', views.get_mcq, name="mcq"),
  path('api/res_list/', views.get_restaurants_list, name="get_restaurants_list"),
  path('api/res/<int:res_id>', views.get_restaurant_data, name="get_restaurant_data"),
]
