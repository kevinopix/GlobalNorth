from django.contrib import messages
from django.middleware.csrf import rotate_token
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.edit import UpdateView
from accounts.models import UserProfile
from accounts.forms import UserProfileUpdateForm
from django.conf import settings
from services.models import Package


class UserProfileUpdateView(generic.TemplateView):
    model = UserProfile
    form_class = UserProfileUpdateForm
    template_name = 'accounts/update_userprofile.html'
    project_name = settings.PROJECT_TITLE
    title = "Update User Profile"

    def get(self, request, *args, **kwargs):
        profile_pk = kwargs['pk']
        userprofile = get_object_or_404(self.model, pk=profile_pk)
        userprofile_pk = profile_pk
        user_profile_pk = self.request.user.profile_pk_value
        if userprofile_pk == user_profile_pk or self.request.user.is_staff:
            context = self.get_context_data()
            context['userprofile'] = userprofile
            context['project'] = self.project_name
            user_mail = self.request.user.email
            context['user_mail'] = user_mail
            context['form'] = self.form_class
            context['location'] = userprofile.location
            rotate_token(self.request)
            return render(request, self.template_name, context)
        elif userprofile_pk != user_profile_pk and not self.request.user.is_staff:
            context = self.get_context_data()
            context['userprofile'] = userprofile
            context['project'] = self.project_name
            context['profile_pk'] = userprofile.pk
            rotate_token(self.request)
            messages.error(self.request, "You are only able to view/edit your own user profile!!")
            return redirect('/accounts/profile/{a}/view'.format(a=user_profile_pk))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            print(location)
            userprofile = get_object_or_404(self.model, pk=kwargs['pk'])
            userprofile.location = location
            userprofile.save()
            messages.success(self.request, 'User Profile Updated Successfully')
            return redirect('/accounts/profile/{a}/view'.format(a=userprofile.pk))

    def get_context_data(self, **kwargs) :
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        context['project'] = self.project_name
        context["page_title"] = self.title
        try:
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
        except:
            pass
        return context
