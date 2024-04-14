# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     response = HttpResponse()
#     response.writelines('<h1>Welcome to Django. I am Django hello world!</h1>')
#     response.write('This is app home!')
#     return response


from django.shortcuts import render
from django.http import HttpResponse
#Create your views here
def index(request):
    return render(request, 'page/home.html')