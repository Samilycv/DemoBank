from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(District)
admin.site.register(City)
admin.site.register(MaterialsProvide)