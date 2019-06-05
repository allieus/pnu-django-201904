from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('travel:post_detail', post.pk)
            # return redirect(post)  # Post모델에 get_absolute_url이 구현
    else:
        form = PostForm()
    return render(request, 'travel/post_form.html', {'form': form})


def post_edit(request, pk):
    pass


def post_list(request):
    return render(request, 'travel/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # comment_list = post.comment_set.all()
    # # comment_list = Comment.objects.filter(post=post)
    # comment_list = comment_list.order_by('-id')

    return render(request, 'travel/post_detail.html', {
        'post': post,
        # 'comment_list': comment_list,
        'comment_form': CommentForm(),
    })


@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('travel:post_detail', post_pk)
    else:
        form = CommentForm()

    return render(request, 'travel/comment_form.html', {'form': form})


@login_required
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, author=request.user, pk=pk)
    # if comment.author != request.user:

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('travel:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'travel/comment_form.html', {'form': form})


@login_required
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, author=request.user, pk=pk)
    if request.method == 'POST':
        comment.delete()  # 호출 즉시 DELETE 쿼리 수행
        return redirect('travel:post_detail', post_pk)
    return render(request, 'travel/post_confirm_delete.html', {
        'comment': comment,
    })
