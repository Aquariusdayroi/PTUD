from django.urls import path
from . import views



urlpatterns = [
     path("", views.home, name = "home"), 
     path("a", views.post_task, name="post_task"),
     path("b", views.update_note, name = 'update_note'),
]
