from operator import ipow
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    reverse
)
from django.forms.models import model_to_dict

from .utils import _get_page
from .models import ITAsset


def index(request):
    ''' Главная страница. '''
    template = 'itasset/index.html'
    assets = ITAsset.objects.all()

    page_obj = _get_page(request, assets)

    context = {
        'page_obj': page_obj,
        'pages_count': page_obj.paginator.page_range,
    }
    return render(request, template, context)

def asset_detail(request, itasset_id):
    ''' Страница ассета. '''
    itasset = get_object_or_404(ITAsset, pk=itasset_id)
    context = {
        'itasset': itasset,
    }
    return render(request, 'itasset/itasset_detail.html', context)