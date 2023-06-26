from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from accounts.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.conf import settings
from django.views import generic
from services.models import Package, Service


class PasswordResetRequestView(generic.TemplateView):
    title = "Password Reset"
    def get(self, request, *args, **kwargs):
        password_reset_form = PasswordResetForm()
        context = self.get_context_data()
        context["password_reset_form"] = password_reset_form
        return render(request=self.request, template_name="registration/password_reset_form.html",context=context)

    def post(self, request, *args, **kwargs):
        password_reset_form = PasswordResetForm(self.request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email": data,
                        'domain': settings.EMAIL_SETUP_DOMAIN,
                        'site_name': settings.EMAIL_SETUP_SITENAME,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': settings.EMAIL_SETUP_PROTOCOL,
                    }
                    email_ = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email_, 'admin@example.com', [data], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')

                    messages.success(self.request, 'Check your email for instructions on how to reset your password.')
                    return redirect("home")
            else:
                messages.error(self.request, 'The email address you provided does not exist in our database')
                return redirect("home")

    def get_context_data(self, **kwargs) :
        context = super(PasswordResetRequestView, self).get_context_data(**kwargs)
        context['page_title'] = self.title
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

