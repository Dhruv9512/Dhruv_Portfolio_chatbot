from .LLM import chat_bot
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.http import JsonResponse
from .LLM import chat_bot
# Cheat API view
@csrf_exempt
def cheatapi(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            message = data.get('message')

            print("Received Message:", message)  # ✅ Debug print

            # Chat with the bot
            response = chat_bot(message)
            print("API Response:", response)  # ✅ Debug print
           
            return JsonResponse({'response': response})
    except Exception as error:
        print("Error:", error)  
        return JsonResponse({'error': str(error)})
    
def ping(request):
    return JsonResponse({"status": "ok", "message": "The app is alive!"})