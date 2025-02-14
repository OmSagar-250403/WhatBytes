from django.urls import path, include
from django.contrib.auth import views as auth_views
from app import views
from app.forms import UserLoginForm, ResetPasswordConfirmForm, ResetPasswordForm

urlpatterns = [
    # login view from auth_views with custom login template
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html',
                                                form_class=UserLoginForm,
                                                # True means that if user is already logged in, it will redirect to homepage
                                                redirect_authenticated_user=False), name='login',
         ),

    # logout view from auth_view
    path('logout/', views.logout1, name='logout'),

    # path for register view
    path('register/', views.register, name='register'),

    #path for activate view
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    #path to reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentication/01_password_reset.html',
                                                                 form_class=ResetPasswordForm), name='password_reset'),

    #path to password_reset_done
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/02_password_reset_done.html'), name='password_reset_done'),

    #path to password_reset_confirm
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/04_password_reset_confirm.html',
                                                                                                 form_class=ResetPasswordConfirmForm), name='password_reset_confirm'),

    #path to password reset complete
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/03_password_reset_complete.html'), name='password_reset_complete'),


    # path for homepage where successfull login will redirect
    path('', views.homepage, name='homepage'),

    
    path('profile/', views.profile_view, name='profile'),




]