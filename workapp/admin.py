from django.contrib import admin
from .models import Worker, Orderer

# Register your models here.
admin.site.register(Worker)
admin.site.register(Orderer)