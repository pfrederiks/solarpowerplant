from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Questions, QuestionsForm


class QuestionsView(LoginRequiredMixin, View):
    form_class = QuestionsForm
    template_name = 'questions.html'

    def get(self, request, *args, **kwargs):
        questions, _ = Questions.objects.get_or_create(user=request.user)
        form = QuestionsForm(instance=questions)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        questions, _ = Questions.objects.get_or_create(user=request.user)
        form = self.form_class(request.POST, instance=questions)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/questionnaire/thanks/')

        return render(request, self.template_name, {'form': form})


class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        context['section'] = "thanks"


