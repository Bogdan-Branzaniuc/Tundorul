from django.urls import path

from . import views

urlpatterns = [
    path("suggestions", views.SuggestionsView.as_view(), name="suggestions")
]