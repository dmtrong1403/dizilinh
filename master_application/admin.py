from django.contrib import admin

from .models import SubCategory, DetailPost, DetailSubCategory, PostTag


#
# Category models
#

class DetailSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(DetailSubCategory, DetailSubCategoryAdmin)


#
# Post models
#


class DetailPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(DetailPost, DetailPostAdmin)

#
# Tag model
#

admin.site.register(PostTag)
