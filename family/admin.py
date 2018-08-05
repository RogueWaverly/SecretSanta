from django.contrib import admin

from .models import Pool, ImmFamily, Member

# Register your models here.
admin.site.register(Pool)
admin.site.register(ImmFamily)
admin.site.register(Member)
