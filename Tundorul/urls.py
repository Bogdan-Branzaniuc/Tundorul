from . import views
from django.urls import path

urlpatterns = [
    path('', views.PopulateUser.as_view(), name='home'),
]
