from django.shortcuts import render


def main(request):
    template_name = "djangokor/main.html"
    return render(request, template_name, {'title': '장고 한글 문서','text':'장고 한글 문서 첫페이지'})
