from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
