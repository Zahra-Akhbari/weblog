from .models import Category, Tag, Post


def sidebar_data(request):
    return {
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "latest_posts": Post.objects.filter(
            status="published"
        ).order_by("-created_at")[:5],
    }