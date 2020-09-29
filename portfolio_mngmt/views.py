from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import AccountForm
from django.urls import reverse_lazy


class HomePage(SuccessMessageMixin, CreateView):
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'
    success_message = "User account was created successfully."