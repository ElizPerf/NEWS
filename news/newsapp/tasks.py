from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@shared_task
def notify_about_new_posy(preview, pk, title, subscribers_emails):

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'http://127.0.0.1:8000/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

