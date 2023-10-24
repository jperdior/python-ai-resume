from rest_framework import serializers

from infrastructure.models import Question

class PostQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'answer')

class GetQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer')