from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

app_name = 'Stu'

urlpatterns = [
    path('', views.index, name='index'),
    path('display', views.display, name='display'),
    path('extends', views.extends, name='extends'),
    path('list/', views.stu_list, name='list'),
    path('create/', views.stu_create, name='create'),
    path('detailpost/<int:id>', views.stu_detail, name='detailpost'),
    path('detailpost/<slug>', views.stu_detail, name='detailpost'),
    path('update/<int:id>', views.stu_update, name='update'),
    path('delete/<int:id>', views.stu_delete, name='delete'),
    path('comment/<int:article_id>', views.add_comment, name='comment'),
    path('like/<int:id>', views.like, name='like'),
    path('jsonlist', views.jsonlist, name='jsonlist')
]
