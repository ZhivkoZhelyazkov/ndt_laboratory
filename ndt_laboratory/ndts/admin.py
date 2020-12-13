from django.contrib import admin
from ndt_laboratory.ndts.models import Ndt, Choose, Comment


class NdtAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'standard')


admin.site.register(Ndt, NdtAdmin)
admin.site.register(Choose)
admin.site.register(Comment)
