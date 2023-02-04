def main_context(request):
    return {
        "domain": request.META["HTTP_HOST"],
        "site_name": "Site Name",
        "footer_text": "Copyright Site Name. All rights reserved.",
        "attribution_text": "Designed by <a href='http://pvanfas.com'>PV Anfas</a>",
    }
