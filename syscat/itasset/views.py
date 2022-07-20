from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils import timezone

from .forms import ITAssetForm
from .models import ITAsset
from .utils import _get_page


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


@login_required(login_url='users:login')
def asset_create(request):
    ''' Страница создания ассета.'''
    if request.method == 'POST':
        form = ITAssetForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = timezone.now()
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect(reverse('itasset:main'))
        else:
            return render(request, 'itasset/add_itasset.html',
                          {'form': form, 'is_edit': False})

    form = ITAssetForm()
    return render(request, 'itasset/add_itasset.html',
                  {'form': form, 'is_edit': False})
