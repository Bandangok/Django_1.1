from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    all_phones = Phone.objects.all()

    if sort_pages == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'name':
        phones = all_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': all_phones}
    return render(request, template, context)


# def show_product(request, slug):
#
#     template = 'product.html'
#     phone = Phone.objects.filter(slug__contains=slug).first()
#     context = {'phones': phone}
#     return render(request, template, context)


def list_person(request):
    phone_objects = Phone.objects.all()
    phones = [f'{p.id}, {p.name}, {p.price}, {p.image}, {p.release_date}, {p.lte_exists}, {p.slug}' for p in phone_objects]
    return HttpResponse('<br>'.join(phones))

def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone_objects = Phone.objects.all()
    for phone in phone_objects:
        if phone.slug == slug:
            context['phone'] = phone
    return render(request, template, context)