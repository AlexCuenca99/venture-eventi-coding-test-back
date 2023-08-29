from django.contrib import admin

from .models import MovementType, Movement

admin.site.register(Movement)
admin.site.register(MovementType)
