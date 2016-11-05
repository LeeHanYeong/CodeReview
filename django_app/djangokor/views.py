from django.shortcuts import render


def main(request):
    template_name = "djangokor/main.html"
    return render(request, template_name, {'title': '장고 한글 문서','text':'장고 한글 문서 시작페이지'})


def document(request):
    template_name = "djangokor/document.html"
    return render(request, template_name, {'title': '목차','text':'장고 한글 문서 목차'})
