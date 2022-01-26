from django.urls import path
from . import views

urlpatterns = [
    path('xmltodb/',views.xmltodb),
    path('menu/green/',views.menu_green),
    path('menu/ikuta/',views.menu_ikuta),
    path('message/',views.message)
]
