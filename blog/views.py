from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import SearchForm


def post_list(request):
    form_search = SearchForm()
    home = 'home'

    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post_list.html', {
                      'page': page,
                      'posts': posts,
                      'home': home,
                      'form_search': form_search,
                  })


def post_detail(request, year, month, day, post):
    form_search = SearchForm()
    post = get_object_or_404(Post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form_search': form_search,
    })


def contact(request):
    contact = 'contact'
    return render(request, 'blog/contact.html', {
        'contact': contact,
    })


def about(request):
    about = 'about'
    return render(request, 'blog/about.html', {
        'about': about,
    })


def search(request):
    form_search = SearchForm()
    query = ''
    results = []
    if 'query' in request.GET:
        form_search = SearchForm(request.GET)
        if form_search.is_valid():
            query = form_search.cleaned_data['query']

    results = Post.published.filter(title__contains=query)

    return render(request, 'blog/search.html', {
        'query': query,
        'results': results,
        'form_search': form_search,
    })
