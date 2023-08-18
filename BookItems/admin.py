from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter= ['name', 'price']


admin.site.register(Passport)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)