from django.contrib import admin
from .models import Post, AboutUS, User, ProductCard

class ProductAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'price', 'description')
    list_filter = ['price']

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display=('user','title','text','date_post')
#     list_filter=('user','date_post')
#     fieldsets = (
#         ('Основная информация', {'fields' : ('user', 'title')}),
#         ('Содержание', {'fields' : ('text', 'date_post')})
#     )
class PostInLine(admin.TabularInline):
    model= Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','role']
    inlines = [PostInLine]

admin.site.register(AboutUS)
admin.site.register(Post)
admin.site.register(ProductCard, ProductAdmin)
