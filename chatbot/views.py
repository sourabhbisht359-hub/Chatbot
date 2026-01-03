from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import json
from django.shortcuts import render

def chat_view(request):
    return render(request, 'chatbot/chat.html')

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        # Simple chatbot logic
        if "hello" in user_message.lower():
            bot_response = "Hi there!"
        elif "how are you" in user_message.lower():
            bot_response = "I'm just a bot, but I'm doing great!"
        else:
            bot_response = "I'm not sure how to respond to that."

        # Save the chat message
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)

        return JsonResponse({'response': bot_response})
