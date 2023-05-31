from django.shortcuts import render, redirect
from shop.models import Supplier
from shop.forms import SupplierForm


def supplier_list(request):
    suppliers = Supplier.objects.all()

    return render(
        request,
        "supplier_list.html",
        context={"title": "Lista de Proveedores", "suppliers": suppliers},
    )


def supplier_create(request):
    form = SupplierForm()

    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.is_active = False
            supplier.save()
            return redirect("supplier-list")

    return render(
        request,
        "form.html",
        {
            "form": form,
            "submit_value": "Crear",
            "title": "Crear Proveedor",
            "action": "btn-primary",
        },
    )


def supplier_update(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    form = SupplierForm(instance=supplier)

    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect("supplier-list")

    return render(
        request,
        "form.html",
        {
            "form": form,
            "submit_value": "Modificar",
            "title": "Modificar Proveedor",
            "action": "btn-warning",
        },
    )
