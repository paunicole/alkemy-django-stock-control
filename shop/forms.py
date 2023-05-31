from django.forms import ModelForm
from .models import Supplier, Product


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        labels = {"first_name": "Nombre", "last_name": "Apellido", "dni": "DNI"}


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "name": "Nombre",
            "price": "Precio",
            "stock_current": "Stock Actual",
            "supplier": "Proveedor",
        }
