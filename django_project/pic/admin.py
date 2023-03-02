from django.contrib import admin
from pic.models import Pic

class PicAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')

admin.site.register(Pic,PicAdmin)
