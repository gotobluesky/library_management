from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render

class Users(APIView):
    permission_classes = [AllowAny]  # Allow access without auth

    def login_view(request):
        return render(request, 'login.html')
    
    def get(self, request):
        # Handle login logic
        # For JWT, typically you just call TokenObtainPairView
        # But if you want custom, implement here
        pass