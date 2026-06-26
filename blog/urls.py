from django.urls import path
from .views import home,post_detail

urlpatterns = [
    path('home/', home, name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]