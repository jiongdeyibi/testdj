# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticle


def index(request):
    return HttpResponse(u"新APP视图d")


def home(request):
    return render(request, 'home.html')


def save(request):
    b = BlogArticle(title='1', author='2', time=3)
    b.save()
    return HttpResponse(u"新APP视图d")
