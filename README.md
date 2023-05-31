# Sistema de gestión de personas

## 📌 Premisa
Construir una aplicación con Django para agregar nuevos clientes y poder
listarlos.

## 📝 Requerimientos
Se pide crear un proyecto que podría ser llamado **StockControl**:

✔️ Agregar una app llamada compra.

✔️ Dentro de esta app se deben agregar los modelos Producto y
Proveedor (ver más abajo los fields requeridos).

✔️ El Producto debe estar relacionado con el Proveedor: entiéndase que
un Proveedor es una foreignkey en Producto.

✔️ Crear el archivo migration y ejecutarlo.

La aplicación debe proveer la **funcionalidad necesaria** para realizar las
siguientes operaciones:

- Agregar un nuevo Proveedor con el siguiente detalle:
  - nombre (texto)
  - apellido (texto)
  - dni (integer)
  - La idea es tener un formulario que permita agregar un nuevo
proveedor.

- Agregar un nuevo Producto con el siguiente detalle:
  - nombre (texto)
  - precio (float o integer)
  - stock_actual (integer)
  - proveedor (foreignkey con el modelo Proveedor)
  - La idea es tener un formulario que permita agregar un nuevo
producto.

- Listar todos los productos registrados en la base de datos:
  - La idea es tener disponible una vista que muestre el listado de
todos los productos a través de una tabla html.

## 📝 Acciones:
- Listar todos los productos registrados en la base de datos
- Permitir agregar un nuevo producto.
- Permitir agregar un nuevo proveedor.
- Tener disponible en el Admin el modelo del producto y del proveedor.

La aplicación debe permitir almacenar nuevos productos y proveedores para
luego mostrarlos en un listado.

## 🎁 Bonus (no obligatorio)
- Implementar uso de Bootstrap en los HTMLs
- Generar el listado de Proveedores.
- Generar el archivo **requirements** del proyecto

## ⚙️ Instalación
Primero tenemos que correr las migraciones de nuestra BD:
> python manage.py migrate

Luego, con un entorno de python creado:
> pip install -r requirements.txt

El cual descargará las librerías utilizadas por django. Finalmente para correr el proyecto utilizaremos:
> python manage.py runserver
