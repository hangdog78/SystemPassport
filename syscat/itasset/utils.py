from django.core.paginator import Page, Paginator

from django.conf import settings


def _get_page(request, assets) -> Page:
    paginator = Paginator(assets, settings.PAGE_SIZE)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return page_obj
