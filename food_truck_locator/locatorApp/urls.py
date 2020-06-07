from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("response", views.nearest_form, name="nearest_form"),
    path("<str:latitude>/<str:longitude>/<int:n>", views.nearest, name="nearest"),
    path("api/<str:latitude>/<str:longitude>/<int:n>",views.nearest_api)
]