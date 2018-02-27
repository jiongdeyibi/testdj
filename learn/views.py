# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"新APP视图d")


def home(request):
    return render(request, 'home.html')
