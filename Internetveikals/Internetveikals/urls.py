"""Internetveikals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from majaslapa.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from majaslapa import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.static import serve


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls, name='admin'),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon/favicon.ico'))),
    path('', views.sakums.as_view(), name='sakums'),
    path('account/', account, name='account'),
    path('account/order/', order, name='order'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('account/login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('category/<slug:post_slug>', category.as_view(), name='category'),
    path('logout/', logoutUser, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('shopingcart/', cart, name='cart'),
    path('product/<str:slug_url>', product_info, name='product'),
    path('search/', search, name='search'),
    path('instruction/', instruction, name='instruction'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

    path('password/', PasswordsChangeView.as_view(
        template_name='majaslapa/change-password.html'), name='password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='majaslapa/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='majaslapa/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='majaslapa/password_reser_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='majaslapa/password_reser_done.html'), name='password_reset'),
    path('<str:slug_url>/create-checkout-session/',
         views.create_checkout_session),
    path('config/', views.stripe_config),
    path('webhook/', views.stripe_webhook),
    path('account/delete-user/', views.deleteuser, name='deleteuser'),
    path('/create-checkout-session/', views.create_checkout_sessionn),

    path('i18n/', include('django.conf.urls.i18n')),


] + i18n_patterns(
    path('admin/', admin.site.urls, name='admin'),
    path('', views.sakums.as_view(), name='sakums'),
    path('shopingcart/', cart, name='cart'),
    path('account/', account, name='account'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('account/login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('category/<str:slug_url>', category.as_view(), name='category'),
    path('logout/', logoutUser, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('account/order/', order, name='order'),
    path('password/', PasswordsChangeView.as_view(
        template_name='majaslapa/change-password.html'), name='password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='majaslapa/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='majaslapa/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='majaslapa/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='majaslapa/password_reset_complete.html'), name='password_reset_complete'),
    path('<str:slug_url>/create-checkout-session/',
         views.create_checkout_session),
    path('search/', search, name='search'),
    path('webhook', views.stripe_webhook),  # new
    path('<str:slug_url>/success/', SuccessView.as_view(), name='success'),
    path('<str:slug_url>/cancelled/', CancelledView.as_view(), name='cancel'),
    path('/create-checkout-session/', views.create_checkout_sessionn),
    path('product/<str:slug_url>', product_info, name='product'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
SOCIAL_AUTH_URL_NAMESPACE = 'social'

handler404 = 'majaslapa.views.eror404'
handler500 = 'majaslapa.views.handle_server_error'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
