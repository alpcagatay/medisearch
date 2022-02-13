#from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import CrawlStatus, Tag, PubmedDatabase

admin.site.register(Tag)
admin.site.register(PubmedDatabase)
admin.site.register(CrawlStatus)

#@admin.register(Tag)
#class TagAdmin(admin.ModelAdmin):
#    pass

#@admin.register(PubmedDatabase)
#class PubmedDatabaseAdmin(admin.ModelAdmin):
#    pass

#@admin.register(CrawlStatus)
#class CrawlStatus(admin.ModelAdmin):
#    pass