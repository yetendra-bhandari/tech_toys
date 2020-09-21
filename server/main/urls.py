from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
    path('storage/<directory>/<filename>/', views.showImage, name='showImage')
]
