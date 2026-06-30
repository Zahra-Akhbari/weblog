from django import forms
from .models import Comment

from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        # ایمیلی که کاربر وارد کرده و قبلاً اعتبارسنجی اولیه شده را بردار بریز تو دیکشنری
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "This email is already registered."
            )

        return email
