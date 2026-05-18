
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [

    path('regional_technologies/',views.regional_technologies),
    path('admin_login_page/',views.admin_login_page),
    path('admin_login_api/',views.admin_login_api),
    path('admin_logout_api/',views.admin_logout_api),
    path(
        'admin_delete_enquiry/<int:id>/',
        views.admin_delete_enquiry
    ),
    path('home/',views.home),
    path('contact_list/',views.contact_list),
    path('admindashboard',views.admindashboard),
    path('contact_api_get',views.contact_api_get),
    path('contact_api',views.contact_api),
    path('careerpage/',views.career_page),
    path('add_career/',views.add_career),
    path('get_careers/',views.get_careers),
    path('career_page/',views.career_page),
    path('delete_career/<int:id>/', views.delete_career),
    path('public_get_careers/',views.public_get_careers),






]
