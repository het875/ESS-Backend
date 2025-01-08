from rest_framework import serializers
from .models import Category, Question, Answer

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'category', 'category_name', 'question_text', 'created_at', 'updated_at']

# Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question_text', read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'question_text', 'employee_id', 'answer_text', 'submitted_at']
