
from django.urls import path
from .views import (
    DoubtsListView,
    DoubtsDetailView,
    DoubtsCreateView,
    DoubtsUpdateView,
    DoubtsDeleteView
)
from . import views

urlpatterns = [
    path('', DoubtsListView.as_view(), name='doubts-home'),
    path('doubts/<int:pk>/', DoubtsDetailView.as_view(), name='doubts-detail'),
    path('doubts/new/', DoubtsCreateView.as_view(), name='doubts-create'),
    path('doubts/<int:pk>/update/', DoubtsUpdateView.as_view(), name='doubts-update'),
    path('doubts/<int:pk>/delete/', DoubtsDeleteView.as_view(), name='doubts-delete'),
    path('about/', views.about, name='doubts-about'),
]