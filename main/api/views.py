from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from todo.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username', '').strip()
    password = request.data.get('password', '').strip()

    if not username or not password:
        return Response({'error': 'username and password are required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'username already taken'}, status=400)

    if len(password) < 6:
        return Response({'error': 'password must be at least 6 characters'}, status=400)

    User.objects.create_user(username=username, password=password)
    return Response({'message': 'account created successfully'}, status=201)


def login_ui(request):
    return render(request, 'login.html')


def todo_ui(request):
    return render(request, 'todo.html')