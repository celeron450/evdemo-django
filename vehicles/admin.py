from django.contrib import admin

from .models import Make, MediaLicense, Model, ModelYear, Trim


admin.site.register(Make)
admin.site.register(Model)
admin.site.register(ModelYear)
admin.site.register(Trim)
admin.site.register(MediaLicense)
