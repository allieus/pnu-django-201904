from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    return render(request, 'travel/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'travel/post_detail.html', {
        'post': post,
    })
