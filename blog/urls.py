from django.urls import path
from .views import home,post_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', home, name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
]