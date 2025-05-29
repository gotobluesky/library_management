# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from users.views import Users  # Custom register view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/books/', permanent=True)),
    path('books/', include('books.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Django's LoginView
    path('register/', Users.register_view, name='register'),  # Custom register view
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]