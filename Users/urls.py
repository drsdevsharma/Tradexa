from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .forms import LoginForm , changePasswordForm,ForgotPasswordForm,NewPasswordConfirmForm


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.RegisterUser , name = 'registeration'),
    path('accounts/login/' , auth_views.LoginView.as_view(template_name = 'login.html',authentication_form = LoginForm) , name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page  = 'home') , name = 'logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name = 'change_password.html',form_class = changePasswordForm,success_url ='/'), name = 'change_password'),
    path('forgot_password/',auth_views.PasswordResetView.as_view(template_name = 'forgot_password.html',email_template_name = 'password_reset_email.html',form_class = ForgotPasswordForm,subject_template_name = 'subject.txt') , name = 'forgot_password'),
    path('forgot_password/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'forgot_password_done.html'), name = 'password_reset_done'),
    path('forgot_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'forgot_password_confirm.html',form_class = NewPasswordConfirmForm,success_url='/accounts/login/'),name='password_reset_confirm'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('addblog/', views.AddPost, name = 'addpost'),
    path('update/<int:id>/', views.UpdatePost, name = 'updatepost'),
    path('delete/<int:id>/', views.DeletePost, name = 'delete'),
    

    ]