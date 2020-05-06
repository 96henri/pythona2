from django.shortcuts import render
from django.http import HttpResponse

def home2(request):
 return render(request, 'ddjango/home.html')


def home(request):
 html = "<html><body>Template - Cadastro de Produtos - Y72W</body></html>"
 return HttpResponse(html)