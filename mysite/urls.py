from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logut/$', views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'', include('blog.urls')),

    ]
