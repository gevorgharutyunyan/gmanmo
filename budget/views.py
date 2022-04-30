from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from budget.forms import SignUpForm, LoginForm
from budget.models import Spent
from django.views.generic import TemplateView
from budget.config_params import headers, fields
from budget.utils import monthly_spent_dict


class MainMenu(TemplateView):
    template_name = "budget/main_menu.html"


class SpentLoginView(LoginView):
    template_name = "budget/login.html"
    fields = "__all__"
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("main-menu")


class RegisterPage(CreateView):
    form_class = SignUpForm
    template_name = "budget/register.html"
    success_url = reverse_lazy("spent")


class SpentCreate(LoginRequiredMixin, CreateView):
    model = Spent
    fields = fields
    success_url = reverse_lazy("spent")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SpentCreate, self).form_valid(form)


class SpentList(LoginRequiredMixin, ListView):
    model = Spent
    context_object_name = "spent"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spent"] = context["spent"].filter(user=self.request.user)
        context['header'] = headers

        context["month_spent"] = monthly_spent_dict()[0]
        return context


class EditSpent(LoginRequiredMixin, UpdateView):
    model = Spent
    fields = fields
    success_url = reverse_lazy("spent")


class SpentDelete(LoginRequiredMixin, DeleteView):
    model = Spent
    context_object_name = "item"
    success_url = reverse_lazy("spent")
