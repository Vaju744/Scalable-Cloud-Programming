from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import submit_feedback, get_feedback
from .views import get_location_coordinates
from .views import show_map_form
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login_register/', views.login_register, name='login_register'),
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('customerregister/',views.customerregister, name='customerregister'),
    path('customerdashboard/',views.customerdashboard, name='customerdashboard'),
    path('logout/', views.customlogout, name='customlogout'),
    
    path('api/feedback/', get_feedback, name='get_feedback'),
    path('api/feedback/submit/', submit_feedback, name='submit_feedback'),

    path('vehicle_index/',views.vehicle_index, name='vehicle_index'),
    path('vehicle_create/',views.vehicle_create, name='vehicle_create'),
    path('vehicle_edit/<int:id>/',views.vehicle_edit, name='vehicle_edit'),

    path('driver_index/',views.driver_index, name='driver_index'),
    path('driver_create/',views.driver_create, name='driver_create'),

    path('consignment_index/',views.consignment_index, name='consignment_index'),
    path('consignment_create/',views.consignment_create, name='consignment_create'),
    path('consignment/edit/<int:id>/', views.consignment_edit, name='consignment_edit'),
    path('consignment/<int:id>/', views.consignment_show, name='consignment_show'),

    path('admindashboard/',views.admindashboard, name='admindashboard'),
    path('all_vehicle/',views.all_vehicle, name='all_vehicle'),
    path('all_driver/',views.all_driver, name='all_driver'),
    path('all_consignment/',views.all_consignment, name='all_consignment'),
    path('report/',views.report, name='report'),
    path('api/location/', get_location_coordinates, name='get_location_coordinates'),
    
    path("map-form/", views.show_map_form, name="map-form"),
    path("map/", views.map_view, name="map-page"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)