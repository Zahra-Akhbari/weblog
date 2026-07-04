from . import  views
from django.urls import path
from .views import home, post_detail, Tag_posts
from django.contrib.auth import views as auth_views
from .views import register
from .views import category_posts ,dashboard

urlpatterns = [
    path('home/', home, name='home'),
    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("register/",register, name="register"),
    path("category/<slug:slug>/",category_posts,name="category_posts"),
    path("tag/<slug:slug>/",Tag_posts,name="tag_posts"),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/dashboard/", dashboard, name="dashboard"),


    path('posts/<slug:slug>/', post_detail, name='post_detail'),


]