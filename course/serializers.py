from .models import Course,Review
from rest_framework import serializers
from user.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    Instructor = UserSerializer()
    class Meta :
        model = Course
        fields = "__all__"
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields ="__all__"