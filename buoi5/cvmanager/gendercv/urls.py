from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.form, name = "form"),
     path('cv<int:num>', views.gencv, name = "gencv"),
     path('submit', views.submit_form, name = "submit-form"),     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

