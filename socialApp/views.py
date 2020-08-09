from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . forms import UserCreationForm
from . models import Profile

class HomepageView(generic.TemplateView):
    template_name = 'socialApp/home.html'

class UserRegistrationView(generic.CreateView):
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    template_name = 'socialApp/register.html'

def home(request):
    return render(request, 'socialApp/home.html')
