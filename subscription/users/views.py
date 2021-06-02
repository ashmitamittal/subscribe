from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PlanUpdateForm
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from .models import Plan, Profile
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'users/home.html', {'plans': list(Plan.objects.all())[1:]})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            dob_check = form.cleaned_data.get('date_of_birth')
            difference_in_years = relativedelta(date.today(), dob_check).years
            # print(difference_in_years)
            if difference_in_years >= 18:
                form.save()
                messages.success(request, f"Your account has been created! You can now Log In!")
                return redirect('login')
            else:
                messages.error(request, "Your account can't be created! You are underage!")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

        messages.success(request, f'Your account has been updated!')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
        }

    return render(request, 'users/profile.html', context)


class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan

    def post(self, request):
        if request.method == 'POST':
            plan = self.get_object()
            Profile.objects.filter(pk=self.request.user.pk).update(plan_name=plan.plan_name,
                                                                   subs_date=datetime.datetime.utcnow())
            messages.success(request, f'You have subscribed!')
            return redirect('user-home')