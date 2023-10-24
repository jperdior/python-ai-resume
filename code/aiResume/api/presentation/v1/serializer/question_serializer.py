from rest_framework import serializers

from api.infrastructure.storage.models import QuestionModel

class PostQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('question', 'answer')

class GetQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('id', 'question', 'answer')