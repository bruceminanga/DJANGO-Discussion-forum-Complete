from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import PostForm
from .forms import commentForm, UserCreateForm
from .models import Post, Comment
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User


def index(request):

    return render(request, 'index.html', {})


def supportView(request):

    return render(request, 'support.html', {})


def work(request):

    return render(request, 'work.html', {})


def question(request):
   u = User.objects.get(username=request.user)
   print(u)
   question_list = Post.objects.all().order_by('-created_date')
   paginator = Paginator(question_list, 10)
   page= request.GET.get('page')
   questions = paginator.get_page(page)
   return render(request, 'question.html', {"questions": questions})


def preview(request):
   if request.method == "GET" and request.is_ajax():
      data = request.GET.get('title_prevw', False)
      print(data)
   
   return HttpResponse(data)


def preview2(request):
   if request.method == "GET" and request.is_ajax():
      data = request.GET.get('content_prevw', False)
      print(data)
   
   return HttpResponse(data)   


def post(request):
   if request.method == "POST":
      form = PostForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.published_date = timezone.now()
         print(request.user)
         post.author = request.user
         post.save()

         return redirect('post_details', pk=post.pk)
   else:
        form = PostForm()

   return render(request, 'post.html', {"form": form})
  

def post_details(request, pk):
   post = get_object_or_404(Post, pk=pk)
   post_list = Post.objects.all().order_by('-created_date')
   if request.method == "POST":
      form = commentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.post= post
         # print(request.user)
         comment.author = request.user
         comment.save()
         # return redirect('post_details', pk=post.pk)
   else:          
      form  = commentForm()    
   comments = Comment.objects.filter(post=post)
   return render(request, 'post_details.html', {"post": post, 'form': form, 'comments': comments })


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('question')  
   

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('question')
    else:
        form = PostForm(instance=post)
    return render(request, 'post.html', {'form': form})   



def search(request):
   template = 'question.html'
   query = request.get.GET(q) 
   results = Post.objects.filter(Q(title__icontains=query) | Q(content__iconains=query))
   return render(request, template, {'form': form})


