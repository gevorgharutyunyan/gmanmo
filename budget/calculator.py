from django.views.generic import TemplateView


class Calculator(TemplateView):
    template_name = "budget/calculator.html"
