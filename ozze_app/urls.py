from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.start),
    path('main/', views.start),
    re_path('register/', views.RegisterForm.as_view()),
    re_path('auth/', views.AuthForm.as_view()),
    re_path('logout/', views.LogoutForm.as_view()),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),\

    re_path('account/', views.Account.as_view()),
    re_path('changeAccData/',views.ChangeAccData.as_view()),
    re_path('coat_catalog/', views.CoatCatalog.as_view()),
    re_path('dress_catalog/', views.DressCatalog.as_view()),
    re_path('parka_catalog/', views.ParkaCatalog.as_view()),
    re_path('facemask_catalog/', views.FaceMaskCatalog.as_view()),
    re_path('sale_catalog/', views.OnSaleCatalog.as_view()),
    re_path('catalog/', views.AllCatalog.as_view()),
    re_path('size_chart/', views.size_chart),
    path('coat/<int:pk>/', views.coat_detail, name='coat_detail'),
    path('dress/<int:pk>/', views.dress_detail, name='dress_detail'),
    path('parka/<int:pk>/', views.parka_detail, name='parka_detail'),
    path('face_mask/<int:pk>/', views.face_mask_detail, name='face_mask_detail'),

    path('cart/', views.cart_view),
    re_path('cart_add/', views.add_to_cart),
    re_path('cart_del/', views.del_from_cart),




]
