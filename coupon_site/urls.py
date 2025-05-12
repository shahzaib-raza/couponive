from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from coupons import views as coupons_views
import django
from django.urls import re_path as url

urlpatterns = urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', coupons_views.logout_view, name='logout'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', coupons_views.register, name='register'),
    path('store/<int:store_id>/', coupons_views.store_detail, name='store_detail'),
    path('', include('coupons.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {
    'document_root': settings.MEDIA_ROOT}),]