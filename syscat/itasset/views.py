import string
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings

from .forms import ITAssetForm
from .models import ITAsset, ITAssetGroup
from .utils import _get_page


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


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


@login_required(login_url='users:login')
def asset_detail(request, itasset_id):
    ''' Страница ассета. '''
    itasset = get_object_or_404(ITAsset, pk=itasset_id)
    itasset.userlist = settings.ENCODED_FIELD_DENIED
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
            post.slug = slugify(rand_slug() + "-" + post.title)
            post.save()
            files = request.FILES.getlist('file_field')
            for file in files:
                print(file)

            form.save_m2m()
            return redirect(reverse('itasset:main'))
        else:
            return render(request, 'itasset/add_itasset.html',
                          {'form': form, 'is_edit': False})

    form = ITAssetForm()
    return render(request, 'itasset/add_itasset.html',
                  {'form': form, 'is_edit': False})

# Страница редактирования поста.
@login_required(login_url='users:login')
def asset_edit(request, asset_id):
    asset = get_object_or_404(ITAsset, pk=asset_id)

    if request.user != asset.author:
        return redirect(reverse('itasset:itasset_detail', args=[asset_id]))

    if request.method == 'POST':
        form = ITAssetForm(
            request.POST or None,
            files=request.FILES or None,
            instance=asset
        )
        if form.is_valid():
            asset.created = timezone.now()
            form.save()
            return redirect(reverse('itasset:itasset_detail', args=[asset_id]))

    form = ITAssetForm(instance=asset)
    return render(request, 'itasset/add_itasset.html',
                  {'form': form, 'is_edit': True})


@login_required
def itasset_list(request):
    template = 'itasset/group_assets.html'

    assets = None
    group_id = request.GET.get('group', None)
    if group_id is not None:
        group = get_object_or_404(ITAssetGroup, pk=group_id)
        assets = group.itasset.order_by('title')
    else:
        assets = ITAsset.objects.all().order_by('title')

    page_obj = _get_page(request, assets)

    context = {
        'group': ITAssetGroup.objects.all(),
        'page_obj': page_obj,
        'pages_count': page_obj.paginator.page_range,
    }
    return render(request, template, context)
