from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.SentenceView.as_view(), name = 'analyze'),
]
