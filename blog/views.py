from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Post
def index(request,pk):
    posts = get_object_or_404(Post,pk=pk)
    print(posts)
    context = {
        "posts":posts,
    }
    return render(request, 'more.html', context)