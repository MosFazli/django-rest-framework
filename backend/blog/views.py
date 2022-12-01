from django.views.generic import ListView
from .models import Article

class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)