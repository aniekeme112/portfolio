# core/urls.py
from django.urls import path
from .views import FeaturedProjectListAPIView

urlpatterns = [
    path('projects/', FeaturedProjectListAPIView.as_view(), name='project-list'),
]
