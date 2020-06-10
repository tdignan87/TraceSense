from django.shortcuts import render

def create_question(request):
    return render(request,"pages/new_question.html")