from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from iha.views import ListIHAView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("iha/", include("iha.urls")),
    path('dashboard/', ListIHAView.as_view(), name='dashboard')




]
