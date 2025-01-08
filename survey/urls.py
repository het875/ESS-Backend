from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, QuestionViewSet, AnswerViewSet, ExportAnswersToExcelView

# Initialize the router
router = DefaultRouter()

# Register viewsets with the router
router.register('categories', CategoryViewSet, basename='category')
router.register('questions', QuestionViewSet, basename='question')
router.register('answers', AnswerViewSet, basename='answer')

# Define your custom URLs
urlpatterns = router.urls + [
    path('export-answers/', ExportAnswersToExcelView.as_view(), name='export-answers'),
]

