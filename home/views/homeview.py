# from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from django.conf import settings


class HomeView(generic.TemplateView):
    title = "HomePage"
    template_name = 'home/homepage.html'
    project_name = settings.PROJECT_TITLE

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title
        context['project'] = self.project_name
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs) :
        context = super(HomeView, self).get_context_data(**kwargs)
        return context