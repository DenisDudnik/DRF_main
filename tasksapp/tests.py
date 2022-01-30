import json  # нужен для чтения содержимого ответа от сервера
from django.test import TestCase  # базовый класс для создания Django-теста
from rest_framework import status  # содержит константы для ответов сервера
from rest_framework.test import (
    APIRequestFactory,  # фабрика для создания запросов
    force_authenticate,  # функция для авторизации пользователя
    APIClient,  # клиент для удобной отправки REST-запросов
    APISimpleTestCase,  # класс для создания простых test cases
    APITestCase,  # класс для создания test cases для REST API
)

# from mixer.backend.django import mixer  # библиотека для генерации тестовых данных
from django.contrib.auth.models import User  # модель пользователя
from .views import ProjectModelViewSet, TODOModelViewSet
from .models import TODO, Project

# Create your tests here.


class TestProjectModelViewSet(TestCase):
    def test_get_project_list(self):
        factory = APIRequestFactory()
        request = factory.get("/api/projects/")
        view = ProjectModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_TODO_list(self):
        factory = APIRequestFactory()
        request = factory.get("/api/TODO/")
        view = TODOModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
