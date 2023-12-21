from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
def about(request):
    return render(request, 'about.html')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    form = PostForm()
    context = {'form': form}
    return render(request, 'create.html', context)