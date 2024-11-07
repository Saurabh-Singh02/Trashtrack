from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('map/', views.map_view, name='map_view'),  # Map route
    path('smart-bins/', views.smart_bins, name='smart_bins'),
    path('tracking/', views.tracking, name='tracking'),
    path('dumping-area/', views.dumping_area, name='dumping_area'),
    path('company-portal/', views.company_portal, name='company_portal'),
    path('company-portal/signup/', views.company_signup, name='company_signup'),
]
