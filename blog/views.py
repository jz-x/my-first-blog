from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Post
from django.utils import timezone


def post_list (request):
    
    # treat variable posts as the name of the QuerySet
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # {} is the place to add some things for the template to use
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail (request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
