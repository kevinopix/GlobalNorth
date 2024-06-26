from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import User, UserProfile
from django.views import generic
from django.conf import settings
from django.middleware.csrf import rotate_token
from services.models import Package, Service


class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/view_userprofile.html'
    project_name = settings.PROJECT_TITLE
    model = UserProfile
    title = "View Profile"

    def get(self, request, *args, **kwargs):
        profile_pk = kwargs['pk']
        try:
            userprofile = get_object_or_404(self.model, pk=profile_pk)
            userprofile_pk = profile_pk
            user_profile_pk = self.request.user.profile_pk_value
            if userprofile_pk == user_profile_pk or self.request.user.is_staff:
                context = self.get_context_data()
                context['userprofile'] = userprofile
                context['project'] = self.project_name
                context['profile_pk'] = userprofile.pk
                rotate_token(self.request)
                return render(request, self.template_name, context)
            elif userprofile_pk != user_profile_pk and not self.request.user.is_staff:
                context = self.get_context_data()
                context['userprofile'] = userprofile
                context['project'] = self.project_name
                context['profile_pk'] = userprofile.pk
                rotate_token(self.request)
                messages.error(self.request, "You are only able to view your own user profile!!")
                return redirect('/accounts/profile/{a}/view'.format(a=user_profile_pk))
        except Exception:
            messages.error(self.request, "User Profile Does NOT exist.")
            return redirect('/accounts/profile/new')

    def get_context_data(self, **kwargs) :
        context = super(UserProfileView, self).get_context_data(**kwargs)
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
        try:
            from testimonials.models import Testimony
            testimonials = Testimony.objects.filter(is_active=True)
            context['testimonials'] = testimonials
        except:
            pass
        return context
