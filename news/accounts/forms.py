from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_managers


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        subject = 'Welcome to our web news postal!'
        text = f'{user.username}, you have logged in successfully on website!'
        html = (
            f'<b>{user.username}</b>, you have logged in successfully on '
            f'<a href="http://127.0.0.1:8000/products">website</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_managers(
            subject='New user!',
            message=f'User {user.username} have logged in on website.'
        )

        # mail_admins(
        #     subject='New user!',
        #     message=f'User {user.username} have logged in on website.'
        # )
        #
        return user


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last nname")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )