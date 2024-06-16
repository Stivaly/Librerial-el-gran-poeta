from django.contrib import admin
from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.redirect_to_login),  
    re_path('admin/', admin.site.urls),
    re_path('api-auth/', include('rest_framework.urls')),
    re_path('login/', views.login),
    re_path('signup/', views.signup),
    re_path('test_token/', views.test_token),
]
