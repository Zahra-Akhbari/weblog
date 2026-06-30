from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator

from .forms import RegisterForm

from .models import Post
from .models import Category


from .forms import CommentForm


def home(request):

    # search
    posts = Post.objects.filter(status="published")

    query = request.GET.get("q")

    if query:
        # عنوان‌هایی را پیدا کن که این متن را داخل خودشان داشته باشند
        # (بدون حساسیت به حروف بزرگ و کوچک).
        posts = posts.filter(title__icontains=query)

    # pagination
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj, #این متغیرها را به Template بفرست.
        "query": query,  # برای استفاده بعدی در Template
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

        if not request.user.is_authenticated:
            return redirect("login")
        # فقط داده‌های کاربر را وارد شیء فرم کرده‌ایم.
        form=CommentForm(request.POST)

        # قسمت اعتبار سنجی
        if form.is_valid():

            # چون دو فیلد اجباری در مدل کامنت هنوز مقدار ندارن
            # پس یک شی میسازیم و میگیم کامنت بساز ولی ذخیره نکن در DB
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user
            comment.save()

            messages.success(request,"Your comment has been submitted successfully")

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


def register(request):

    if request.method == "POST":

        # فرم را با اطلاعاتی که کاربر ارسال کرده بساز.
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            # همین الآن کاربر را Login کن.
            login(request, user)

            return redirect("home")

    else:

        form = RegisterForm()

    context = {

        "form": form

    }

    return render(
        request,
        "blog/register.html",
        context,
    )

def category_posts(request, slug):

    category = get_object_or_404(Category,slug=slug)

    posts = Post.objects.filter(
        category=category,
        status="published"
    )

    context = {
        "category": category,
        "posts": posts,
    }

    return render(
        request,
        "blog/category_posts.html",
        context
    )
