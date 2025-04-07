from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import api_view
import anthropic
import os
from openai import OpenAI
from dotenv import load_dotenv
from google import genai

load_dotenv()
claude_key = os.environ.get("CLAUDE_API_KEY")
gemini_key = os.environ.get("GEMINI_API_KEY")
openai_key = os.environ.get("OPENAI_API_KEY")



@api_view(['POST'])
def claude_txt_generation(request):
    try:
        if request.method == 'POST':
            data = request.data
            input_prompt = data['prompt']

            client = anthropic.Client(api_key=claude_key)
            response = client.messages.create(
                max_tokens=500,
                messages=[
                    {"role": "user", "content": input_prompt}
                ],
                model="claude-2.1",
            )
            generated_text = response.content[0].text.strip()

            return JsonResponse({"res": generated_text})
        else:
            return JsonResponse({'error': "error"})
    except Exception as e:
        return JsonResponse({"error": str(e)})


@api_view(['POST'])
def openAI_TxtGen(request):
    try:
        if request.method == 'POST':

            client = OpenAI(api_key=openai_key)
            # prompt = request.POST.get('prompt')
            data = request.data
            prompt =data['prompt']

            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {
                        'role': 'user', 'content': prompt
                    }
                ]
            )
            generated_text = response.choices[0].message.content
            return JsonResponse({"res": generated_text})
        else:
            return JsonResponse({'error': "error"})
    except Exception as e:
        return JsonResponse({"error": str(e)})

@api_view(['POST'])
def gemini_TxtGen(request):
    try:
        if request.method == 'POST':
            client = genai.Client(api_key=gemini_key)

            data = request.data
            prompt = data['prompt']
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )
            return JsonResponse({"res": response.text})
        else:
            return JsonResponse({'error': "error"})
    except Exception as e:
        return JsonResponse({"error": str(e)})

