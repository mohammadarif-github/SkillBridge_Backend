from django.urls import path,include
from .views import RegistrationView,LoginView,LogoutView,ProfileView,AllProfile
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/token/', LoginView.as_view(), name='login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("user/logout",LogoutView.as_view(),name="logout"),
    path("user/register",RegistrationView.as_view(),name="register"),
    path("user/profile/<int:pk>/",ProfileView.as_view(),name="profile"),
    path("users/",AllProfile.as_view(),name="profile"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]