from store_settings.models import StoreSettings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def dynamic_css(request):
    store_settings = StoreSettings.objects.first()
    background_url = store_settings.main_page_image.url if store_settings and store_settings.main_page_image else "/static/default-bg.jpg"

    css_content = f"""
    body {{
        background: url("{background_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    """

    return HttpResponse(css_content, content_type="text/css")
