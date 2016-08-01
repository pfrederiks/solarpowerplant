from django.views.generic.base import TemplateView


class IntroductionView(TemplateView):

    template_name = "index.html"

class AboutView(TemplateView):

    template_name = "about.html"

class PrizesView(TemplateView):

    template_name = "prizes.html"

