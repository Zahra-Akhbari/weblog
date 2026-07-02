from .models import Category, Tag, Post
from django.db.models import Count

def sidebar_data(request):
    return {
        "categories": Category.objects.annotate(post_count=Count("posts")),
        "tags": Tag.objects.all(),
        "latest_posts": Post.objects.filter(status="published").order_by("-created_at")[:5],
    }


