from django.urls import path
from sci_fi import views

urlpatterns = [
    path("", views.index)
]