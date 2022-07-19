from operator import ipow
from django.shortcuts import render

from .utils import _get_page
from .models import SysTopology


# Create your views here.

# Главная страница
def index(request):
    template = 'itasset/index.html'
    assets = SysTopology.objects.all()

    page_obj = _get_page(request, assets)

    context = {
        'page_obj': page_obj,
        'pages_count': page_obj.paginator.page_range,
    }
    return render(request, template, context)