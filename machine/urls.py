from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('report/<int:pk>', views.report, name='report'),
    path('report_create/', views.report_create, name='report_create'),
    
]