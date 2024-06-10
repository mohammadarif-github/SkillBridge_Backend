from django.shortcuts import render,redirect
from .models import Course,Review
from .serializers import CourseSerializer,ReviewSerializer
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.core.exceptions import PermissionDenied


from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied


from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            serializer.save(Instructor=user)
        else:
            raise PermissionDenied("You do not have permission to perform this action.")

    def perform_update(self, serializer):
        user = self.request.user
        course_instructor = self.get_object().Instructor
        if user.is_superuser or user.is_staff or user == course_instructor:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to perform this action.")

    def perform_destroy(self, instance):
        user = self.request.user
        course_instructor = instance.Instructor
        if user.is_superuser or user.is_staff or user == course_instructor:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to perform this action.")

class InstructorCoursesView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(Instructor=self.request.user)

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        user = self.request.user
        reviewer = self.get_object().user
        if user.is_superuser or user.is_staff or user == reviewer:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to perform this action.")

    def perform_destroy(self, instance):
        user = self.request.user
        reviewer = instance.user
        if user.is_superuser or user.is_staff or user == reviewer:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to perform this action.")

