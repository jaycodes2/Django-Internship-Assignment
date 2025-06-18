from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import send_welcome_email

import logging
logger = logging.getLogger(__name__)




@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public endpoint, accessible by anyone."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}. You are authenticated!"})


  # 👈 import the celery task

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)

    # ✅ Call Celery task in background
    send_welcome_email.delay(user.email)
    logger.info(f"📧 Sending welcome email to {user.email}")

    return Response({'message': 'User registered successfully'})
