from rest_framework import viewsets
from .models import HighSchool, Review
from .serializers import HighSchoolSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

class HighSchoolViewSet(viewsets.ModelViewSet):
    queryset = HighSchool.objects.all()
    serializer_class = HighSchoolSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create_user(
        username=data['username'],
        password=data['password']
    )
    return Response({'id': user.id})

@api_view(['POST'])
def user_login(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'})
    else:
        return Response({'message': 'Invalid credentials'}, status=400)
