from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Article
from .forms import ArticleForm


@require_safe
def index(request):
    return render(request, 'articles/index.html')

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