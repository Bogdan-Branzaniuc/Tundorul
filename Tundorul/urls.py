from . import views
from django.urls import path

urlpatterns = [
    path('', views.MyView.as_view(), name='home'),
]
