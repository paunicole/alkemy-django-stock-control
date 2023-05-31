from django.shortcuts import render, redirect
from shop.models import Product
from shop.forms import ProductForm


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "product_list.html",
        context={"title": "Lista de Productos", "products": products},
    )


def product_create(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.is_active = False
            product.save()
            return redirect("product-list")

    return render(
        request,
        "form.html",
        {
            "form": form,
            "submit_value": "Crear",
            "title": "Crear Producto",
            "action": "btn-primary",
        },
    )


def product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product-list")

    return render(
        request,
        "form.html",
        {
            "form": form,
            "submit_value": "Modificar",
            "title": "Modificar Producto",
            "action": "btn-warning",
        },
    )
