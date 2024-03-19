from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.form, name = "form"),
     path('cv<int:num>', views.gencv, name = "gencv"),
     path('submit', views.submit_form, name = "submit-form"),  
     path('cvs/', views.list_cv, name='list-cv'),   
     path('cvs/<int:cv_id>/', views.cv_detail, name='cv-detail'),
      path('cvs/delete/<int:cv_id>/', views.cv_delete, name='cv-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

