from rest_framework import viewsets
from .models import Category, Question, Answer
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from .models import Answer
from .serializers import AnswerSerializer
from .utils import export_answers_to_excel
import os

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Question ViewSet
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Answer ViewSet
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ExportAnswersToExcelView(APIView):
    def get(self, request):
        # Fetch all answers
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)

        # Export to Excel
        file_path = "answers.xlsx"
        export_answers_to_excel(serializer.data, file_path=file_path)

        # Serve the file as a response
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, "rb"), as_attachment=True, filename=file_path)
            return response
        else:
            return Response({"error": "File not found"}, status=500)
