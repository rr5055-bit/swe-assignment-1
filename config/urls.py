# Root URL configuration
from django.urls import include, path

urlpatterns = [
    path("", include("cv_assignment.urls")),
]
