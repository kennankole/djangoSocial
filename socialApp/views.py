from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . forms import UserCreationForm, ProfilesUpdateForm
from . models import Profiles
from . utils import ProfileGetObjectMixin


class HomepageView(generic.TemplateView):
    template_name = 'socialApp/home.html'

class UserRegistrationView(generic.CreateView):
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    template_name = 'socialApp/register.html'

def home(request):
    return render(request, 'socialApp/home.html')



class ProfileDetail(ProfileGetObjectMixin,generic.DetailView):
    model = Profiles
    template_name = 'socialApp/profile_detail.html'
    

class ProfileUpdate(ProfileGetObjectMixin, generic.UpdateView):
    model = Profiles
    form_class = ProfilesUpdateForm
    


class PublicProfiles(generic.DetailView):
    model = Profiles