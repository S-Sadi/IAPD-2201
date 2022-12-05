
from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
    # path('login', views.login, name="login"),
    # path('logout/', views.logout, name="logout"),
    # path('registration/', views.registration, name="registration"),
    # path("", views.home, name="home"),
    # path("index", views.index, name="index"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
