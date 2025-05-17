import json
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .LLM import chat_bot  # your chatbot function

# Configure logger
logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class CheatAPI(APIView):

    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data.get('message')

            logger.info(f"Received message: {message}")

            # Call your chatbot function
            response = chat_bot(message)

            logger.info(f"Bot response: {response}")

            return JsonResponse({'response': response})

        except Exception as error:
            logger.error(f"Error in CheatAPI: {error}", exc_info=True)
            return JsonResponse({'error': str(error)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class PingView(APIView):

    def get(self, request):
        logger.info("Ping received")
        return JsonResponse({"status": "ok", "message": "The app is alive!"}, status=200)
