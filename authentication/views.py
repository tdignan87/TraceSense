from django.shortcuts import render

def main_page(request):
    return render(request,"pages/index.html")

def support_page(request):
    return render(request,"pages/support.html")
