from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'group', GroupViewSet)
router.register(r'add', GroupRoleViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('changePassword/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
    path('upload/', picUploadView.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/facebook/', FacebookLogin.as_view(), name='fb_login')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)