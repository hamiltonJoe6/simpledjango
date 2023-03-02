from django.urls import path
from . import views
from django.urls import path, reverse_lazy

app_name = 'helloview'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('index', views.Anotherindex.as_view(), name='index'),
    #path('index/<int:pk_from_url>/', views.detail, name='detailview'),
    path('index/<int:pk_from_url>/', views.AnotherDetail.as_view(), name='detailview'),
    path('guess', views.guess, name='anotherguess'),
    path('loginview', views.LoginGetView.as_view(), name='loginview'),
    path('main', views.ManualProtect.as_view(), name='main'),
    path('mainview', views.MainView.as_view(), name='mainview'),
    path('create', views.MakeCreate.as_view(), name='create'),
    path('mainview/<int:pk>/update/', views.MakeUpdate.as_view(), name='mainupdate'),
    path('mainview/<int:pk>/delete/', views.MakeDelete.as_view(), name='maindelete'),
    path('something', views.MyView.as_view(template_name='hello/something.html')),
]
