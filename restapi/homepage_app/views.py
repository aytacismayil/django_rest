from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from rest_framework.authtoken.models import Token
class HomePage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id is not None:
            context['token'] = Token.objects.filter(user=self.request.user)
        return context

    