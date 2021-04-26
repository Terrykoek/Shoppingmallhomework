from shops.models import Shop
from shops.forms import ShopForm
from django.shortcuts import redirect, render

# Create your views here.


def view_index(request):
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shops_index')
    shops = Shop.objects.all()
    context = {"form": form, "shops": shops}
    return render(request, 'shops/index.html', context)


def view_show(request, pk):
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return redirect('shops_index')

    if request.GET.get('action') == 'del':
        shop.delete()
        return redirect('shops_index')

    if request.method == 'POST' and request.GET['action'] == 'edit':
        print("i am here")
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_show', shop.id)

    if request.GET.get('action') == 'edit':
        form = ShopForm(instance=shop)
        context = {"shop": shop, "edit": True, "form": form}
        return render(request, 'shops/show.html', context)

    context = {"shop": shop, "edit": False}
    return render(request, 'shops/show.html', context)