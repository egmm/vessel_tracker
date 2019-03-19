from django.urls import path, re_path

from . import views

urlpatterns = [
    path('ships/', views.ships_list, name='ships_list'),
    re_path(r'^positions/(?P<imo>[0-9]+)/$', views.ships_position, name='ships_position'),
]