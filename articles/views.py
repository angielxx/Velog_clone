from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe

from accounts.models import User
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_safe
def index(request):
    articles = Article.objects.all()
    users = User.objects.all()
    comments = Comment.objects.all()
    context = {
        'articles': articles,
        'users': users,
        'comments': comments,
    }
    return render(request, 'articles/index.html', context)

# @require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'page_title': 'velog',
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def search(request):
    param = request.GET.get('param')
    print(param)
    return render(request, 'articles/search.html')

# detail
@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article_id=pk)
    form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)

# comment
@require_http_methods(['POST'])
def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)
    return redirect('accounts:login')