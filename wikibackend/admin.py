from django.contrib import admin

from wikibackend import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.WikiPage)
admin.site.register(models.WikiPage2Customer)
