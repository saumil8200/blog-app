from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from .forms import BlogForm
from users.models import Profile

# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs.html', context)

def blog(request, pk):
    blogObj = Blog.objects.get(id=pk)
    context = {
        'blog': blogObj
    }
    return render(request, 'blogs/blog.html', context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blogs/categories.html', context)

def category(request, pk):
    category = Category.objects.get(id=pk)
    blogs = Blog.objects.filter(category=category)
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs.html', context)

@login_required(login_url="login")
def createBlog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            blog = form.save(commit=False)
            blog.owner = profile
            blog.save()
            return redirect('blogs')

    context = {
        'form': form
    }
    return render(request, 'blogs/blog_form.html', context)

@login_required(login_url="login")
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.user != blog.owner.user:
        return redirect('permission_denied')

    form = BlogForm(instance=blog)

    if request.method == 'POST':
        # print(request.POST)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    context = {
        'form': form
    }
    return render(request, 'blogs/blog_form.html', context)

@login_required(login_url="login")
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.user != blog.owner.user:
        return redirect('permission_denied')

    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')

    context = {
        'object': blog
    }
    return render(request, 'blogs/delete_template.html', context)