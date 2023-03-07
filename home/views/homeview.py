# from django.contrib import messages
from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.views import generic
# from accounts.models import User
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, generic.TemplateView):
    title = "HomePage"
    template_name = 'home/homepage.html'
    project_name = settings.PROJECT_TITLE

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        user_ = self.request.user.email
        context['title'] = self.title
        context['project'] = self.project_name
        return render(request, self.template_name, context)
        # try:
        #
        #     # context['form']= form
        #     return render(request, self.template_name, context)
        # except:
        #     messages.error(self.request,"You cannot log in without registering as a Researcher!!")
        #     return HttpResponseRedirect("/accounts/login/")

    def get_context_data(self, **kwargs) :
        context = super(HomeView, self).get_context_data(**kwargs)
        return context