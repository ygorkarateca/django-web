from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('page_web/', views.page_web, name='page_web'),
    
]