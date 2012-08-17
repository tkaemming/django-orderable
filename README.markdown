# django-orderable

Adds simple, drag-and-drop object ordering to the Django administration
change list view and to [inlines][inlines] within add/edit views.

[inlines]: https://docs.djangoproject.com/en/1.4/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin

## Installation

### Option A: pip

    pip install -e "git://github.com/tkaemming/django-orderable.git#egg=django-orderable"

### Option B: manual checkout

1. Clone the [django-orderable](http://github.com/tkaemming/django-orderable)
repository from [GitHub](http://www.github.com/).
2. Run `python setup.py install` to install the module package.

### Option C: PyPI

TODO.

## Using

1. Add `orderable` to the `INSTALLED_APPS` tuple for your Django project.
2. Make sure you have [Django staticfiles][staticfiles] configured.

[staticfiles]: https://docs.djangoproject.com/en/1.4/ref/contrib/staticfiles/

### Define Your Models

For any models that you would like to add ordering to, have these
models subclass `orderable.models.OrderableModel`.

Alternatively, (particularly if you are working with legacy data), you may
subclass `orderable.models.BaseOrderableModel`. Then ensure that you define
an `order` field (preferrably a `PositiveIntegerField`) and that you have
defined `ordering = ('order',)` in your `class Meta`.

### Adding Ordering to Change List View

Ensure that your model is orderable (see "Define Your Models" above).

Define your [ModelAdmin class][modeladmin] as usual, but subclass
`orderable.admin.OrderableAdmin` instead of `admin.ModelAdmin`.

[modeladmin]: https://docs.djangoproject.com/en/1.4/ref/contrib/admin/#modeladmin-objects

*Note*: Make sure that in your `ModelAdmin`, the `list_per_page` attribute
is set to a value that is greater than the possible number of objects (this
attribute defaults to 100). If you're looking to order an inordinate number
of model instances, you might want to look elsewhere for your ordering
solution.

### Adding Orderable Administration Inlines

Ensure that the model being inlined (the "inner" model) is orderable (see
"Define Your Models" above).

Define your [admin.py inlines][inlines] as usual, but subclass either
`orderable.admin.OrderableStackedInline` or
`orderable.admin.OrderableTabularInline` (instead of the standard
`admin.StackedInline` or `admin.TabularInline`).

"Stacked" inlines can be dragged from the "header" of the item.

"Tabular" inlines can be dragged from anywhere inside the item row.

[inlines]: https://docs.djangoproject.com/en/1.4/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin

### Caveats

Please note that this isn't a fool-proof solution to ordering objects in
every scenario. However, this app _is_ useful for small applications where
the change list will not be paginated beyond the first page of model
instances. There are a lot of cases where this application isn't the
appropriate solution (at least currently), such as objects that are ordered
with respect to a related object, situations where the `list_filter` will be
implemented, etc.

## Example Application

A test application is bundled with this repository, showing an example of
how to use `OrderableModel`, `BaseOrderableModel` and the various admin
classes.

The source code and usage instructions can be found in the `demosrc`
directory of this repository.

## Authors

* [Ted Kaemming](http://www.kaemming.com/)
* [Jannis Leidel](http://jezdez.me/)
* [Mike Tigas](http://mike.tig.as/)
