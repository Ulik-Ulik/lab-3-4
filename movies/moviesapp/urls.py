from django.urls import path
from . import views

urlpatterns = [
    path("", views.MaviesView.as_view()),
]