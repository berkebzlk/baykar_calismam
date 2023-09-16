from django.contrib import admin
from .models import IHA, IHAUser


@admin.register(IHA)
class IHAAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("model_name",)}


admin.site.register(IHAUser)
