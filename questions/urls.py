from django.urls import path
from questions.views import create_question


urlpatterns = [
  path("questions/",create_question,name="create_question") 
]