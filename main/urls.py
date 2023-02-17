from . import views
from django.urls import path
from django.views.generic import TemplateView


app_name = "main"

urlpatterns = [
    path("index.html", TemplateView.as_view(template_name="pages/index.html")),
    path("typography.html", TemplateView.as_view(template_name="pages/typography.html")),
    path("mdi.html", TemplateView.as_view(template_name="pages/mdi.html")),
    path("chartjs.html", TemplateView.as_view(template_name="pages/chartjs.html")),
    path("404.html", TemplateView.as_view(template_name="pages/404.html")),
    path("500.html", TemplateView.as_view(template_name="pages/500.html")),
]
