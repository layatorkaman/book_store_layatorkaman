from django.contrib import admin
from .models import Book, Category

# Register your models here.
admin.site.site_header= "سايت تخصصي كتاب كودك"
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category,CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['img_tag','title','author', 'inventory', 'jcreated','category_to_str',]
    list_filter = ['title', 'inventory']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}

    def category_to_str(self, obj):
        return " , ".join([Category.title for Category in obj.category.all()])

    category_to_str.short_description = "دسته بندي"


admin.site.register(Book, BookAdmin)



