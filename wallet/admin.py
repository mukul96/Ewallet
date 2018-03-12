from django.contrib import admin
from wallet.models import Person
class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

# Register your models here.
