from django.contrib import admin
from .models import category, item, delivery

admin.site.register(category)
admin.site.register(item)
admin.site.register(delivery)

#models have been registered for use by the admin panel