from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetMoviesView.as_view()),
]