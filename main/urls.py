from . import views
from django.urls import path
from django.views.generic import TemplateView


app_name = "main"

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/blank-page.html")),
    path("basic_elements.html", TemplateView.as_view(template_name="pages/basic_elements.html")),
    path("basic-table.html", TemplateView.as_view(template_name="pages/basic-table.html")),
    path("blank-page.html", TemplateView.as_view(template_name="pages/blank-page.html")),
    path("buttons.html", TemplateView.as_view(template_name="pages/buttons.html")),
    path("chartjs.html", TemplateView.as_view(template_name="pages/chartjs.html")),
    path("404.html", TemplateView.as_view(template_name="pages/404.html")),
    path("500.html", TemplateView.as_view(template_name="pages/500.html")),
    path("login.html", TemplateView.as_view(template_name="pages/login.html")),
    path("mdi.html", TemplateView.as_view(template_name="pages/mdi.html")),
    path("register.html", TemplateView.as_view(template_name="pages/register.html")),
    path("typography.html", TemplateView.as_view(template_name="pages/typography.html")),
    path("index.html", TemplateView.as_view(template_name="pages/index.html")),
]
