from django import forms
from .models import Comment

from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
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

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"



            placeholders = {
                "username": "Enter your username",
                "email": "Enter your email",
                "password1": "Enter password",
                "password2": "Repeat password",
            }

            for name, field in self.fields.items():
                field.widget.attrs["class"] = "form-control"

                field.widget.attrs["placeholder"] = placeholders.get(name,"")




    def clean_email(self):
        # ایمیلی که کاربر وارد کرده و قبلاً اعتبارسنجی اولیه شده را بردار بریز تو دیکشنری
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "This email is already registered."
            )

        return email



class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ["body"]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["body"].widget.attrs.update({

            "class": "form-control",

            "rows": 4,

            "placeholder": "Write your comment..."

        })