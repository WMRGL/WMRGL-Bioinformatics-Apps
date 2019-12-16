from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('delete/<int:pk>', views.AppDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>', views.AppEditView.as_view(), name='edit')
]
