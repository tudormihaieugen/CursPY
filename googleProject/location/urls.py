app_name = 'location'
from django.urls import path
from location import views


urlpatterns = [
    path('location_index/', views.LocationsList.as_view(), name="location_list"),
    path('createLocation', views.NewLocationView.as_view(), name="create_location"),
    path('updateLocation/<int:pk>/', views.UpdateLocationView.as_view(), name="update_location"),
]
