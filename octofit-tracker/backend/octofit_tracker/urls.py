from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_root, name='api_root'),
]
