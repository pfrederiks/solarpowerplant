from django.views.generic.base import TemplateView


class IntroductionView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IntroductionView, self).get_context_data(**kwargs)
        context['section'] = "introduction"


class AboutView(TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['section'] = "about"


class PrizesView(TemplateView):

    template_name = "prizes.html"

    def get_context_data(self, **kwargs):
        context = super(PrizesView, self).get_context_data(**kwargs)
        context['section'] = "prizes"
