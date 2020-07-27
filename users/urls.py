
from . import views
from django.urls import path


urlpatterns = [
    path('current/', views.GetUser.as_view())
]
