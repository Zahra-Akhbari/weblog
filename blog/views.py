from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Post

from .forms import CommentForm


def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(
        request,
        'blog/home.html',
        context
    )

def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status='published'
    )
    if request.method == 'POST':
        # فقط داده‌های کاربر را وارد شیء فرم کرده‌ایم.
        form=CommentForm(request.POST)

        # قسمت اعتبار سنجی
        if form.is_valid():

            # چون دو فیلد اجباری در مدل کامنت هنوز مقدار ندارن
            # پس یک شی میسازیم و میگیم کامنت بساز ولی ذخیره نکن در DB
            comment = form.save(commit=False)
            comment.post = post
            comment.author = User.objects.first()
            comment.save()

            return redirect(
                'post_detail',
                slug=post.slug
            )


    else:
        # یک فرم خالی بساز.
        form=CommentForm()


    context = {
        'post': post,
        'form': form,
    }

    return render(
        request,
        'blog/post_detail.html',
        context
    )