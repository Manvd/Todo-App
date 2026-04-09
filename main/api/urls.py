from django.urls import path
from rest_framework import routers
from .views import TodoViewSet, todo_ui, register

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = router.urls

urlpatterns += [
    path('register/', register, name='register'),
    path('', todo_ui, name='todo-ui'),
]