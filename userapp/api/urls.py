from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from userapp.api import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/',views.user_registration_view,name='register'),
    path('text/',views.Textview.as_view(),name='text'),
    

]