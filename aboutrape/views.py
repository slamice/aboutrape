from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from aboutrape.models import Category, Comment, UserProfile
import json

def about(request):
    users = UserProfile.objects.all()
    return render(request, 'templates/comments/about.html', {'categories':categories})

def base(request):
    categories = Category.objects.all()
    return render(request, 'templates/comments/about.html', {'categories':categories})

def category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    comments = Comment.objects.filter(category_id=category_id)
    return render(request, 'templates/comments/category.html', {'categories':categories, 'category': category, 'comments': comments})