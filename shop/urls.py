from django.urls import path
from . import views
from .custom_views import supplier_views, product_views

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "shop/suppliers/list",
        supplier_views.supplier_list,
        name="supplier-list",
    ),
    path(
        "shop/suppliers/create", supplier_views.supplier_create, name="supplier-create"
    ),
    path(
        "shop/suppliers/update/<int:supplier_id>",
        supplier_views.supplier_update,
        name="supplier-update",
    ),
    path(
        "shop/products/list",
        product_views.product_list,
        name="product-list",
    ),
    path("shop/products/create", product_views.product_create, name="product-create"),
    path(
        "shop/products/update/<int:product_id>",
        product_views.product_update,
        name="product-update",
    ),
]
