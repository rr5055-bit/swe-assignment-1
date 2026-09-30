# URL routes for the CV app
from django.urls import path

from . import views

app_name = "cv_assignment"

urlpatterns = [
    path("", views.cv_view, name="home"),
    path("section/<str:name>/", views.section_view, name="section"),
]
