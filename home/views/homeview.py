# from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from django.conf import settings
from services.models import Package, Price
from home.models import Mission, Vision


class HomeView(generic.TemplateView):
    title = "HomePage"
    template_name = 'home/homepage.html'
    project_name = settings.PROJECT_TITLE

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs) :
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['project'] = self.project_name
        try:
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
            context['prices'] = Price.objects.all()
        except:
            pass
        try:
            vision = Vision.objects.get(is_active=True)
            context['vision'] = vision
        except:
            pass
        try:
            mission = Mission.objects.get(is_active=True)
            context['mission'] = mission
        except:
            pass
        return context


