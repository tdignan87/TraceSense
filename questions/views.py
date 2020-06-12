from django.shortcuts import render,redirect
from .forms import GMPQuestions
from .models import Gmp_questions


def create_question(request):
    """ Function for creating a new question"""
    questions_form = GMPQuestions()
    form_class = GMPQuestions()
    if request.method == "POST":
        form = GMPQuestions(request.POST)
        if form.is_valid():
            createQuestion = form.save(commit=False)
            createQuestion.user_id = request.user.id
            form.save()
            return redirect(question_list)
    context = {'form':questions_form}
    return render(request,"pages/new_question.html",context)

def question_list(request):
    """ Function for returning list of questions from db"""
    question = Gmp_questions.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_questions.html",{"question":question})

def update_question(request,pk):
    """Function for updating the questions in the system"""
    question = Gmp_questions.objects.get(gmp_questionid=pk)
    form = GMPQuestions(instance=question)
    if request.method == "POST":
        form = GMPQuestions(request.POST,instance=question)
        if form.is_valid():
            form.save()
            return redirect(question_list)
    context = {'form':form}
    return render(request,"pages/new_question.html",context)

def delete_question(request,pk):
    """ Function for deleting question from the database"""
    question = Gmp_questions.objects.get(gmp_questionid=pk)
    if request.method == "POST":
        question.delete()
        return redirect(question_list)
    
    context={'question':question}
    return render(request, 'pages/delete_question.html',context)
    
    
    