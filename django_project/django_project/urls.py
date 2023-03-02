from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
    path('', include('approvals.urls')),
    path('articles/', include('articles.urls')),
    path('stus/', include('stu.urls')),
    path('pic/', include('pic.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', views.redir),
    path('accounts/login/', views.login),
    path('accounts/auth/', views.auth_view),
    path('accounts/invalid/', views.invalid),
    path('accounts/logout/', views.logout, name="logout"),
    path('accounts/loggedin/', views.loggedin),
    path('accounts/register/', views.register_user),
    path('accounts/register_success/', views.register_success),
    path('accounts/changepassword/', views.change_password),
    path('accounts/index', views.index),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('accounts/index/', views.index),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
