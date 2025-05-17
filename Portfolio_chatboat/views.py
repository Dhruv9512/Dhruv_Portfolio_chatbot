from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .LLM import chat_bot  # your chatbot function

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class CheatAPI(APIView):

    def post(self, request):
        try:
            # Parse JSON body (you can also use request.data directly in DRF)
            data = json.loads(request.body)
            message = data.get('message')

            logger.info(f"Received message: {message}")

            # Call your chatbot function
            response = chat_bot(message)

            logger.info(f"Bot response: {response}")

            # Return Python dict wrapped by DRF Response, NOT JsonResponse
            return Response({'response': response}, status=status.HTTP_200_OK)

        except Exception as error:
            logger.error(f"Error in CheatAPI: {error}", exc_info=True)
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(csrf_exempt, name='dispatch')
class PingView(APIView):

    def get(self, request):
        logger.info("Ping received")
        return Response({"status": "ok", "message": "The app is alive!"}, status=status.HTTP_200_OK)
