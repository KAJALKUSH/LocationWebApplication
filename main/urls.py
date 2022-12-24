from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.route_view, name="route"),
    path('map', views.map_view, name="map"),
    ]