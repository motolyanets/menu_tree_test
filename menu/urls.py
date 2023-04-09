from django.urls import path
from .views import *


urlpatterns = [
    path('<str:menu_url>/<str:path_url>/', menu),
]
