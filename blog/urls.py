from django.urls import path
from .views import home,post_detail
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('home/', home, name='home'),
    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("register/",register, name="register"),

    path('posts/<slug:slug>/', post_detail, name='post_detail'),

]