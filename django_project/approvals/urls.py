from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('notification', views.index, name='index'),
    path('notification/<int:notification_id>', views.show_notification, name='show_notification'),
    path('delete/<int:notification_id>', views.delete_notification, name='delete_notification')

]
