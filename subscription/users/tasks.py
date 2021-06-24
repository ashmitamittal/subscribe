# from celery import shared_task
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# import datetime
# from django.conf import settings
# from .models import Profile, Plan
#
#
# @shared_task(name='email_for_subs_end')
# def subs_check():
#     users = Profile.objects.filter(active_subs=True)
#     for user in users:
#         diff = datetime.date.today() - user.profile.subs_date.date()
#         plan_validity = user.plan_name.validity
#         if diff.days <= plan_validity - 3:
#             send_mail('Subscription ending soon',
#                       'Your subscription is ending in less than 3 days.',
#                       settings.EMAIL_HOST_USER,
#                       [user.user.email])
#
#
# @shared_task(name='task_for_subs_update')
# def subs_update():
#     users = Profile.objects.all()
#     for user in users:
#         diff = datetime.date.today() - user.subs_date.date()
#         plan_validity = user.plan_name.validity
#         if diff.days == plan_validity:
#             if user.profile.active_subs:
#                 Profile.objects.filter(user=user).update(plan_name=user.plan_name,
#                                                          subs_date=datetime.datetime.now(),
#                                                          active_subs=False)
#                 send_mail('Subscription Updated',
#                           f'Your {user.plan_name.plane_name} subscription has been updated.',
#                           settings.EMAIL_HOST_USER,
#                           [user.user.email])
#             else:
#                 Profile.objects.filter(user=user).update(plan_name=Plan.objects.first(),
#                                                          subs_date=None,
#                                                          active_subs=False)