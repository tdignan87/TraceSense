from django.urls import path
from questions.views import create_question,question_list,update_question,delete_question


urlpatterns = [
  path("questions/",create_question,name="create_question"),
  path("question_list/",question_list,name="view_questions"),
  path("question_update/<str:pk>",update_question,name="update_question"),
  path("delete_question/<str:pk>",delete_question,name="delete_question"),
]