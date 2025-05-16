from django.contrib import admin

from .models import Trees, TreesImages

class TreesImageInLine(admin.StackedInline):
    model = TreesImages
    extra = 1
@admin.register(Trees)
class TreeAdmin(admin.ModelAdmin):
    inlines = [TreesImageInLine]
    #list_display = []
# Register your models here.
#admin.site.register(Trees)
admin.site.register(TreesImages)