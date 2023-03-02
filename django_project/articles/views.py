from django.http import HttpResponse
from articles.models import Article
from articles.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")

class ArticleListView(OwnerListView):
    model = Article
    template_name = "articles/article_list.html"

class ArticleDetailView(OwnerDetailView):
    model = Article
    template_name = "articles/article_detail.html"

class ArticleCreateView(OwnerCreateView):
    model = Article

    fields = ['title', 'text']

class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']

class ArticleDeleteView(OwnerDeleteView):
    model = Article
