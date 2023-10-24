from django.urls import path
from api.presentation.v1.controller.question_controller import QuestionController


urlpatterns = [
    path("question/", QuestionController.as_view(), name="question-api"),
]
