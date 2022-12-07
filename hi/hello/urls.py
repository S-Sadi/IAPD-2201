
from django.urls import path
from .import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registration/', views.registration, name="registration"),
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("product/<int:id>/ ", views.product, name="product"),
]
