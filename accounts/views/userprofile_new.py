from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserProfileCreationForm
from accounts.models import User, UserProfile
from django.views import generic
from django.conf import settings
from django.middleware.csrf import rotate_token
from services.models import Package, Service
from termsandconditions.models import Terms
from django.utils import timezone


class UserProfileRegisterView(LoginRequiredMixin, generic.TemplateView):
    form_class = UserProfileCreationForm
    template_name = 'accounts/new_userprofile.html'
    project_name = settings.PROJECT_TITLE
    title = "New User Profile"

    def get(self, request):
        user_profile_pk = self.request.user.profile_pk_value
        if user_profile_pk is not None and user_profile_pk > 0 and not self.request.user.is_staff:
            messages.info(self.request, 'Your User Profile Already Exists')
            return redirect('/accounts/profile/{a}/view'.format(a=user_profile_pk))
        else:
            form = self.form_class(None)
            context = self.get_context_data()
            context['form'] = form
            context['project'] = self.project_name
            user_mail = self.request.user.email
            context['user_mail'] = user_mail
            context['terms'] = Terms.objects.get(is_active=True)
            rotate_token(self.request)
            return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        user_mail = self.request.user.email
        context = self.get_context_data()
        if form.is_valid():
            accepted = request.POST.get('terms_conditions_accepted')
            if accepted == "on":
                print(request.POST.get('terms_conditions_accepted'))
                location = request.POST.get('location')
                existing_user = User.objects.get(email=user_mail)
                try:
                    existing_profile = UserProfile.objects.get(user__pk = existing_user.pk)
                    messages.info(self.request, 'UserProfile already Exists! You can only edit profile')
                    return redirect('/accounts/profile/{a}/view'.format(a=existing_profile.pk))
                except:
                    userprofile = UserProfile(
                        user=existing_user,
                        location=location,
                        is_active=True,
                        terms_conditions_accepted = True
                    )
                    userprofile.date_terms_accepted = timezone.now()
                    userprofile.save()
                    saved_profile = UserProfile.objects.get(user=existing_user)
                    saved_profile_user = User.objects.get(email=saved_profile.user.email)
                    saved_profile_user.profile_pk_value = saved_profile.pk
                    saved_profile_user.save()
                    messages.success(self.request,'New User Profile Added Successfully')
                    return redirect('/accounts/profile/{a}/view'.format(a=saved_profile.pk))
            else:
                form = self.form_class(None)
                context = self.get_context_data()
                context['form'] = form
                context['project'] = self.project_name
                user_mail = self.request.user.email
                context['user_mail'] = user_mail
                context['terms'] = Terms.objects.get(is_active=True)
                rotate_token(self.request)
                messages.warning(self.request, "Terms and Conditions have to be accepted to Proceed!")
                return redirect('/accounts/profile/new')
        else:
            messages.error(self.request, 'User Profile Not Added. Restart UserProfile Registration Process!')
            context['form'] = form
            context['project'] = self.project_name
            rotate_token(self.request)
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs) :
        context = super(UserProfileRegisterView, self).get_context_data(**kwargs)
        context["page_title"] = self.title
        try:
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
        except:
            pass
        try:
            services = Service.objects.filter(is_active=True)
            context['services'] = services
        except:
            pass
        return context
