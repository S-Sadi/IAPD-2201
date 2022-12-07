
from django.urls import path
from .import views


urlpatterns = [
    path("", views.home, name="home"),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registration/', views.registration, name="registration"),
    path("index", views.index, name="index"),
    path("product/<int:id>/ ", views.product, name="product"),
    path("search=<str:pk>", views.search, name="search"),
]
