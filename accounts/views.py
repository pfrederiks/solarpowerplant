from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Profile, ProfileForm


class RegisterView(CreateView):

    template_name = 'registration/register.html'
    form_class = auth.forms.UserCreationForm
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        form.save()
        new_user = auth.authenticate(username=self.request.POST['username'], password=self.request.POST['password1'])
        auth.login(self.request, new_user)
        new_profile = Profile(user=new_user, keep_me_up_to_date=True)
        new_profile.save()
        return super(RegisterView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = '/questionnaire/'
    model = Profile

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
