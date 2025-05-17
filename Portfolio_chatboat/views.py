import json
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .LLM import chat_bot

# Configure logger
logger = logging.getLogger(__name__)

@csrf_exempt
def cheatapi(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            message = data.get('message')

            logger.info(f"Received message: {message}")

            # Call your chatbot function
            response = chat_bot(message)

            logger.info(f"Bot response: {response}")

            return JsonResponse({'response': response})
        else:
            logger.warning(f"Invalid method {request.method} used.")
            return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

    except Exception as error:
        logger.error(f"Error in cheatapi: {error}", exc_info=True)
        return JsonResponse({'error': str(error)}, status=500)


@csrf_exempt
def ping(request):
    logger.info("Ping received")
    return JsonResponse({"status": "ok", "message": "The app is alive!"})
