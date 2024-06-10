from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CourseView,ReviewView,InstructorCoursesView

router = DefaultRouter()
router.register(r'courses',CourseView)
router.register(r"reviews",ReviewView)

urlpatterns = [
    path("",include(router.urls)),
    path('instructor/courses/', InstructorCoursesView.as_view(), name='instructor-courses'),
]