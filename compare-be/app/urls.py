from django.urls import path
from . import views

urlpatterns = [
    path('claudeTxtGen/', views.claude_txt_generation, name="claude_TxtGen"),
    path('openaiTxtGen/', views.openAI_TxtGen, name='openai_TxtGen'),
    path('geminiTxtGen/', views.gemini_TxtGen, name='gemini_TxtGen'),
]