from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls',namespace='account')),
    path('',views.homepage,name='home')
]
