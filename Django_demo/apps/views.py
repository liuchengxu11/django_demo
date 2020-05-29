from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Projects(View):
    def get(self,request,pk):

        return HttpResponse("get请求")

    def post(self,request,pk):
        print(pk)
        return HttpResponse("post请求")

    def put(self,request,pk):

        return HttpResponse("put请求")
