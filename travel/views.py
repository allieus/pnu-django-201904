from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import CommentForm


def post_list(request):
    return render(request, 'travel/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'travel/post_detail.html', {
        'post': post,
    })


def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('travel:post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'travel/comment_form.html', {'form': form})
