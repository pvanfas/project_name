from django.contrib import messages
from django.contrib.sites.models import Site
from django.conf import settings


def main_context(request):
    if not Site.objects.filter(pk=settings.SITE_ID).exists():
        Site(pk=settings.SITE_ID, domain=request.META["HTTP_HOST"], name="Site Name").save()
    return {
        "domain": request.META["HTTP_HOST"],
        "site_name": "Site Name",
        "footer_text": "Copyright Site Name. All rights reserved.",
        "attribution_text": "Designed by <a href='http://pvanfas.com'>PV Anfas</a>",
    }
