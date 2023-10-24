from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponseNotFound, JsonResponse
from api.application.handler.question_handler import QuestionHandler
from api.presentation.v1.serializer.question_serializer import PostQuestionSerializer
from api.dependency_injection import QUESTION_HANDLER

class QuestionController(APIView):

    def __init__(self):
        self.question_handler = QUESTION_HANDLER

    def post(self, request, *args, **kwargs) -> Response:
        serializer = PostQuestionSerializer(data=request.data)

        if serializer.is_valid():
            question = serializer.validated_data.get('question')
            print(question)
            self.question_handler.create_question(question)
            return Response("This is a response to a POST request.", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def http_method_not_allowed(self, request, *args, **kwargs) -> Response:
        # Return a 404 Not Found response for other HTTP methods
        return HttpResponseNotFound("Page not found")
    