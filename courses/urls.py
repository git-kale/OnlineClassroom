
from django.urls import path
from .views import (
    CoursesListView,
    CoursesDetailView,
    CoursesCreateView,
    CoursesUpdateView,
    CoursesDeleteView
)
from . import views

urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='courses-home'),
    path('courses/<int:pk>/', CoursesDetailView.as_view(), name='courses-detail'),
    path('courses/new/', CoursesCreateView.as_view(), name='courses-create'),
    path('courses/<int:pk>/update/', CoursesUpdateView.as_view(), name='courses-update'),
    path('courses/<int:pk>/delete/', CoursesDeleteView.as_view(), name='courses-delete'),
    path('courses/about', views.about, name='courses-about'),
    path('course/added_to_course',views.accepted, name='course-added'),
    path('',views.homepage,name='classroom-home')
]