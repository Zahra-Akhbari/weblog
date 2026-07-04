from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator

from .forms import RegisterForm
from .forms import PostForm

from .models import Post
from .models import Category
from .models import Tag

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

def Tag_posts(request, slug):

    tag = get_object_or_404(Tag,slug=slug)

    posts = Post.objects.filter(
        tags=tag,
        status="published"
    )

    context = {
        "tag": tag,
        "posts": posts,
    }

    return render(
        request,
        "blog/Tag_posts.html",
        context
    )

@login_required
def create_post(request):

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES # برای ارسال تصویر است
        )

        if form.is_valid(): #اعتبارسنجی فرم

            post = form.save(commit=False) #شیء Post ساخته می‌شود ولی هنوز در دیتابیس ذخیره نشده است

            post.author = request.user #نویسنده را از کاربر لاگین‌شده می‌گیریم

            post.save()

            form.save_m2m()

            return redirect(
                "post_detail",
                slug=post.slug
            )

    else:

        form = PostForm()

    context = {
        "form": form
    }

    return render(
        request,
        "blog/create_post.html",
        context
    )


@login_required
def dashboard(request):

    posts = Post.objects.filter(
        author=request.user # هر نویسنده باید پست های خودش رو ببینه
    ).order_by("-created_at")

    context = {
        "posts": posts
    }

    return render(
        request,
        "blog/dashboard.html",
        context
    )
