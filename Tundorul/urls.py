from . import views
from django.urls import path

urlpatterns = [
    path('', views.PopulateUserProfile.as_view(), name='home'),
]
