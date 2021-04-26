from django.contrib import admin
from home.models import *

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

class packages(admin.ModelAdmin):
    list_display    = ('pkg_name', 'pkg_price', 'get_classes')

admin.site.register(Package, packages)

# https://medium.com/hackernoon/automatically-register-all-models-in-django-admin-django-tips-481382cf75e5
# how to add all models and also list all the fields

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass