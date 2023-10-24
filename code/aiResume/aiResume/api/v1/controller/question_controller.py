from django.http import HttpResponseNotFound, JsonResponse
from django.views import View

class QuestionController(View):

    def post(self, request, *args, **kwargs):
        # Handle POST requests here
        return JsonResponse("This is a response to a POST request.")

    def http_method_not_allowed(self, request, *args, **kwargs):
        # Return a 404 Not Found response for other HTTP methods
        return HttpResponseNotFound("Page not found")