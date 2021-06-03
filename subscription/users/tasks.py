from celery import task
from django.contrib.auth.models import User
from django.core.mail import send_mail
import datetime
from subscription.subscription import settings


@task(name='email_for_subs_end')
def subs_check():
    users = User.objects.filter(active_subs=True)
    for user in users:
        diff = datetime.date.today() - user.profile.subs_date.date()
        plan_validity = user.profile.plan_name.validity
        if diff.days >= plan_validity - 3:
            send_mail('Subscription ending soon',
                      'Your subscription is ending in less than 3 days.',
                      settings.EMAIL_HOST_USER,
                      [user.email])



