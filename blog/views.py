from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def blogs(request):
    all_blogs = Blog.objects.order_by('-updated_at')
    return render(request, 'blog/blogs.html', {'blogs': all_blogs})


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog.html', {'blog': blog})
